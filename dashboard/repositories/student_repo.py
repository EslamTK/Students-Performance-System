from dashboard.models import *
from .repo import Repo


class StudentRepo(Repo):
    def __init__(self):
        super().__init__(Student)
