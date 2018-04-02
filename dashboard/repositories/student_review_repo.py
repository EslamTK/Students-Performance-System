from dashboard.models import *
from .repo import Repo


class StudentReviewRepo(Repo):
    def __init__(self):
        super().__init__(StudentReview)
