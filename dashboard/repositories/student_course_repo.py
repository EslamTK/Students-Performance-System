from dashboard.models import *
from .repo import Repo


class StudentCourseRepo(Repo):
    def __init__(self):
        super().__init__(StudentCourse)

    def get_student_courses(self, student):
        return StudentCourse.objects.filter(student=student)
