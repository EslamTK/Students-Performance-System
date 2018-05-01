from django.shortcuts import render

from dashboard.controllers.educator.base import EducatorBaseView, EducatorPaginatorBaseView
from dashboard.logic import *


class EducatorStudentsView(EducatorBaseView):
    template_name = 'educator/students.html'

    def get(self, request, user_id):
        # Educator Students
        students, students_num_pages = educator.get_educator_students(educator_id=user_id)

        # Departments
        departments = general.get_departments()

        # Years
        years = general.get_years()

        # Terms
        terms = general.get_terms()

        # Educator Students Pass & Fail Counts
        courses_counts = educator.get_educator_counts(educator_id=user_id)

        result = {
            'educator_students': students,
            'educator_students_num_pages': students_num_pages,
            'departments': departments,
            'years': years,
            'terms': terms,
            'courses_counts': courses_counts
        }

        return render(request, self.template_name, result)


class EducatorStudentsPaginatorView(EducatorPaginatorBaseView):
    template_name = 'educator/pagination/students.html'

    def get(self, request, user_id, page, page_size):
        # Getting the search keyword
        keyword = request.GET.get('keyword')

        # Educator Students
        students, students_num_pages = educator.get_educator_students(educator_id=user_id,
                                                                      keyword=keyword, page=page,
                                                                      page_size=page_size)

        result = {
            'educator_students': students,
            'educator_students_num_pages': students_num_pages,
        }

        return render(request, self.template_name, result)
