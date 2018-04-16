from dashboard.models import *
from .repo import Repo


class EducatorAdviceRepo(Repo):
    def __init__(self):
        super().__init__(EducatorAdvice)

    def get_student_advices(self, student):
        advices = self._model.objects.filter(student=student). \
            select_related('educator').order_by('created_at')

        return advices

    def add_student_advice(self, student, educator, content):
        advice = self._model(student_id=student, educator_id=educator, content=content)

        advice.save()
