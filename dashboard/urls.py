from django.urls import path

from dashboard.controllers import student_controller, educator_controller, administrator_controller

app_name = 'dashboard'

urlpatterns = [
    path('student/',
         student_controller.index,
         name='student_index'),

    path('student_advices/',
         student_controller.get_student_advices,
         name='student_advices_paginator'),

    path('student/courses/',
         student_controller.student_courses,
         name='student_courses'),

    path('student_courses/',
         student_controller.get_student_courses,
         name='student_courses_paginator'),

    path('student/educator/<int:educator_id>/',
         student_controller.educator_profile,
         name='student_educator_profile'),

    path('educator/',
         educator_controller.index,
         name='educator_index'),

    path('educator_reviews',
         educator_controller.get_educator_reviews,
         name='educator_reviews_paginator'),

    path('educator/student/<int:student_id>/',
         educator_controller.student_profile,
         name='educator_student_profile'),

    path('educator/students/',
         educator_controller.educator_students,
         name='educator_students'),

    path('educator_students/',
         educator_controller.get_educator_students,
         name='educator_students_paginator'),

    path('administrator/',
         administrator_controller.index,
         name='administrator_index'),

    path('administrator/student/<int:student_id>/',
         administrator_controller.student_profile,
         name='administrator_student_profile'),

    path('administrator/educators',
         administrator_controller.educators,
         name='administrator_educators'),

    path('administrator/educator/<int:educator_id>/',
         administrator_controller.educator_profile,
         name='administrator_educator_profile')
]
