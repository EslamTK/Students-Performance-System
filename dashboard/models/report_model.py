from django.db import models
from django.utils import timezone

from .student_review_model import StudentReview


class Report(models.Model):
    student_review = models.OneToOneField(StudentReview, on_delete=models.CASCADE, primary_key=True)
    is_closed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return "{0} review".format(self.student_review.student.name)
