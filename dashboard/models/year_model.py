from django.db import models


class Year(models.Model):
    name = models.CharField(max_length=50)
