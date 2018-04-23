from django import forms

from dashboard.models.educator_advice_model import EducatorAdvice


class EducatorAdviceForm(forms.ModelForm):
    #content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'row':5}))
    class Meta:
        model = EducatorAdvice
        fields = ['content']
