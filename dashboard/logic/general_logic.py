from .logic import Logic


class GeneralLogic(Logic):

    def get_review_items(self):
        return self._unit_of_work.review_items.get_all()

    def get_departments(self):
        return self._unit_of_work.departments.get_all()

    def get_years(self):
        return self._unit_of_work.year.get_all()

    def get_terms(self):
        return self._unit_of_work.term.get_all()

    def get_home_page(self, group_id):
        return self._unit_of_work.home_pages.get_one(primary_key=group_id)
