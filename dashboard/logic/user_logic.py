from django.contrib.auth.forms import AuthenticationForm

from .logic import Logic


class UserLogic(Logic):

    def get_login_form(self, request_data=None):
        return AuthenticationForm(data=request_data)
