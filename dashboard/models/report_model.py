from django.db import models

from .student_review_model import StudentReview


class Report(models.Model):
    student_review = models.OneToOneField(StudentReview, on_delete=models.CASCADE, primary_key=True)
