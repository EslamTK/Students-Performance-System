from dashboard.models import *
from .repo import Repo


class StudentRepo(Repo):
    def __init__(self):
        super().__init__(Student)

    def get_all(self):
        return self._model.objects. \
            values('user_id', 'name', 'department', 'department__name', 'year', 'year__name')
