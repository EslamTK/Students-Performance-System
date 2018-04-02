from dashboard.models import *
from .repo import Repo


class StudentCourseRepo(Repo):
    def __init__(self):
        super().__init__(StudentCourse)

    def get_student_courses(self, student):
        return StudentCourse.objects.filter(student=student)

    def get_student_courses(self, student, is_current):
        return StudentCourse.objects.filter(student=student).exclude(final_grade__isnull=not is_current)
