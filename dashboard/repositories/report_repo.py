from dashboard.models import *
from .repo import Repo


class ReportRepo(Repo):
    def __init__(self):
        super().__init__(Report)
