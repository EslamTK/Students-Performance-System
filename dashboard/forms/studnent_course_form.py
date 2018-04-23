from django import forms

from dashboard.models.student_course_model import StudentCourse


class StudentCourseForm(forms.ModelForm):
    class Meta:
        model = StudentCourse
        fields = ['course', 'study_time', 'failures', 'absences', 'has_family_support',
                  'take_paid_class', 'midterm_grade', 'final_grade']
