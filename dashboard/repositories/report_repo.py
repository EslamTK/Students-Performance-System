from dashboard.models import *
from .repo import Repo


class ReportRepo(Repo):
    def __init__(self):
        super().__init__(Report)

    def add_report(self, review_id):
        report = self._model(student_review_id=review_id)

        report.save()

    def get_all(self, educator=None, is_closed=False):
        reports = self._model.objects.filter(is_closed=is_closed, student_review__educator=educator) \
            .select_related('student_review', 'student_review__student', 'student_review__educator') \
            .order_by('-created_at')

        return reports

    def set_closed(self, report_id):
        report = self.get_one(primary_key=report_id)
        report.is_closed = True
        report.save()
