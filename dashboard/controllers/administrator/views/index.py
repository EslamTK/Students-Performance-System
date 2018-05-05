from django.shortcuts import render

from dashboard.controllers.administrator.base import AdministratorBaseView, \
    AdministratorPaginatorBaseView
from dashboard.logic import *


class AdministratorIndexView(AdministratorBaseView):
    template_name = 'administrator/students/students_performance.html'

    def get(self, request, user_id):
        # Departments
        departments = general.get_departments()

        # Years
        years = general.get_years()

        # Terms
        terms = general.get_terms()

        # Years Success And Fail Counts
        years_counts = administrator.get_courses_pass_fail_counts()

        # Students
        students, students_num_pages = administrator.get_students()

        result = {
            'departments': departments,
            'years': years,
            'terms': terms,
            'years_counts': years_counts,
            'students': students,
            'students_num_pages': students_num_pages
        }

        return render(request, self.template_name, result)


class AdministratorStudentsPaginatorView(AdministratorPaginatorBaseView):
    template_name = 'administrator/students/pagination/students_performance.html'

    def get(self, request, user_id, page, page_size):
        # Getting the search keyword
        keyword = request.GET.get('keyword')

        # Students
        students, students_num_pages = administrator.get_students(keyword=keyword, page=page,
                                                                  page_size=page_size)

        result = {
            'students': students,
            'students_num_pages': students_num_pages
        }

        return render(request, self.template_name, result)
