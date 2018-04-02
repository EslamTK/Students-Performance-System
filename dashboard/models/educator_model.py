from django.conf import settings
from django.db import models


class Educator(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    image_url = models.CharField(max_length=200)
    about_me = models.TextField()
