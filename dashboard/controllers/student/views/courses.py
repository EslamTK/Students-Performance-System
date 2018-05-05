from django.shortcuts import render

from dashboard.controllers.student.base import StudentBaseView, StudentPaginatorBaseView
from dashboard.logic import *


class StudentCoursesView(StudentBaseView):
    template_name = 'student/courses.html'

    def get(self, request, user_id):
        # Student Current Courses Predictions
        predictions = student.get_student_predictions(student_id=user_id)

        # Years
        years = general.get_years()

        # Terms
        terms = general.get_terms()

        # Student Courses
        courses, courses_num_pages = student.get_student_courses(student_id=user_id, is_all=True)

        result = {
            'student_predictions': predictions,
            'years': years,
            'terms': terms,
            'student_courses': courses,
            'student_courses_num_pages': courses_num_pages
        }

        return render(request, self.template_name, result)


class StudentCoursesPaginatorView(StudentPaginatorBaseView):
    template_name = 'student/pagination/courses.html'

    def get(self, request, user_id, page, page_size):
        # Getting the search keyword
        keyword = request.GET.get('keyword')

        # Student Courses
        courses, courses_num_pages = student.get_student_courses(student_id=user_id, is_all=True,
                                                                 keyword=keyword,
                                                                 page=page, page_size=page_size)

        result = {
            'student_courses': courses,
            'student_courses_num_pages': courses_num_pages
        }

        return render(request, self.template_name, result)
