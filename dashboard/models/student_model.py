from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from .department_model import Department
from .term_model import Term
from .year_model import Year


class Student(models.Model):
    male, female = 'M', 'F'
    gender_choices = ((male, 'Male'), (female, 'Female'))

    less_3, greater_3 = 'LE3', 'GT3'
    family_size_choices = ((less_3, 'Less or equal to 3'), (greater_3, 'Greater than 3'))

    together, apart = 'T', 'A'
    parent_status_choices = ((together, 'Living together'), (apart, 'Apart'))

    mother, father, other = 'mother', 'father', 'other'
    guardian_choices = ((mother, 'Mother'), (father, 'Father'), (other, 'Other'))

    teacher, health, services, at_home, other = 'teacher', 'health', 'services', 'at_home', 'other'
    job_choices = ((teacher, 'Teacher'), (health, 'Health Related'), (services, 'Services'),
                   (at_home, 'At Home'), (other, 'Other'))

    no_education, primary_education, preparatory_education, secondary_education, higher_education = \
        0, 1, 2, 3, 4

    education_choices = ((no_education, 'No Education'), (primary_education, 'Primary Education'),
                         (preparatory_education, 'Preparatory Education'),
                         (secondary_education, 'Secondary Education'),
                         (higher_education, 'Higher Education'))

    less_15_min, less_30_min, less_1_hour, equals_1_hour = 1, 2, 3, 4
    travel_time_choices = ((less_15_min, 'Less than 15 min'), (less_30_min, 'From 15 to 30 min'),
                           (less_1_hour, 'From 30 min to 1 hour'), (equals_1_hour, '1 hour'))

    one_to_five_range_validator = [MinValueValidator(1), MaxValueValidator(5)]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    year = models.ForeignKey(Year, on_delete=models.SET_NULL, null=True)
    term = models.ForeignKey(Term, on_delete=models.SET_NULL, null=True)
    department = models.ForeignKey(Department, on_delete=models.PROTECT)
    name = models.CharField(max_length=50, db_index=True)
    gender = models.CharField(max_length=1, choices=gender_choices)
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(3),
                                                       MaxValueValidator(100)])
    family_size = models.CharField(max_length=3, choices=family_size_choices)
    parent_status = models.CharField(max_length=1, choices=parent_status_choices)
    mother_education = models.PositiveSmallIntegerField(choices=education_choices)
    father_education = models.PositiveSmallIntegerField(choices=education_choices)
    guardian = models.CharField(max_length=10, choices=guardian_choices)
    mother_job = models.CharField(max_length=10, choices=job_choices)
    father_job = models.CharField(max_length=10, choices=job_choices)
    travel_time = models.PositiveSmallIntegerField(choices=travel_time_choices)
    do_extra_activity = models.BooleanField()
    wants_higher_education = models.BooleanField()
    has_internet = models.BooleanField()
    has_relationship = models.BooleanField()
    family_relation_quality = models.PositiveSmallIntegerField(validators=one_to_five_range_validator)
    free_time = models.PositiveSmallIntegerField(validators=one_to_five_range_validator)
    go_out_time = models.PositiveSmallIntegerField(validators=one_to_five_range_validator)
    health_status = models.PositiveSmallIntegerField(validators=one_to_five_range_validator)

    def __str__(self):
        return self.name
