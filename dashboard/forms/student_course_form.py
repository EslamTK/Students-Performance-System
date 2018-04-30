from django import forms
from django.forms import modelformset_factory

from dashboard.models.student_course_model import StudentCourse


class StudentCourseForm(forms.ModelForm):
    class Meta:
        model = StudentCourse
        fields = ['course', 'study_time', 'failures', 'absences', 'has_family_support',
                  'take_paid_class', 'midterm_grade', 'final_grade']


class StudentCourseFormsetInitializer:

    def __init__(self, request_data, student_courses, available_courses):
        self.StudentCourseFormset = modelformset_factory(model=StudentCourseForm.Meta.model,
                                                         form=StudentCourseForm,
                                                         validate_max=True,
                                                         max_num=len(student_courses) + len(available_courses),
                                                         can_delete=True)

        self.courses_formset = self.StudentCourseFormset(request_data, queryset=student_courses)
