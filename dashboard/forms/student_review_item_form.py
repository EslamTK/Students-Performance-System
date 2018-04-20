from django import forms

from dashboard.models.student_review_item_model import StudentReviewItem


class StudentReviewItemForm(forms.ModelForm):
    name = forms.CharField(widget=forms.HiddenInput)
    rate = forms.ChoiceField(choices=[(1, ''), (2, ''), (3, '')],
                             widget=forms.RadioSelect(attrs={"required": "required"}))

    class Meta:
        model = StudentReviewItem
        fields = ['review_item', 'rate']
        widgets = {'review_item': forms.HiddenInput}
