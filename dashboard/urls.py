from django.urls import path

from dashboard.controllers.administrator.apis.educator_rating import AdministratorEducatorRatingApi
from dashboard.controllers.administrator.apis.educators_rating import AdministratorEducatorsRatingApi
from dashboard.controllers.administrator.apis.review_actions import AdministratorReviewActionsApi
from dashboard.controllers.administrator.apis.students_years_performance import AdministratorStudentsYearsPerformanceApi
from dashboard.controllers.administrator.views.educator_profile import AdministratorEducatorProfileView, \
    AdministratorEducatorReviewsPaginatorView
from dashboard.controllers.administrator.views.educators import AdministratorEducatorsView, \
    AdministratorEducatorsPaginatorView
from dashboard.controllers.administrator.views.index import AdministratorIndexView, \
    AdministratorStudentsPaginatorView
from dashboard.controllers.administrator.views.student_profile import AdministratorStudentProfileView, \
    AdministratorStudentCoursesView
from dashboard.controllers.educator.apis.rating import EducatorRatingApi
from dashboard.controllers.educator.apis.review_report import EducatorReportApi
from dashboard.controllers.educator.apis.student_courses import EducatorStudentsCoursesGradesApi
from dashboard.controllers.educator.apis.students_counts import EducatorStudentsCountsApi
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

    path('student/educators/<int:educator_id>/',
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
         AdministratorIndexView.as_view(),
         name='administrator_index'),

    path('administrator/students/',
         AdministratorIndexView.as_view(),
         name='administrator_students'),

    path('administrator/students/paginator/',
         AdministratorStudentsPaginatorView.as_view(),
         name='administrator_students_paginator'),

    path('api/administrator/students/years/performance/',
         AdministratorStudentsYearsPerformanceApi.as_view(),
         name='administrator_students_years_performance_api'),

    path('administrator/students/add/',
         AdministratorStudentProfileView.as_view(),
         name='administrator_student_add'),

    path('administrator/students/<int:student_id>/',
         AdministratorStudentProfileView.as_view(),
         name='administrator_student_update'),

    path('administrator/students/<int:student_id>/courses/',
         AdministratorStudentCoursesView.as_view(),
         name='administrator_student_courses_update'),


    path('administrator/educators/',
         AdministratorEducatorsView.as_view(),
         name='administrator_educators'),

    path('administrator/educators/paginator/',
         AdministratorEducatorsPaginatorView.as_view(),
         name='administrator_educators_paginator'),

    path('api/administrator/educators/rating/',
         AdministratorEducatorsRatingApi.as_view(),
         name='administrator_educators_rating_api'),

    path('administrator/educators/add/',
         AdministratorEducatorProfileView.as_view(),
         name='administrator_educator_add'),

    path('administrator/educators/<int:educator_id>/',
         AdministratorEducatorProfileView.as_view(),
         name='administrator_educator_profile'),

    path('administrator/educators/<int:educator_id>/reviews/paginator/',
         AdministratorEducatorReviewsPaginatorView.as_view(),
         name='administrator_educator_reviews_paginator'),

    path('api/administrator/educators/<int:educator_id>/rating/',
         AdministratorEducatorRatingApi.as_view(),
         name='administrator_educator_rating_api'),

    path('api/administrator/reviews/actions/',
         AdministratorReviewActionsApi.as_view(),
         name='administrator_review_actions_api')
]
