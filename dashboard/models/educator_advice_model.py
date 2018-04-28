from django.db import models

from .educator_model import Educator
from .student_model import Student


class EducatorAdvice(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    educator = models.ForeignKey(Educator, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0} advice for {1}".format(self.educator.name, self.student.name)
