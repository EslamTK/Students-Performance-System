from dashboard.models import *
from .repo import Repo


class ReportRepo(Repo):
    def __init__(self):
        super().__init__(Report)

    def add_report(self, review_id):
        report = self._model(student_review_id=review_id)

        report.save()
