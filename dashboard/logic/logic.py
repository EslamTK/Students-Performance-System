from .unit_of_work import UnitOfWork


class Logic:
    def __init__(self):
        self._unit_of_work = UnitOfWork()
