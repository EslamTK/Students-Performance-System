from django import forms

from dashboard.models.educator_account_model import EducatorAccount


class EducatorAccountForm(forms.ModelForm):
    class Meta:
        model = EducatorAccount
        fields = ['account', 'url']
        widgets = {'account': forms.HiddenInput}
