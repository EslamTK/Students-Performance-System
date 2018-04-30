from django.contrib.auth.forms import UserCreationForm

from dashboard.logic.administrator.educator import AdministratorEducatorLogic
from dashboard.logic.administrator.student import AdministratorStudentLogic


class AdministratorLogic(AdministratorStudentLogic, AdministratorEducatorLogic):

    @staticmethod
    def get_user_form(request_data=None):
        return UserCreationForm(request_data)
