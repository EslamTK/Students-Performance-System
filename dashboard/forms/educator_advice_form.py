from django import forms

from dashboard.models.educator_advice_model import EducatorAdvice


class EducatorAdviceForm(forms.ModelForm):
    class Meta:
        model = EducatorAdvice
        fields = ['content']
