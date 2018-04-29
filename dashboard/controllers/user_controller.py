from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_http_methods

from dashboard.logic import *


@require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return HttpResponse('Welcome {0} You Are Already Logged In'.format(request.user.id))

    if request.method == 'POST':
        login_form = user.get_login_form(request.POST)

        if login_form.is_valid():
            login_user = login_form.get_user()
            auth.login(request, login_user)
            return HttpResponse('Login Success')

    else:
        login_form = user.get_login_form()

    result = {
        'login_form': login_form
    }

    return render(request, 'login.html', result)


@require_GET
def logout(request):
    auth.logout(request)

    return redirect(to='dashboard:user_login')
