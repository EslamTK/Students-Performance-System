from django.urls import path

# from dashboard.controllers import forms_testing
from dashboard.controllers import educator_controller, administrator_controller
from dashboard.controllers.student.apis.courses_grades import StudentCoursesGradesApi
from dashboard.controllers.student.views.courses import StudentCoursesView, StudentCoursesPaginatorView
from dashboard.controllers.student.views.educator_profile import StudentEducatorProfileView
from dashboard.controllers.student.views.index import StudentIndexView, StudentAdvicesPaginatorView
from dashboard.controllers.user.login import LoginView
from dashboard.controllers.user.logout import LogoutView

app_name = 'dashboard'

urlpatterns = [

    # path('form/',
    #      forms_testing.index,
    #      name='form'),

    path('login/',
         LoginView.as_view(),
         name='user_login'),

    path('logout/',
         LogoutView.as_view(),
         name='user_logout'),

    path('student/',
         StudentIndexView.as_view(),
         name='student_index'),

    path('student/advices/',
         StudentAdvicesPaginatorView.as_view(),
         name='student_advices_paginator'),

    path('student/courses/',
         StudentCoursesView.as_view(),
         name='student_courses'),

    path('student/courses/paginator',
         StudentCoursesPaginatorView.as_view(),
         name='student_courses_paginator'),

    path('api/student/courses/grades/',
         StudentCoursesGradesApi.as_view(),
         name='student_courses_grades_api'),

    path('student/educator/<int:educator_id>/',
         StudentEducatorProfileView.as_view(),
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
