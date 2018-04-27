from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.http import JsonResponse, HttpResponse, \
    HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.decorators.http import require_GET, require_POST, require_http_methods

from dashboard.forms.educator_advice_form import EducatorAdviceForm
from dashboard.logic import *

def login(request):
    return render(request, 'login.html')