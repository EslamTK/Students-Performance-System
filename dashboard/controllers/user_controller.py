from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST, require_http_methods

from dashboard.logic import *


@require_http_methods(['GET', 'POST'])
def login(request):
    next_url = request.GET.get('next')

    if request.user.is_authenticated:
        return redirect_user(request.user)

    if request.method == 'POST':

        login_form = user_logic.get_login_form(request.POST)

        if login_form.is_valid():
            login_user = login_form.get_user()
            auth.login(request, login_user)
            return redirect_user(login_user, next_url)

    else:
        login_form = user_logic.get_login_form()

    result = {
        'login_form': login_form,
        'next_url': next_url
    }

    return render(request, 'login.html', result)


@require_POST
def logout(request):
    auth.logout(request)

    return redirect(to='dashboard:user_login')


def redirect_user(user, next_url=None):
    if next_url:
        return HttpResponseRedirect(next_url)

    user_group = user.groups.all()[0].name

    if user_group == 'students':
        return redirect(to='dashboard:student_index')
    elif user_group == 'educators':
        return redirect(to='dashboard:educator_index')
    else:
        return redirect(to='dashboard:administrator_index')
