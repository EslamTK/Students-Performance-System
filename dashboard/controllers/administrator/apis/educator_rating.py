from django.http import JsonResponse

from dashboard.controllers.administrator.base import AdministratorBaseView
from dashboard.logic import *


class AdministratorEducatorRatingApi(AdministratorBaseView):

    def get(self, request, user_id, educator_id):
        # Getting the department
        department_id = request.GET.get('department_id')

        # Getting the year
        year = request.GET.get('year')

        # Educator Rating
        educator_rating = educator.get_educator_rating(educator_id=educator_id,
                                                       department_id=department_id,
                                                       year=year)

        result = {
            'result': list(educator_rating)
        }

        return JsonResponse(result)
