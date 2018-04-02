from dashboard.models import *
from .repo import Repo


class YearRepo(Repo):
    def __init__(self):
        super().__init__(Year)
