from django.urls import path

from dashboard.controllers import student_controller, educator_controller, administrator_controller

app_name = 'dashboard'

urlpatterns = [
    path('student/', student_controller.index, name='student_index'),
    path('student/courses/', student_controller.student_courses, name='student_courses'),
    path('student/educator/<int:educator_id>/', student_controller.educator_profile, name='student_educator_profile'),
    path('educator/', educator_controller.index, name='educator_index'),
    path('educator/student/<int:student_id>/', educator_controller.student_profile, name='educator_student_profile'),
    path('educator/students/', educator_controller.educator_students, name='educator_students'),
    path('administrator/', administrator_controller.index, name='administrator_index'),
    path('administrator/student/<int:student_id>/', administrator_controller.student_profile,
         name='administrator_student_profile'),
    path('administrator/educators', administrator_controller.educators, name='administrator_educators'),
    path('administrator/educator/<int:educator_id>/', administrator_controller.educator_profile,
         name='administrator_educator_profile')
]
