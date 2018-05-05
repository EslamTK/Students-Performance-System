from django.http import JsonResponse

from dashboard.controllers.administrator.base import AdministratorBaseView
from dashboard.logic import *


class AdministratorEducatorsRatingApi(AdministratorBaseView):

    def get(self, request, user_id):
        # Getting the department
        department_id = request.GET.get('department_id')

        # Getting the year
        year_id = request.GET.get('year_id')

        # Educators Rating
        educators_rating = administrator.get_educators_rating(department_id=department_id,
                                                              year_id=year_id)
        result = {
            'result': list(educators_rating),
        }

        return JsonResponse(result)
