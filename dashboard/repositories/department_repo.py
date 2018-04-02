from dashboard.models import *
from .repo import Repo


class DepartmentRepo(Repo):
    def __init__(self):
        super().__init__(Department)
