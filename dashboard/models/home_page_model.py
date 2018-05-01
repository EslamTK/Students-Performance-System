from django.contrib.auth.models import Group
from django.db import models


class HomePage(models.Model):
    group = models.OneToOneField(Group, on_delete=models.CASCADE, primary_key=True)
    url_name = models.CharField(max_length=100)
