from dashboard.models import *
from .repo import Repo


class TermRepo(Repo):
    def __init__(self):
        super().__init__(Term)
