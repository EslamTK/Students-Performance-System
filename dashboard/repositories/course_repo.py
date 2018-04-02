from dashboard.models import *
from .repo import Repo


class CourseRepo(Repo):
    def __init__(self):
        super().__init__(Course)
