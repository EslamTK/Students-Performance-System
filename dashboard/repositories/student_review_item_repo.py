from django.db.models import Avg

from dashboard.models import *
from .repo import Repo


class StudentReviewItemRepo(Repo):
    def __init__(self):
        super().__init__(StudentReviewItem)

    def get_educator_rating(self, educator, year=None, department=None):

        filters = {
            'student_review__educator': educator
        }

        if year:
            filters['student_review__created_at__year'] = year

        if department:
            filters['student_review__student__department'] = department

        rating = self._model.objects.filter(**filters). \
            values('review_item__id', 'review_item__name').annotate(Avg('rate')).order_by('review_item__name')

        return rating

    def get_educators_rating(self, department=None):

        rating = self._model.objects \
            .extra(select={'year': "EXTRACT(year FROM dashboard_studentreview.created_at)"},
                   tables=['dashboard_studentreview']) \
            .values('review_item', 'review_item__name', 'year').annotate(Avg('rate'))

        if department:
            rating = rating.filter(student_review__student__department=department)

        return rating
