from django.conf import settings
from django.db import models

from .department_model import Department
from .year_model import Year


class Student(models.Model):
    male, female = 'M', 'F'
    sex_choices = ((male, 'Male'), (female, 'Female'))

    less_3, greater_3 = 'LE3', 'GT3'
    family_size_choices = ((less_3, 'Less or equal to 3'), (greater_3, 'Greater than 3'))

    together, apart = 'T', 'A'
    parent_status_choices = ((together, 'Living together'), (apart, 'Apart'))

    mother, father, other = 'mother', 'father', 'other'
    guardian_choices = ((mother, 'Mother'), (father, 'Father'), (other, 'Other'))

    teacher, health, services, at_home, other = 'teacher', 'health', 'services', 'at_home', 'other'
    job_choices = ((teacher, 'Teacher'), (health, 'Health Related'), (services, 'Services'),
                   (at_home, 'At Home'), (other, 'Other'))

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    sex = models.CharField(max_length=1, choices=sex_choices)
    age = models.SmallIntegerField()
    family_size = models.CharField(max_length=3, choices=family_size_choices)
    parent_status = models.CharField(max_length=1, choices=parent_status_choices)
    mother_education = models.SmallIntegerField()
    father_education = models.SmallIntegerField()
    guardian = models.CharField(max_length=10, choices=guardian_choices)
    mother_job = models.CharField(max_length=10, choices=job_choices)
    father_job = models.CharField(max_length=10, choices=job_choices)
    travel_time = models.SmallIntegerField()
    do_extra_activity = models.BooleanField()
    wants_higher_education = models.BooleanField()
    has_internet = models.BooleanField()
    has_relationship = models.BooleanField()
    family_relation_quality = models.SmallIntegerField()
    free_time = models.SmallIntegerField()
    go_out_time = models.SmallIntegerField()
    health_status = models.SmallIntegerField()
