from django.db import models

from .account_model import Account
from .educator_model import Educator


class EducatorAccount(models.Model):
    educator = models.ForeignKey(Educator, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    url = models.URLField()

    class Meta:
        unique_together = ("educator", "account")

    def __str__(self):
        return "{0}'s {1}".format(self.educator.name, self.account.name)
