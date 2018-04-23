from django import forms
from django.forms import modelformset_factory

from dashboard.forms.studnent_course_form import StudentCourseForm
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

    def __init__(self, *args, student_courses, available_courses, **kwargs):
        super().__init__(*args, **kwargs)

        self.available_courses = available_courses

        self.StudentCourseFormset = modelformset_factory(model=StudentCourseForm.Meta.model,
                                                         form=StudentCourseForm,
                                                         validate_max=True,
                                                         max_num=len(student_courses) + len(available_courses),
                                                         can_delete=True)

        self.courses_formset = self.StudentCourseFormset(args[0], queryset=student_courses)
