from django.db import models

from .course_model import Course
from .educator_model import Educator
from .student_model import Student


class StudentCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    educator = models.ForeignKey(Educator, on_delete=models.CASCADE)
    study_time = models.PositiveSmallIntegerField()
    failures = models.PositiveSmallIntegerField()
    absences = models.PositiveSmallIntegerField()
    has_family_support = models.BooleanField()
    take_paid_class = models.BooleanField()
    midterm_grade = models.PositiveSmallIntegerField()
    final_grade = models.PositiveSmallIntegerField(null=True, blank=True)
    prediction_grade = models.PositiveSmallIntegerField(null=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
