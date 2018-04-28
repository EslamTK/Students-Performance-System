from django.db import models

from .review_item_model import ReviewItem
from .student_review_model import StudentReview


class StudentReviewItem(models.Model):
    student_review = models.ForeignKey(StudentReview, on_delete=models.CASCADE)
    review_item = models.ForeignKey(ReviewItem, on_delete=models.CASCADE)
    rate = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = ("student_review", "review_item")

    def __str__(self):
        return "{0}'s rate {1} ".format(self.review_item.name, self.rate)
