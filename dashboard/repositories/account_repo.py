from django.db.models import Q

from dashboard.models import *
from .repo import Repo


class AccountRepo(Repo):
    def __init__(self):
        super().__init__(Account)

    def get_educator_accounts(self, educator):
        accounts = self._model.objects. \
            filter(Q(educatoraccount__isnull=True) | Q(educatoraccount__educator=educator)). \
            values('id', 'name', 'logo', 'educatoraccount__url')

        return accounts
