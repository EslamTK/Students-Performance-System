from .unit_of_work import UnitOfWork

unit_of_work = UnitOfWork()


def get_educator_info(educator_id):
    educator = unit_of_work.educators.get_one(educator_id)

    return educator


def get_educator_accounts(educator_id):
    accounts = unit_of_work.educators_accounts.get_educator_accounts(educator_id)

    return accounts


def get_educator_reviews_years(educator_id):
    years = unit_of_work.students_reviews.get_educator_reviews_years(educator=educator_id)

    return years


def get_educator_reviews_departments(educator_id):
    departments = unit_of_work.students_reviews.get_educator_reviews_departments(educator=educator_id)

    return departments


def get_educator_rating(educator_id, year=None, department=None):
    rating = unit_of_work.students_review_items. \
        get_educator_rating(educator=educator_id, year=year, department=department)

    return rating


def get_educator_reviews(educator_id):
    reviews = unit_of_work.students_reviews.get_educator_reviews(educator_id)

    return reviews


def get_educator_students(educator_id):
    students = unit_of_work.students_courses.get_educator_students(educator=educator_id)

    return students


def get_educator_counts(educator_id, department=None, year=None, term=None):
    counts = unit_of_work.students_courses. \
        get_educator_students_counts(educator=educator_id, department=department, year=year, term=term)

    return counts
