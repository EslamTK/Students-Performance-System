from dashboard.models import *
from .repo import Repo


class AccountRepo(Repo):
    def __init__(self):
        super().__init__(Account)
