from django.urls import path

from dashboard.controllers import student_controller

urlpatterns = [
    path('student', student_controller.index, name='index'),
    path('student/courses', student_controller.student_courses, name='student_courses'),
    path('student/educator/<int:educator_id>/', student_controller.educator_profile, name='educator_profile')
]
