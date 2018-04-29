from django.contrib.auth.models import Group

from .repo import Repo


class GroupRepo(Repo):
    def __init__(self):
        super().__init__(Group)

    def get_group_by_name(self, name):
        group = self._model.objects.get(name=name)
        return group
