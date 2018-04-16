from django.db.models import Count, Q

from dashboard.models import *
from .repo import Repo


class EducatorRepo(Repo):
    def __init__(self):
        super().__init__(Educator)

    def get_all(self, keyword=None):
        filters = {}

        if keyword:
            filters['name__icontains'] = keyword

        educators = self._model.objects.filter(**filters) \
            .values('user_id', 'name') \
            .annotate(courses=Count('course', distinct=True),
                      students=Count('course__studentcourse',
                                     filter=Q(course__studentcourse__final_grade__isnull=True)),
                      prediction_fail=Count('course__studentcourse',
                                            filter=Q(course__studentcourse__prediction_grade__lt=50,
                                                     course__studentcourse__final_grade__isnull=True))) \
            .order_by('name')

        return educators
