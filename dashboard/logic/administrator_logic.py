from django.contrib.auth.forms import UserCreationForm

from dashboard.forms.educator_form import EducatorForm
from dashboard.forms.student_course_form import StudentCourseFormsetInitializer
from dashboard.forms.student_form import StudentForm
from .logic import Logic
from .utilities import get_paginated_result_and_num_pages


class AdministratorLogic(Logic):

    def __init__(self, student):
        super().__init__()
        self.student = student

    def get_students(self, keyword=None, page=1, page_size=6):
        students = self._unit_of_work.students.get_all(keyword=keyword)

        return get_paginated_result_and_num_pages(result=students, page_size=page_size, page=page)

    def get_educators(self, keyword=None, page=1, page_size=6):
        educators = self._unit_of_work.educators.get_all(keyword=keyword)

        return get_paginated_result_and_num_pages(result=educators, page_size=page_size, page=page)

    def get_educators_rating(self, department_id=None, year_id=None):
        rating = self._unit_of_work.students_review_items.get_educators_rating(department=department_id,
                                                                               year=year_id)

        return rating

    def get_educator_accounts(self, educator_id):
        accounts = self._unit_of_work.accounts.get_educator_accounts(educator=educator_id)

        return accounts

    def get_courses_pass_fail_counts(self, department_id=None, year_id=None, term_id=None):
        counts = self._unit_of_work.students_courses. \
            get_courses_success_fail_counts(department=department_id, year=year_id, term=term_id)

        return counts

    def get_available_student_courses(self, student_id):
        student = self.student.get_student_data(student_id=student_id)

        courses = self._unit_of_work.courses.get_available_student_courses(student=student)

        return courses

    def get_user_form(self, request_data=None):
        return UserCreationForm(request_data)

    def get_educator_form(self, educator_id=None, request_data=None, request_files=None):

        educator, educator_accounts = None, self._unit_of_work.educators_accounts.get_none()

        if educator_id:
            educator = self._unit_of_work.educators.get_one(educator_id)

            educator_accounts = self._unit_of_work.educators_accounts. \
                get_educator_accounts(educator=educator_id)

        accounts = self._unit_of_work.accounts.get_all()

        educator_not_accounts = []

        accounts_dict = {}

        for account in accounts:
            educator_has_account = False
            for educator_account in educator_accounts:
                if account == educator_account.account:
                    educator_has_account = True
                    break
            accounts_dict[account.id] = {
                'name': account.name,
                'logo': account.logo
            }

            if not educator_has_account:
                educator_not_accounts.append({'account': account.id})

        educator_form = EducatorForm(request_data, request_files,
                                     instance=educator, accounts=accounts_dict,
                                     educator_accounts=educator_accounts,
                                     educator_not_accounts=educator_not_accounts)

        return educator_form

    def update_educator(self, educator_id, educator_form, accounts_formset):

        educator_form.save()

        instances = accounts_formset.save(commit=False)

        for instance in instances:
            instance.educator_id = educator_id
            instance.save()

        for instance in accounts_formset.deleted_objects:
            instance.delete()

    def add_educator(self, user_form, educator_form, accounts_formset):

        user = user_form.save()

        educator = educator_form.save(commit=False)
        educator.user_id = user.id
        educator.save()

        instances = accounts_formset.save(commit=False)

        for instance in instances:
            instance.educator_id = user.id
            instance.save()

    def get_student_form(self, student_id=None, request_data=None):

        student = None

        if student_id:
            student = self._unit_of_work.students.get_one(student_id)

        student_form = StudentForm(request_data, instance=student)

        return student_form

    def update_student(self, student_form):
        student_form.save()

    def add_student(self, user_form, student_form):

        user = user_form.save()

        student = student_form.save(commit=False)
        student.user_id = user.id
        student.save()

        return user.id

    def get_student_courses_formset(self, student_id=None, request_data=None):

        student_courses, available_courses = self._unit_of_work.students_courses.get_none(), None

        if student_id:

            student_courses = self._unit_of_work.students_courses. \
                get_student_courses(student=student_id)

            available_courses = self._unit_of_work.courses. \
                get_available_student_courses(student=student_id)

        course_formset_initialize = StudentCourseFormsetInitializer(request_data=request_data,
                                                                    student_courses=student_courses,
                                                                    available_courses=available_courses)

        return course_formset_initialize.courses_formset

    def update_student_courses(self, course_formset, student_id):

        instances = course_formset.save(commit=False)

        for instance in instances:
            if instance.student_id is None:
                instance.student_id = student_id
                instance.educator_id = instance.course.educator_id
            instance.save()

        for instance in course_formset.deleted_objects:
            instance.delete()

    def get_reports(self, educator_id=None, is_closed=False):
        reports = self._unit_of_work.reports.get_all(educator=educator_id,
                                                     is_closed=is_closed)

        return reports

    def close_report(self, report_id):
        self._unit_of_work.reports.set_closed(report_id=report_id)

    def delete_review(self, review_id):
        self._unit_of_work.students_reviews.delete(primary_key=review_id)
