from dashboard.models import *
from .repo import Repo


class StudentReviewRepo(Repo):
    def __init__(self):
        super().__init__(StudentReview)

    def get_educator_reviews(self, educator):
        reviews = self._model.objects.filter(educator=educator) \
            .values('student_id', 'student__name', 'id', 'content', 'created_at',
                    'is_anonymous', 'report__is_closed') \
            .order_by('-created_at')

        return reviews

    def get_educator_reviews_years(self, educator):
        years = self._model.objects.filter(educator=educator) \
            .extra(select={'year': "EXTRACT(year FROM created_at)"}) \
            .values('year').order_by('-year').distinct()

        return years

    def get_educator_reviews_departments(self, educator):
        departments = self._model.objects.filter(educator=educator) \
            .values('student__department', 'student__department__name') \
            .order_by('-student__department').distinct()

        return departments
