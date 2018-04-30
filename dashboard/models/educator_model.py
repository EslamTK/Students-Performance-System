from django.conf import settings
from django.db import models

from .utilities import get_path_with_time_now


class Educator(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=50, db_index=True)
    title = models.CharField(max_length=50)
    email = models.EmailField()
    photo = models.ImageField(upload_to=get_path_with_time_now)
    about_me = models.TextField()

    def __str__(self):
        return self.name
