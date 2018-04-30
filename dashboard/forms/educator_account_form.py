from django import forms

from dashboard.models.educator_account_model import EducatorAccount


class EducatorAccountForm(forms.ModelForm):
    logo_url = forms.CharField(widget=forms.HiddenInput)

    class Meta:
        model = EducatorAccount
        fields = ['account', 'url']
        widgets = {'account': forms.HiddenInput}

    def __init__(self, *args, accounts, **kwargs):

        super().__init__(*args, **kwargs)

        if kwargs.get('instance'):
            self.fields['logo_url'].initial = accounts[kwargs.get('instance').account_id]['logo'].url
        elif kwargs.get('initial'):
            self.fields['logo_url'].initial = accounts[kwargs.get('initial')['account']]['logo'].url
