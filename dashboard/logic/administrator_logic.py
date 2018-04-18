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
