from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.http import HttpResponseBadRequest, HttpResponse

from dashboard.controllers.administrator.base import AdministratorBaseView
from dashboard.logic import *


class AdministratorReviewActionsApi(AdministratorBaseView):

    def dispatch(self, request, *args, **kwargs):

        # Getting the review id
        review_id = request.POST.get('review_id')

        if not review_id:
            return HttpResponseBadRequest('The required review_id is not given')

        return super().dispatch(request, *args, review_id=review_id, **kwargs)

    def post(self, request, user_id, review_id):

        try:
            administrator.close_report(review_id=review_id)

        except (ObjectDoesNotExist, ValueError, IntegrityError):
            return HttpResponseBadRequest('The given review_id is not valid')

        return HttpResponse('The report closed successfully')

    def delete(self, request, user_id, review_id):

        try:
            administrator.delete_review(review_id=review_id)

        except (ObjectDoesNotExist, ValueError, IntegrityError):
            return HttpResponseBadRequest('The given review_id is not valid')

        return HttpResponse('The review removed successfully')
