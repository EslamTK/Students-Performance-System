from dashboard.models import *
from .repo import Repo


class HomePageRepo(Repo):
    def __init__(self):
        super().__init__(HomePage)
