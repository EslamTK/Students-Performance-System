from dashboard.logic.student_logic import StudentLogic
from .unit_of_work import UnitOfWork


class AdministratorLogic:

    def __init__(self):
        self.unit_of_work = UnitOfWork()

    def get_students(self):
        students = self.unit_of_work.students.get_all()

        return students

    def get_educators(self):
        educators = self.unit_of_work.educators.get_all()

        return educators

    def get_educators_rating(self, department=None):
        rating = self.unit_of_work.students_review_items.get_educators_rating(department=department)

        return rating

    def get_educator_accounts(self, educator_id):
        accounts = self.unit_of_work.accounts.get_educator_accounts(educator=educator_id)

        return accounts

    def get_courses_pass_fail_counts(self, department=None, term=None):
        counts = self.unit_of_work.students_courses. \
            get_courses_success_fail_counts(department=department, term=term)

        return counts

    def get_available_student_courses(self, student_id):
        student_logic = StudentLogic()

        student = student_logic.get_student_data(student_id=student_id)

        courses = self.unit_of_work.courses.get_available_student_courses(student=student)

        return courses
