from django.db import models

from .account_model import Account
from .educator_model import Educator


class EducatorAccount(models.Model):
    educator = models.ForeignKey(Educator, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    url = models.CharField(max_length=200)

    class Meta:
        unique_together = ("educator", "account")
