from django.db import IntegrityError
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render

from dashboard.controllers.educator.base import EducatorBaseView, EducatorPaginatorBaseView
from dashboard.forms.educator_advice_form import EducatorAdviceForm
from dashboard.logic import *


class EducatorStudentProfileView(EducatorBaseView):
    template_name = 'educator/student_profile.html'

    def get(self, request, user_id, student_id):

        advice_form = EducatorAdviceForm()

        return self.render_page(request, student_id, advice_form)

    def post(self, request, user_id, student_id):

        advice_form = EducatorAdviceForm(request.POST)

        if advice_form.is_valid():

            try:
                educator.add_student_advice(student_id=student_id, educator_id=user_id,
                                            form=advice_form)

                return HttpResponseRedirect('')

            except IntegrityError:
                return HttpResponseBadRequest()

        return self.render_page(request, student_id, advice_form)

    def render_page(self, request, student_id, advice_form):

        # Student Current Courses Predictions
        predictions = student.get_student_predictions(student_id=student_id)

        # Years
        years = general.get_years()

        # Terms
        terms = general.get_terms()

        # Student Advices
        student_advices, student_advices_num_pages = student.get_student_advices(student_id=student_id)

        result = {
            'student_predictions': predictions,
            'years': years,
            'terms': terms,
            'student_id': student_id,
            'advice_form': advice_form,
            'student_advices': student_advices,
            'student_advices_num_pages': student_advices_num_pages
        }

        return render(request, self.template_name, result)


class EducatorStudentAdvicesPaginatorView(EducatorPaginatorBaseView):
    template_name = 'educator/pagination/student_profile.html'

    def get(self, request, user_id, page, page_size, student_id):
        student_advices, student_advices_num_pages = student.get_student_advices(student_id=student_id,
                                                                                 page=page,
                                                                                 page_size=page_size)

        result = {
            'student_advices': student_advices,
            'student_advices_num_pages': student_advices_num_pages
        }

        return render(request, self.template_name, result)
