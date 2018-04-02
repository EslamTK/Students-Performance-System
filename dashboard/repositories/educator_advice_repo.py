from dashboard.models import *
from .repo import Repo


class EducatorAdviceRepo(Repo):
    def __init__(self):
        super().__init__(EducatorAdvice)

    def get_student_advices(self, student):
        return EducatorAdvice.objects.filter(student=student)
