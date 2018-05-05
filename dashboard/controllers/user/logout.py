from django.contrib import auth
from django.shortcuts import redirect
from django.views import View


class LogoutView(View):
    login_url_name = 'dashboard:user_login'

    def post(self, request):
        auth.logout(request)
        return redirect(to=self.login_url_name)
