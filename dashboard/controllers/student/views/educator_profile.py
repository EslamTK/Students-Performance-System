from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render

from dashboard.controllers.student.base import StudentBaseView
from dashboard.logic import *


class StudentEducatorProfileView(StudentBaseView):
    template_name = 'student/educator_profile.html'

    def get(self, request, user_id, educator_id):

        # Review Forms
        review_form = student.get_review_forms()

        return self.render_page(request, educator_id, review_form)

    def post(self, request, user_id, educator_id):

        review_form = student.get_review_forms(request.POST)

        if review_form.is_valid() and review_form.review_items.is_valid():

            try:
                student.add_review(student_id=user_id, educator_id=educator_id, review_form=review_form)

                return HttpResponseRedirect('')

            except (ObjectDoesNotExist, IntegrityError):

                return HttpResponseBadRequest()

        return self.render_page(request, educator_id, review_form)

    def render_page(self, request, educator_id, review_form):

        # Educator Info
        educator_info = educator.get_educator_info(educator_id)

        # Educator Accounts
        educator_accounts = educator.get_educator_accounts(educator_id)

        result = {
            'educator_info': educator_info,
            'educator_accounts': educator_accounts,
            'educator_id': educator_id,
            'review_form': review_form,
            'review_items_form': review_form.review_items
        }

        return render(request, self.template_name, result)
