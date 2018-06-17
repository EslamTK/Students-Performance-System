from django.shortcuts import render, redirect

from dashboard.controllers.administrator.base import AdministratorBaseView
from dashboard.logic import *


class AdministratorStudentProfileView(AdministratorBaseView):
    template_name = 'administrator/students/student_profile.html'
    form_template_name = 'administrator/students/forms/add_student.html'

    def get(self, request, user_id, student_id=None):

        # User Form
        user_form = None

        # Student Form
        student_form = administrator.get_student_form(student_id=student_id)

        # Courses Formset
        courses_formset = None

        if student_id:
            courses_formset = administrator.get_student_courses_formset(student_id=student_id)
        else:
            user_form = administrator.get_user_form()

        result = {
            'student_id': student_id,
            'student_form': student_form,
            'user_form': user_form,
            'courses_formset': courses_formset
        }

        return render(request, self.template_name, result)

    def post(self, request, user_id, student_id=None):

        template_to_render = self.template_name

        user_form = None

        student_form = administrator.get_student_form(request_data=request.POST,
                                                      student_id=student_id)
        if student_id:

            if student_form.is_valid():
                administrator.update_student(student_form)

            template_to_render = self.form_template_name

        else:

            user_form = administrator.get_user_form(request_data=request.POST)

            if user_form.is_valid() and student_form.is_valid():
                student_id = administrator.add_student(user_form, student_form)

                return redirect(to='dashboard:administrator_student_update',
                                student_id=student_id)

        result = {
            'student_id': student_id,
            'student_form': student_form,
            'user_form': user_form
        }

        return render(request, template_to_render, result)


class AdministratorStudentCoursesView(AdministratorBaseView):
    form_template_name = 'administrator/students/forms/courses_form.html'

    def post(self, request, user_id, student_id):
        courses_formset = administrator. \
            get_student_courses_formset(request_data=request.POST, student_id=student_id)

        if courses_formset.is_valid():
            administrator.update_student_courses(course_formset=courses_formset,
                                                 student_id=student_id)

            courses_formset = administrator.get_student_courses_formset(student_id=student_id)

        result = {
            'student_id': student_id,
            'courses_formset': courses_formset
        }

        return render(request, self.form_template_name, result)
