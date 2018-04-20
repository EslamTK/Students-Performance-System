from .logic import Logic
from .utilities import get_paginated_result_and_num_pages


class EducatorLogic(Logic):

    def get_educator_info(self, educator_id):
        educator = self._unit_of_work.educators.get_one(educator_id)

        return educator

    def get_educator_accounts(self, educator_id):
        accounts = self._unit_of_work.educators_accounts.get_educator_accounts(educator_id)

        return accounts

    def get_educator_reviews_years(self, educator_id):
        years = self._unit_of_work.students_reviews.get_educator_reviews_years(educator=educator_id)

        return years

    def get_educator_reviews_departments(self, educator_id):
        departments = self._unit_of_work.students_reviews.get_educator_reviews_departments(educator=educator_id)

        return departments

    def get_educator_rating(self, educator_id, year=None, department_id=None):
        rating = self._unit_of_work.students_review_items. \
            get_educator_rating(educator=educator_id, year=year, department=department_id)

        return rating

    def get_educator_reviews(self, educator_id, page=1, page_size=4):
        reviews = self._unit_of_work.students_reviews.get_educator_reviews(educator_id)

        return get_paginated_result_and_num_pages(result=reviews, page_size=page_size, page=page)

    def get_educator_students(self, educator_id, keyword=None, page=1, page_size=6):
        students = self._unit_of_work.students_courses.get_educator_students(educator=educator_id, keyword=keyword)

        return get_paginated_result_and_num_pages(result=students, page_size=page_size, page=page)

    def get_educator_counts(self, educator_id, department_id=None, year_id=None, term_id=None):
        counts = self._unit_of_work.students_courses. \
            get_educator_students_counts(educator=educator_id, department=department_id, year=year_id,
                                         term=term_id)

        return counts

    def add_student_advice(self, student_id, educator_id, form):
        advice = form.save(commit=False)
        advice.student_id = student_id
        advice.educator_id = educator_id
        advice.save()

    def add_review_report(self, review_id, educator_id):
        review = self._unit_of_work.students_reviews.get_one(review_id)

        if review.educator_id != educator_id:
            raise ValueError()

        self._unit_of_work.reports.add_report(review_id=review_id)
