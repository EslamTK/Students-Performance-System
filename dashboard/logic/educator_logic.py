from django.core.paginator import Paginator

from .unit_of_work import UnitOfWork
from .utilities import item_not_found_message


class EducatorLogic:

    def __init__(self):
        self.unit_of_work = UnitOfWork()

    def get_educator_info(self, educator_id):
        educator = self.unit_of_work.educators.get_one(educator_id)

        return educator

    def get_educator_accounts(self, educator_id):
        accounts = self.unit_of_work.educators_accounts.get_educator_accounts(educator_id)

        return accounts

    def get_educator_reviews_years(self, educator_id):
        years = self.unit_of_work.students_reviews.get_educator_reviews_years(educator=educator_id)

        return years

    def get_educator_reviews_departments(self, educator_id):
        departments = self.unit_of_work.students_reviews.get_educator_reviews_departments(educator=educator_id)

        return departments

    def get_educator_rating(self, educator_id, year=None, department_id=None):
        rating = self.unit_of_work.students_review_items. \
            get_educator_rating(educator=educator_id, year=year, department=department_id)

        return rating

    def get_educator_reviews(self, educator_id, page=1, page_size=6):
        reviews = self.unit_of_work.students_reviews.get_educator_reviews(educator_id)

        paginator = Paginator(reviews, page_size)

        reviews = paginator.get_page(page)

        return reviews, paginator.num_pages

    def get_educator_students(self, educator_id, keyword=None, page=1, page_size=2):
        students = self.unit_of_work.students_courses.get_educator_students(educator=educator_id, keyword=keyword)

        paginator = Paginator(students, page_size)

        students = paginator.get_page(page)

        return students, paginator.num_pages

    def get_educator_counts(self, educator_id, department_id=None, year_id=None, term_id=None):
        counts = self.unit_of_work.students_courses. \
            get_educator_students_counts(educator=educator_id, department=department_id, year=year_id,
                                         term=term_id)

        return counts

    def is_student_exist(self, student_id):
        return self.unit_of_work.students.is_exist(student_id)

    def is_educator_exist(self, educator_id):
        return self.unit_of_work.educators.is_exist(educator_id)

    def add_student_advice(self, student_id, educator_id, content):

        if not self.is_student_exist(student_id=student_id):
            raise ValueError(item_not_found_message('student'))

        self.unit_of_work.educators_advices. \
            add_student_advice(student=student_id, educator=educator_id, content=content)

    def add_review_report(self, review_id, educator_id):

        try:
            review = self.unit_of_work.students_reviews.get_one(review_id)

        except:
            raise ValueError(item_not_found_message('review'))

        if review.educator_id != educator_id:
            raise PermissionError('The specified review is not owned by the given educator')

        self.unit_of_work.reports.add_report(review_id=review_id)
