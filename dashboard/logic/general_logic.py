from .unit_of_work import UnitOfWork

unit_of_work = UnitOfWork()


def get_review_items():
    return unit_of_work.review_items.get_all()


def get_departments():
    return unit_of_work.departments.get_all()


def get_years():
    return unit_of_work.year.get_all()


def get_terms():
    return unit_of_work.term.get_all()
