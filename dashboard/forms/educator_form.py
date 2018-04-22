from django import forms
from django.forms import modelformset_factory

from dashboard.forms.educator_account_form import EducatorAccountForm
from dashboard.models.educator_model import Educator


class EducatorForm(forms.ModelForm):
    class Meta:
        model = Educator
        fields = ['photo', 'name', 'title', 'email', 'about_me']

    def __init__(self, *args, accounts, educator_accounts, educator_not_accounts, **kwargs):
        super().__init__(*args, **kwargs)

        self.accounts = accounts

        self.EducatorAccountFormset = modelformset_factory(model=EducatorAccountForm.Meta.model,
                                                           form=EducatorAccountForm,
                                                           extra=len(educator_not_accounts),
                                                           validate_max=True,
                                                           max_num=len(accounts),
                                                           can_delete=True)

        self.accounts_formset = self.EducatorAccountFormset(args[0],
                                                            form_kwargs={'accounts': accounts},
                                                            queryset=educator_accounts,
                                                            initial=educator_not_accounts)
