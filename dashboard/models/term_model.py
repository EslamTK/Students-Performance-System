from django.db import models


class Term(models.Model):
    name = models.CharField(max_length=50)
