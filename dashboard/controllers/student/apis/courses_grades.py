from django.http import JsonResponse

from dashboard.controllers.student.base import StudentBaseView
from dashboard.logic import *


class StudentCoursesGradesApi(StudentBaseView):

    def get(self, request, user_id):
        # Getting the year
        year_id = request.GET.get('year_id')

        # Getting the term
        term_id = request.GET.get('term_id')

        # Student Courses Grades
        courses_grades = student.get_student_courses(student_id=user_id, is_current=False,
                                                     year=year_id, term=term_id)

        formatted_courses = []

        for i in courses_grades:
            course = {
                'id': i.course_id,
                'name': i.course.name,
                'midterm': i.midterm_grade,
                'final': i.final_grade
            }
            formatted_courses.append(course)

        result = {
            'result': formatted_courses,
        }

        return JsonResponse(result)
