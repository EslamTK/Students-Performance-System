from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.http import JsonResponse, HttpResponse, \
    HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.decorators.http import require_GET, require_POST, require_http_methods

from dashboard.forms.educator_advice_form import EducatorAdviceForm
from dashboard.logic import *

user = authenticate(username='educator', password='3$81jkjjSA')


@require_GET
def index(request):

    # Educator Reviews Rating
    educator_rating = educator.get_educator_rating(educator_id=user.id)

    # Educator Reviews Years
    educator_reviews_years = educator.get_educator_reviews_years(educator_id=user.id)

    # Educator Reviews Departments
    educator_reviews_departments = educator.get_educator_reviews_departments(educator_id=user.id)

    # Educator Reviews
    educator_reviews, educator_reviews_num_pages = educator.get_educator_reviews(educator_id=user.id)

    result = {
        'educator_rating': educator_rating,
        'educator_reviews_years': educator_reviews_years,
        'educator_reviews_departments': educator_reviews_departments,
        'educator_reviews': educator_reviews,
        'educator_reviews_num_pages': educator_reviews_num_pages
    }

    return render(request, 'educator/index.html', result)
    # For Testing Only
    # test_result = {
    #     'educator_reviews': list(educator_reviews),
    #     'educator_rating': list(educator_rating),
    #     'educator_reviews_years': list(educator_reviews_years),
    #     'educator_reviews_departments': list(educator_reviews_departments)
    # }
    # return JsonResponse(test_result, safe=False)


@require_GET
def get_educator_rating(request):
    # Getting the department
    department_id = request.GET.get('department_id')

    # Getting the year
    year = request.GET.get('year')

    # Getting the educator
    educator_id = request.GET.get('educator_id', user.id)

    # Educator Rating
    educator_rating = educator.get_educator_rating(educator_id=educator_id,
                                                   department_id=department_id, year=year)

    result = {
        'result': list(educator_rating)
    }

    return JsonResponse(result)


@require_GET
def get_educator_reviews(request):
    # Getting the page number
    page = request.GET.get('page')

    # Getting the page size
    page_size = request.GET.get('page_size', 4)

    # Educator Reviews
    educator_reviews, educator_reviews_num_pages = educator.get_educator_reviews(educator_id=user.id,
                                                                                 page=page, page_size=page_size)

    result = {
        'educator_reviews': educator_reviews,
        'educator_reviews_num_pages': educator_reviews_num_pages
    }
    template = 'educator/pagination.html'

    return render_to_response(template, result, content_type=RequestContext(request))

    # For Testing Only
    # test_result = {
    #     'educator_reviews': list(educator_reviews),
    #     'educator_reviews_num_pages': educator_reviews_num_pages
    # }
    #
    # return JsonResponse(test_result)


@require_http_methods(['GET', 'POST'])
def student_profile(request, student_id):
    # Educator Advice Form Submission
    if request.method == 'POST':

        advice_form = EducatorAdviceForm(request.POST)

        if advice_form.is_valid():
            try:
                educator.add_student_advice(student_id=student_id, educator_id=user.id,
                                            form=advice_form)

                return HttpResponseRedirect('')

            except IntegrityError:
                return HttpResponseBadRequest()

    else:
        advice_form = EducatorAdviceForm()

    # Student Current Courses Predictions
    predictions = student.get_student_predictions(student_id=student_id)

    # Years
    years = general.get_years()

    # Terms
    terms = general.get_terms()

    # Student Advices
    student_advices, student_advices_num_pages = student.get_student_advices(student_id=student_id)

    result = {
        'student_predictions': predictions,
        'years': years,
        'terms': terms,
        'student_id': student_id,
        'advice_form': advice_form,
        'student_advices': student_advices,
        'student_advices_num_pages': student_advices_num_pages
    }

    return render(request, 'educator/student_profile.html', result)

    # For Testing Only
    # test_result = {
    #     'student_predictions': predictions,
    #     'years': list(years.values()),
    #     'terms': list(terms.values()),
    #     'student_advices': list(student_advices.values())
    # }
    #
    # return JsonResponse(test_result, safe=False)


@require_GET
def educator_students(request):
    # Educator Students
    students, students_num_pages = educator.get_educator_students(educator_id=user.id)

    # Departments
    departments = general.get_departments()

    # Years
    years = general.get_years()

    # Terms
    terms = general.get_terms()

    # Educator Students Pass & Fail Counts
    courses_counts = educator.get_educator_counts(educator_id=user.id)

    result = {
        'educator_students': students,
        'educator_students_num_pages': students_num_pages,
        'departments': departments,
        'years': years,
        'terms': terms,
        'courses_counts': courses_counts
    }

    return render(request, 'educator/students.html', result)

    # For Testing Only
    # test_result = {
    #     'educator_students': list(students),
    #     'departments': list(departments.values()),
    #     'years': list(years.values()),
    #     'terms': list(terms.values()),
    #     'courses_counts': list(courses_counts)
    # }
    #
    # return JsonResponse(test_result, safe=False)


@require_GET
def get_educator_courses_counts(request):
    # Getting the department
    department_id = request.GET.get('department_id')

    # Getting the year
    year_id = request.GET.get('year_id')

    # Getting the term
    term_id = request.GET.get('term_id')

    # Educator Courses Counts
    educator_counts = educator.get_educator_counts(educator_id=user.id, department_id=department_id,
                                                   year_id=year_id, term_id=term_id)

    result = {
        'result': list(educator_counts)
    }

    return JsonResponse(result)


@require_GET
def get_educator_students(request):
    # Getting the page number
    page = request.GET.get('page')

    # Getting the page size
    page_size = request.GET.get('page_size', 6)

    # Getting the search keyword
    keyword = request.GET.get('keyword')

    # Educator Students
    students, students_num_pages = educator.get_educator_students(educator_id=user.id,
                                                                  keyword=keyword, page=page,
                                                                  page_size=page_size)

    result = {
        'educator_students': students,
        'educator_students_num_pages': students_num_pages,
    }

    template = 'educator/students_pagination.html'
    return render_to_response(template, result, content_type=RequestContext(request))

    # For Testing Only
    # test_result = {
    #     'educator_students': list(students),
    #     'educator_students_num_pages': students_num_pages
    # }
    #
    # return JsonResponse(test_result)


@require_POST
def add_review_report(request):
    # Getting the review id
    review_id = request.POST.get('review_id')

    if not review_id:
        return HttpResponseBadRequest('The required review_id is not given')

    try:
        educator.add_review_report(educator_id=user.id, review_id=review_id)

    except (ObjectDoesNotExist, ValueError, IntegrityError):
        return HttpResponseBadRequest('The given review_id is not valid')

    return HttpResponse('The review report added successfully')
