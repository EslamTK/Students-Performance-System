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
