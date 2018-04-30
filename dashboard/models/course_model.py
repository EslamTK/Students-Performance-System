from django.db import models

from .educator_model import Educator
from .term_model import Term
from .year_model import Year


class Course(models.Model):
    name = models.CharField(max_length=50)
    educator = models.ForeignKey(Educator, on_delete=models.CASCADE)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
