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

        rating = StudentReviewItem.objects.select_related('review_item').filter(**filters). \
            values('review_item__id', 'review_item__name').annotate(Avg('rate')).order_by('review_item__name')

        return rating
