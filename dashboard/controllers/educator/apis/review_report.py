from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.http import HttpResponseBadRequest, HttpResponse

from dashboard.controllers.educator.base import EducatorBaseView
from dashboard.logic import *


class EducatorReportApi(EducatorBaseView):

    def post(self, request, user_id):

        # Getting the review id
        review_id = request.POST.get('review_id')

        if not review_id:
            return HttpResponseBadRequest('The required review_id is not given')

        try:
            educator.add_review_report(educator_id=user_id, review_id=review_id)

        except (ObjectDoesNotExist, ValueError, IntegrityError):
            return HttpResponseBadRequest('The given review_id is not valid')

        return HttpResponse('The review report added successfully')
