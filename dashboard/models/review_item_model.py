from django.db import models


class ReviewItem(models.Model):
    name = models.CharField(max_length=50)
