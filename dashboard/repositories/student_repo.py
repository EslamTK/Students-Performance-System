from dashboard.models import *
from .repo import Repo


class StudentRepo(Repo):
    def __init__(self):
        super().__init__(Student)

    def get_all(self, keyword=None):
        filters = {}

        if keyword:
            filters['name__icontains'] = keyword

        return self._model.objects.filter(**filters) \
            .values('user_id', 'name', 'department', 'department__name', 'year', 'year__name') \
            .order_by('name')
