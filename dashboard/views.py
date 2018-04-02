from django.http import HttpResponse

from .models import *
from .repositories.account_repo import AccountRepo


def index(request):
    ac = Account(name='ccc', logo_url='sasasa')
    ac.save()
    account_repo = AccountRepo()
    return HttpResponse(str(account_repo.get_one(primary_key=1).name))
