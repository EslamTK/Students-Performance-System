from .unit_of_work import UnitOfWork


class GeneralLogic:

    def __init__(self):
        self.unit_of_work = UnitOfWork()

    def get_review_items(self):
        return self.unit_of_work.review_items.get_all()

    def get_departments(self):
        return self.unit_of_work.departments.get_all()

    def get_years(self):
        return self.unit_of_work.year.get_all()

    def get_terms(self):
        return self.unit_of_work.term.get_all()
