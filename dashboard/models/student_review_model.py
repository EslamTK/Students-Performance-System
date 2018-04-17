from django.db import models

from .educator_model import Educator
from .student_model import Student
from .year_model import Year


class StudentReview(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    educator = models.ForeignKey(Educator, on_delete=models.CASCADE)
    student_year = models.ForeignKey(Year, on_delete=models.CASCADE)
    content = models.TextField()
    is_anonymous = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
