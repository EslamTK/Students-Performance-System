from django.db import models

from .course_model import Course
from .educator_model import Educator
from .student_model import Student


class StudentCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    educator = models.ForeignKey(Educator, on_delete=models.CASCADE)
    study_time = models.SmallIntegerField()
    failures = models.SmallIntegerField()
    absences = models.SmallIntegerField()
    has_family_support = models.BooleanField()
    take_paid_class = models.BooleanField()
    midterm_grade = models.SmallIntegerField()
    final_grade = models.SmallIntegerField(null=True, blank=True)
