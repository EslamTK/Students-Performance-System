from django.db import models

from .educator_model import Educator
from .student_model import Student
from .year_model import Year


class StudentReview(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    educator = models.ForeignKey(Educator, on_delete=models.CASCADE)
    student_year = models.ForeignKey(Year, on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    is_anonymous = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0} review for {1}".format(self.student.name, self.educator.name)
