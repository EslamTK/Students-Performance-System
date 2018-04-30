from django import forms

from dashboard.models.student_model import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'gender', 'age', 'department', 'year', 'term',
                  'guardian', 'family_size', 'parent_status', 'family_relation_quality',
                  'mother_job', 'father_job', 'mother_education', 'father_education',
                  'travel_time', 'free_time', 'go_out_time', 'health_status',
                  'do_extra_activity', 'wants_higher_education', 'has_internet',
                  'has_relationship']
