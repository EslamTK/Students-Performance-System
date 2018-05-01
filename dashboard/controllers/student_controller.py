from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.http import JsonResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.decorators.http import require_GET, require_http_methods

from dashboard.logic import *


def is_student(user):
    return user.groups.filter(name='students').exists()


@user_passes_test(is_student)
@require_GET
def index(request):
    user = request.user

    # Student Year and Term
    student_info = student.get_student_year_and_term(student_id=user.id)

    # Student Advices
    student_advices, student_advices_num_pages = student.get_student_advices(student_id=user.id)

    # Student Courses Predictions
    predictions = student.get_student_predictions(student_id=user.id)

    # Student Recommendations
    recommendations = student.get_student_recommendations(student_id=user.id)

    result = {
        'student_info': student_info,
        'student_advices': student_advices,
        'student_advices_num_pages': student_advices_num_pages,
        'student_predictions': predictions,
        'student_recommendations': recommendations
    }

    return render(request, 'student/index.html', result)


@user_passes_test(is_student)
@require_GET
def get_student_advices(request):
    user = request.user

    # Getting the page number
    page = request.GET.get('page')

    # Getting the page size
    page_size = request.GET.get('page_size', 4)

    # Student Advices
    student_advices, student_advices_num_pages = student.get_student_advices(student_id=user.id,
                                                                             page=page, page_size=page_size)

    result = {
        'student_advices': student_advices,
        'student_advices_num_pages': student_advices_num_pages
    }
    template = 'student/pagination/index.html'

    return render_to_response(template, result, content_type=RequestContext(request))


@user_passes_test(is_student)
@require_GET
def student_courses(request):
    user = request.user
    # Student Current Courses Predictions
    predictions = student.get_student_predictions(student_id=user.id)

    # Years
    years = general.get_years()

    # Terms
    terms = general.get_terms()

    # Student All Courses
    courses, courses_num_pages = student.get_student_courses(student_id=user.id, is_all=True)

    result = {
        'student_predictions': predictions,
        'years': years,
        'terms': terms,
        'student_courses': courses,
        'student_courses_num_pages': courses_num_pages
    }

    return render(request, 'student/courses.html', result)


@user_passes_test(is_student)
@require_GET
def get_student_courses_grades(request):
    user = request.user
    # Getting the year
    year_id = request.GET.get('year_id')

    # Getting the term
    term_id = request.GET.get('term_id')

    # Getting the student
    student_id = request.GET.get('student_id', user.id)

    # Student Courses Grades
    courses_grades = student.get_student_courses(student_id=student_id, is_current=False,
                                                 year=year_id, term=term_id)

    formatted_courses = []

    for i in courses_grades:
        course = {
            'id': i.course_id,
            'name': i.course.name,
            'midterm': i.midterm_grade,
            'final': i.final_grade
        }
        formatted_courses.append(course)

    result = {
        'result': formatted_courses,
    }

    return JsonResponse(result)


@user_passes_test(is_student)
@require_GET
def get_student_courses(request):
    user = request.user
    # Getting the page number
    page = request.GET.get('page')

    # Getting the page size
    page_size = request.GET.get('page_size', 6)

    # Getting the search keyword
    keyword = request.GET.get('keyword')

    # Student All Courses
    courses, courses_num_pages = student.get_student_courses(student_id=user.id, is_all=True, keyword=keyword,
                                                             page=page, page_size=page_size)

    result = {
        'student_courses': courses,
        'student_courses_num_pages': courses_num_pages
    }
    template = 'student/pagination/courses.html'

    return render_to_response(template, result, content_type=RequestContext(request))


@user_passes_test(is_student)
@require_http_methods(['GET', 'POST'])
def educator_profile(request, educator_id):
    user = request.user
    # Student Review Form Submission
    if request.method == 'POST':
        review = student.get_review_forms(request.POST)

        if review.is_valid() and review.review_items.is_valid():
            try:
                student.add_review(student_id=user.id, educator_id=educator_id, review_form=review)

                return HttpResponseRedirect('')

            except (ObjectDoesNotExist, IntegrityError):
                return HttpResponseBadRequest()

    # Educator Info
    educator_info = educator.get_educator_info(educator_id)

    # Educator Accounts
    educator_accounts = educator.get_educator_accounts(educator_id)

    # Review Forms
    review = student.get_review_forms()

    result = {
        'educator_info': educator_info,
        'educator_accounts': educator_accounts,
        'educator_id': educator_id,
        'review_form': review,
        'review_items_form': review.review_items
    }
    
    return render(request, 'student/educator_profile.html', result)
