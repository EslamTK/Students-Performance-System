from django.http import JsonResponse

from dashboard.controllers.educator.base import EducatorBaseView
from dashboard.logic import *


class EducatorStudentsCountsApi(EducatorBaseView):

    def get(self, request, user_id):
        # Getting the department
        department_id = request.GET.get('department_id')

        # Getting the year
        year_id = request.GET.get('year_id')

        # Getting the term
        term_id = request.GET.get('term_id')

        # Educator Courses Counts
        educator_counts = educator.get_educator_counts(educator_id=user_id,
                                                       department_id=department_id,
                                                       year_id=year_id, term_id=term_id)

        result = {
            'result': list(educator_counts)
        }

        return JsonResponse(result)
