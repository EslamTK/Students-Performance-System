from dashboard.forms.student_course_form import StudentCourseFormsetInitializer
from dashboard.forms.student_form import StudentForm
from dashboard.logic.logic import Logic
from dashboard.logic.utilities import get_paginated_result_and_num_pages


class AdministratorStudentLogic(Logic):
    def __init__(self, student):
        super().__init__()
        self.student = student

    def get_courses_pass_fail_counts(self, department_id=None, year_id=None, term_id=None):
        counts = self._unit_of_work.students_courses. \
            get_courses_success_fail_counts(department=department_id, year=year_id, term=term_id)

        return counts

    def get_students(self, keyword=None, page=1, page_size=6):
        students = self._unit_of_work.students.get_all(keyword=keyword)

        return get_paginated_result_and_num_pages(result=students, page_size=page_size, page=page)

    def get_available_student_courses(self, student_id):
        student = self.student.get_student_data(student_id=student_id)

        courses = self._unit_of_work.courses.get_available_student_courses(student=student)

        return courses

    def get_student_form(self, student_id=None, request_data=None):

        student = None

        if student_id:
            student = self._unit_of_work.students.get_one(student_id)

        student_form = StudentForm(request_data, instance=student)

        return student_form

    @staticmethod
    def update_student(student_form):
        student_form.save()

    def add_student(self, user_form, student_form):

        user = user_form.save()

        student = student_form.save(commit=False)
        student.user_id = user.id
        student.save()

        students_group = self._unit_of_work.groups.get_group_by_name('students')
        user.groups.add(students_group)

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

    @staticmethod
    def update_student_courses(course_formset, student_id):

        instances = course_formset.save(commit=False)

        for instance in instances:
            if instance.student_id is None:
                instance.student_id = student_id
                instance.educator_id = instance.course.educator_id
            instance.save()

        for instance in course_formset.deleted_objects:
            instance.delete()
