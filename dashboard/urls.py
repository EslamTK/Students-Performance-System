from django.urls import path

# from dashboard.controllers import forms_testing
from dashboard.controllers import administrator_controller
from dashboard.controllers.educator.apis.counts import EducatorStudentsCountsApi
from dashboard.controllers.educator.apis.rating import EducatorRatingApi
from dashboard.controllers.educator.apis.report import EducatorReportApi
from dashboard.controllers.educator.apis.student_courses import EducatorStudentsCoursesGradesApi
from dashboard.controllers.educator.views.index import EducatorIndexView, EducatorReviewsPaginatorView
from dashboard.controllers.educator.views.student_profile import EducatorStudentProfileView, \
    EducatorStudentAdvicesPaginatorView
from dashboard.controllers.educator.views.students import EducatorStudentsView, EducatorStudentsPaginatorView
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

    path('student/advices/paginator/',
         StudentAdvicesPaginatorView.as_view(),
         name='student_advices_paginator'),

    path('student/courses/',
         StudentCoursesView.as_view(),
         name='student_courses'),

    path('student/courses/paginator/',
         StudentCoursesPaginatorView.as_view(),
         name='student_courses_paginator'),

    path('api/student/courses/grades/',
         StudentCoursesGradesApi.as_view(),
         name='student_courses_grades_api'),

    path('student/educator/<int:educator_id>/',
         StudentEducatorProfileView.as_view(),
         name='student_educator_profile'),


    path('educator/',
         EducatorIndexView.as_view(),
         name='educator_index'),

    path('educator/reviews/paginator/',
         EducatorReviewsPaginatorView.as_view(),
         name='educator_reviews_paginator'),

    path('api/educator/rating/',
         EducatorRatingApi.as_view(),
         name='educator_rating_api'),

    path('api/educator/reviews/report/',
         EducatorReportApi.as_view(),
         name='educator_add_report_api'),

    path('educator/students/',
         EducatorStudentsView.as_view(),
         name='educator_students'),

    path('educator/students/paginator/',
         EducatorStudentsPaginatorView.as_view(),
         name='educator_students_paginator'),

    path('api/educator/students/counts/',
         EducatorStudentsCountsApi.as_view(),
         name='educator_students_counts_api'),

    path('educator/students/<int:student_id>/',
         EducatorStudentProfileView.as_view(),
         name='educator_student_profile'),

    path('educator/students/<int:student_id>/advices/paginator/',
         EducatorStudentAdvicesPaginatorView.as_view(),
         name='educator_student_profile_advices_paginator'),

    path('api/educator/students/<int:student_id>/courses/grades/',
         EducatorStudentsCoursesGradesApi.as_view(),
         name='educator_student_profile_courses_grades_api'),


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
