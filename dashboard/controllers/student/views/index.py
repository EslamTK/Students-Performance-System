from django.shortcuts import render

from dashboard.controllers.student.base import StudentBaseView, StudentPaginatorBaseView
from dashboard.logic import *


class StudentIndexView(StudentBaseView):
    template_name = 'student/index.html'

    def get(self, request, user_id):
        # Student Year and Term
        student_info = student.get_student_year_and_term(student_id=user_id)

        # Student Advices
        student_advices, student_advices_num_pages = student.get_student_advices(student_id=user_id)

        # Student Courses Predictions
        predictions = student.get_student_predictions(student_id=user_id)

        # Student Recommendations
        recommendations = student.get_student_recommendations(student_id=user_id)

        result = {
            'student_info': student_info,
            'student_advices': student_advices,
            'student_advices_num_pages': student_advices_num_pages,
            'student_predictions': predictions,
            'student_recommendations': recommendations
        }

        return render(request, self.template_name, result)


class StudentAdvicesPaginatorView(StudentPaginatorBaseView):
    template_name = 'student/pagination/index.html'

    def get(self, request, user_id, page, page_size):
        student_advices, student_advices_num_pages = student.get_student_advices(student_id=user_id,
                                                                                 page=page,
                                                                                 page_size=page_size)

        result = {
            'student_advices': student_advices,
            'student_advices_num_pages': student_advices_num_pages
        }

        return render(request, self.template_name, result)
