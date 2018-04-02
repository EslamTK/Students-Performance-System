from django.db.models import Avg

from dashboard.models import *
from .repo import Repo


class StudentReviewItemRepo(Repo):
    def __init__(self):
        super().__init__(StudentReviewItem)

    def get_educator_rating(self, educator):
        reviews = StudentReview.objects.filter(educator=educator)

        rating = StudentReviewItem.objects.filter(student_review__in=reviews). \
            values('review_item').annotate(Avg('rate'))

        return rating
