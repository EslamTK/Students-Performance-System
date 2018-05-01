from dashboard.repositories import *


class UnitOfWork:
    def __init__(self):
        self.accounts = AccountRepo()
        self.courses = CourseRepo()
        self.departments = DepartmentRepo()
        self.educators_accounts = EducatorAccountRepo()
        self.educators_advices = EducatorAdviceRepo()
        self.educators = EducatorRepo()
        self.reports = ReportRepo()
        self.review_items = ReviewItemRepo()
        self.students = StudentRepo()
        self.students_courses = StudentCourseRepo()
        self.students_reviews = StudentReviewRepo()
        self.students_review_items = StudentReviewItemRepo()
        self.term = TermRepo()
        self.year = YearRepo()
        self.groups = GroupRepo()
        self.home_pages = HomePageRepo()
