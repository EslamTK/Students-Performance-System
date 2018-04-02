from dashboard.models import *
from .repo import Repo


class ReviewItemRepo(Repo):
    def __init__(self):
        super().__init__(ReviewItem)
