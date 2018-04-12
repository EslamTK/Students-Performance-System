from django.db.models import Q

from dashboard.models import *
from .repo import Repo


class CourseRepo(Repo):
    def __init__(self):
        super().__init__(Course)

    # To be edit
    def get_available_student_courses(self, student):
        courses = Course.objects.exclude((Q(studentcourse__student=student) &
                                          (Q(studentcourse__final_grade__gte=50) |
                                           Q(studentcourse__final_grade__isnull=True))))

        return courses

# If the course is in the student year and the student doesn't has it
# If the student fail in the course and didn't pass yet
