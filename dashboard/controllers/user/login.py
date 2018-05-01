from django.contrib import auth
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render, redirect
from django.views import View

from dashboard.logic import *


class LoginView(View):
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        next_url = request.GET.get('next')
        return super().dispatch(request, *args, next_url=next_url, **kwargs)

    def get(self, request, next_url):

        if request.user.is_authenticated:
            return self.redirect_user(request.user)

        login_form = user_logic.get_login_form()

        return self.render_page(request, login_form, next_url)

    def post(self, request, next_url):

        login_form = user_logic.get_login_form(request.POST)

        if login_form.is_valid():
            login_user = login_form.get_user()
            auth.login(request, login_user)
            return self.redirect_user(login_user, next_url)

        return self.render_page(request, login_form, next_url)

    def render_page(self, request, login_form, next_url):

        result = {
            'login_form': login_form,
            'next_url': next_url
        }

        return render(request, self.template_name, result)

    @staticmethod
    def redirect_user(user, next_url=None):

        if next_url:
            return HttpResponseRedirect(next_url)

        user_group = user.groups.first()

        if user_group:
            home_page = general.get_home_page(user_group).url_name
            return redirect(to=home_page)
        else:
            return HttpResponseForbidden()
