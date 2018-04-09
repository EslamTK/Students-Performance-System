from dashboard.models import *
from .repo import Repo


class EducatorAccountRepo(Repo):
    def __init__(self):
        super().__init__(EducatorAccount)

    def get_educator_accounts(self, educator):
        return self._model.objects.filter(educator=educator).select_related('account')
