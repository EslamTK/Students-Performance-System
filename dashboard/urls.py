from django.urls import path

# from dashboard.controllers import forms_testing
from dashboard.controllers import student_controller, \
    educator_controller, administrator_controller
from dashboard.controllers.user import login, logout

app_name = 'dashboard'

urlpatterns = [

    # path('form/',
    #      forms_testing.index,
    #      name='form'),

    path('login/',
         login.LoginView.as_view(),
         name='user_login'),

    path('logout/',
         logout.LogoutView.as_view(),
         name='user_logout'),

    path('student/',
         student_controller.index,
         name='student_index'),

    path('student_advices/',
         student_controller.get_student_advices,
         name='student_advices_paginator'),

    path('student/courses/',
         student_controller.student_courses,
         name='student_courses'),

    path('student_courses_grades/',
         student_controller.get_student_courses_grades,
         name='student_courses_grades'),

    path('student_courses/',
         student_controller.get_student_courses,
         name='student_courses_paginator'),

    path('student/educator/<int:educator_id>/',
         student_controller.educator_profile,
         name='student_educator_profile'),

    path('educator/',
         educator_controller.index,
         name='educator_index'),

    path('educator_rating/',
         educator_controller.get_educator_rating,
         name='educator_rating'),

    path('educator_reviews/',
         educator_controller.get_educator_reviews,
         name='educator_reviews_paginator'),

    path('educator/student/<int:student_id>/',
         educator_controller.student_profile,
         name='educator_student_profile'),

    path('educator/students/',
         educator_controller.educator_students,
         name='educator_students'),

    path('educator_courses_counts/',
         educator_controller.get_educator_courses_counts,
         name='educator_courses_counts'),

    path('educator_students/',
         educator_controller.get_educator_students,
         name='educator_students_paginator'),

    path('educator/review_report/',
         educator_controller.add_review_report,
         name='educator_add_review_report'),

    path('administrator/',
         administrator_controller.index,
         name='administrator_index'),

    path('administrator_years_counts/',
         administrator_controller.get_years_counts,
         name='administrator_years_counts'),

    path('administrator_students/',
         administrator_controller.get_students,
         name='administrator_students_paginator'),

    path('administrator/student/<int:student_id>/',
         administrator_controller.student_profile,
         name='administrator_student_update'),

    path('administrator/student/<int:student_id>/form/',
         administrator_controller.student_form_handler,
         name='administrator_student_update_form'),

    path('administrator/student/add/',
         administrator_controller.student_profile,
         name='administrator_student_add'),

    path('administrator/student/add/form/',
         administrator_controller.student_form_handler,
         name='administrator_student_add_form'),

    path('administrator/student/<int:student_id>/courses/form/',
         administrator_controller.student_courses_formset_handler,
         name='administrator_student_courses_update_form'),

    path('administrator/educators/',
         administrator_controller.educators,
         name='administrator_educators'),

    path('administrator_educators_rating/',
         administrator_controller.get_educators_rating,
         name='administrator_educators_rating'),

    path('administrator_educators/',
         administrator_controller.get_educators,
         name='administrator_educators_paginator'),

    path('administrator/educator/add/',
         administrator_controller.add_educator,
         name='administrator_add_educator'),
         
    path('administrator/educator/<int:educator_id>/',
         administrator_controller.educator_profile,
         name='administrator_educator_profile'),

    path('administrator/educator/<int:educator_id>/reviews/',
         administrator_controller.get_educator_reviews,
         name='administrator_educator_reviews_paginator'),
    
]
