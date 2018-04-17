from django.core.paginator import Paginator

from dashboard.logic.student_logic import StudentLogic
from .unit_of_work import UnitOfWork


class AdministratorLogic:

    def __init__(self):
        self.unit_of_work = UnitOfWork()

    def get_students(self, keyword=None, page=1, page_size=6):
        students = self.unit_of_work.students.get_all(keyword=keyword)

        paginator = Paginator(students, page_size)

        students = paginator.get_page(page)

        return students, paginator.num_pages

    def get_educators(self, keyword=None, page=1, page_size=6):
        educators = self.unit_of_work.educators.get_all(keyword=keyword)

        paginator = Paginator(educators, page_size)

        educators = paginator.get_page(page)

        return educators, paginator.num_pages

    def get_educators_rating(self, department_id=None, year_id=None):
        rating = self.unit_of_work.students_review_items.get_educators_rating(department=department_id,
                                                                              year=year_id)

        return rating

    def get_educator_accounts(self, educator_id):
        accounts = self.unit_of_work.accounts.get_educator_accounts(educator=educator_id)

        return accounts

    def get_courses_pass_fail_counts(self, department_id=None, year_id=None, term_id=None):
        counts = self.unit_of_work.students_courses. \
            get_courses_success_fail_counts(department=department_id, year=year_id, term=term_id)

        return counts

    def get_available_student_courses(self, student_id):
        student_logic = StudentLogic()

        student = student_logic.get_student_data(student_id=student_id)

        courses = self.unit_of_work.courses.get_available_student_courses(student=student)

        return courses
