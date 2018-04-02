from dashboard.models import *
from .repo import Repo


class EducatorRepo(Repo):
    def __init__(self):
        super().__init__(Educator)
