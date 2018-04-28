from django.db import models

from .utilities import get_path_with_time_now


class Account(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to=get_path_with_time_now)

    def __str__(self):
        return self.name
