from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .course_model import Course
from .educator_model import Educator
from .student_model import Student


class StudentCourse(models.Model):
    two_hours, two_to_five_hours, five_to_ten_hours, ten_hours = 1, 2, 3, 4

    study_time_choices = ((two_hours, '2 hours'),
                          (two_to_five_hours, '2 to 5 hours'),
                          (five_to_ten_hours, '5 to 10 hours'),
                          (ten_hours, '10 hours'))

    zero_to_hundred_range_validator = [MinValueValidator(0), MaxValueValidator(100)]

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    educator = models.ForeignKey(Educator, on_delete=models.CASCADE)
    study_time = models.PositiveSmallIntegerField(choices=study_time_choices)
    failures = models.PositiveSmallIntegerField(validators=[MinValueValidator(0),
                                                            MaxValueValidator(4)])
    absences = models.PositiveSmallIntegerField(validators=[MinValueValidator(0),
                                                            MaxValueValidator(93)])
    has_family_support = models.BooleanField()
    take_paid_class = models.BooleanField()
    midterm_grade = models.PositiveSmallIntegerField(validators=zero_to_hundred_range_validator)
    final_grade = models.PositiveSmallIntegerField(null=True, blank=True,
                                                   validators=zero_to_hundred_range_validator)
    prediction_grade = models.PositiveSmallIntegerField(null=True, editable=False,
                                                        validators=zero_to_hundred_range_validator)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return "{0}'s {1} ".format(self.student.name, self.course.name)
