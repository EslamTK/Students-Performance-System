from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.views.decorators.http import require_GET

from dashboard.logic import *

user = authenticate(username='student', password='1#lklsaK313')


@require_GET
def index(request):

    # Student Advices
    student_advices, student_advices_num_pages = student.get_student_advices(student_id=user.id)

    # Student Courses Predictions
    predictions = student.get_student_predictions(student_id=user.id)

    # Student Recommendations
    recommendations = student.get_student_recommendations(student_id=user.id)

    result = {
        'student_advices': student_advices,
        'student_advices_num_pages': student_advices_num_pages,
        'student_predictions': predictions,
        'student_recommendations': recommendations
    }

    return render(request, 'student/index.html', result)

    # For Testing Only
    # test_result = {
    #    'student_advices': list(student_advices.values()),
    #    'student_predictions': predictions,
    #    'student_recommendations': recommendations
    # }
    # return JsonResponse(test_result, safe=False)


@require_GET
def get_student_advices(request):
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
    template = 'student/pagination.html'

    
    return render_to_response(template,result,content_type=RequestContext(request))
    # For Testing Only
    #formatted_advices = []
    #
    #for i in student_advices:
    #    advice = {
    #        'id': i.id,
    #        'educator_id': i.educator_id,
    #        'educator_name': i.educator.name,
    #        'educator_photo_url': i.educator.photo.url,
    #        'created_at': i.created_at,
    #        'content': i.content
    #   }
    #    formatted_advices.append(advice)
    
    #test_result = {
    #    'advices': formatted_advices,
    #    'num_pages': student_advices_num_pages
    #}
    
    #return JsonResponse(test_result)


@require_GET
def student_courses(request):
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
    print(result)
    return render(request, 'student/courses.html', result)

    # For Testing Only
    # test_result = {
    #     'student_predictions': predictions,
    #     'years': list(years.values()),
    #     'terms': list(terms.values()),
    #     'student_courses': list(courses.values()),
    #     'student_courses_num_pages': courses_num_pages
    # }
    # return JsonResponse(test_result, safe=False)


@require_GET
def get_student_courses_grades(request):
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


@require_GET
def get_student_courses(request):
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
    template = 'student/courses_pagination.html'

    
    return render_to_response(template,result,content_type=RequestContext(request))

    # For Testing Only
    # formatted_courses = []
    #
    # for i in courses:
    #     course = {
    #         'id': i.id,
    #         'course_name': i.course.name,
    #         'year_name': i.course.year.name,
    #         'educator_id': i.educator_id,
    #         'educator_name': i.educator.name,
    #         'final_grade': i.final_grade,
    #     }
    #     formatted_courses.append(course)
    #
    # test_result = {
    #     'courses': formatted_courses,
    #     'num_pages': courses_num_pages
    # }
    #
    # return JsonResponse(test_result)


@require_GET
def educator_profile(request, educator_id):
    # Educator Info
    educator_info = educator.get_educator_info(educator_id)

    # Educator Accounts
    educator_accounts = educator.get_educator_accounts(educator_id)

    # Review Items
    review_items = general.get_review_items()

    result = {
        'educator_info': educator_info,
        'educator_accounts': educator_accounts,
        'review_items': review_items
    }

    return render(request, 'student/educator_profile.html', result)

    # For Testing Only
    # educator_info = model_to_dict(educator_info)
    # educator_info['photo'] = educator_info['photo'].url
    #
    # test_result = {
    #     'educator_info': educator_info,
    #     'educator_accounts': list(educator_accounts.values()),
    #     'review_items': list(review_items.values())
    # }
    # return JsonResponse(test_result, safe=False)
