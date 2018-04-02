from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=50)
    logo_url = models.CharField(max_length=200)
