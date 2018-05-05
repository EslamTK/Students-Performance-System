from django.http import JsonResponse

from dashboard.controllers.administrator.base import AdministratorBaseView
from dashboard.logic import *


class AdministratorStudentsYearsPerformanceApi(AdministratorBaseView):

    def get(self, request, user_id):
        # Getting the department
        department_id = request.GET.get('department_id')

        # Getting the year
        year_id = request.GET.get('year_id')

        # Getting the term
        term_id = request.GET.get('term_id')

        # Years Success And Fail Counts
        years_counts = administrator.get_courses_pass_fail_counts(department_id=department_id,
                                                                  year_id=year_id, term_id=term_id)

        result = {
            'result': list(years_counts),
        }

        return JsonResponse(result)
