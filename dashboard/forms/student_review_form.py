from django import forms
from django.forms import formset_factory

from dashboard.forms.student_review_item_form import StudentReviewItemForm
from dashboard.models.student_review_model import StudentReview


class StudentReviewForm(forms.ModelForm):

    class Meta:
        model = StudentReview
        fields = ['content', 'is_anonymous']

    def __init__(self, *args, review_items, **kwargs):
        super().__init__(*args, **kwargs)

        initial_data = [{'review_item': i.id, 'name': i.name} for i in review_items]

        self.ReviewItemsFormset = formset_factory(
            form=StudentReviewItemForm,
            extra=0,
            validate_min=True, validate_max=True,
            min_num=review_items.count(),
            max_num=review_items.count())

        self.review_items = self.ReviewItemsFormset(args[0], initial=initial_data)
