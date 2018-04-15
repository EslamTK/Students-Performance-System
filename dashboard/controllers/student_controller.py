from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET, require_POST

from dashboard.logic.educator_logic import EducatorLogic
from dashboard.logic.general_logic import GeneralLogic
from dashboard.logic.student_logic import StudentLogic

user = authenticate(username='student', password='1#lklsaK313')

student_logic = StudentLogic()
educator_logic = EducatorLogic()
general_logic = GeneralLogic()


@require_GET
def index(request):
    # Student Advices
    student_advices = student_logic.get_student_advices(student_id=user.id)

    # Student Courses Predictions
    predictions = student_logic.get_student_predictions(student_id=user.id)

    # Student Recommendations
    recommendations = student_logic.get_student_recommendations(student_id=user.id)

    result = {
        'student_advices': student_advices,
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


@require_POST
def get_student_advices(request):
    # Getting the page
    page = request.POST.get('page')

    # Student Advices
    student_advices = student_logic.get_student_advices(student_id=user.id, page=page)

    return JsonResponse(list(student_advices.values()), safe=False)


@require_GET
def student_courses(request):
    # Student Current Courses Predictions
    predictions = student_logic.get_student_predictions(student_id=user.id)

    # Years
    years = general_logic.get_years()

    # Terms
    terms = general_logic.get_terms()

    # Student All Courses
    courses = student_logic.get_student_courses(student_id=user.id, is_all=True)

    result = {
        'student_predictions': predictions,
        'years': years,
        'terms': terms,
        'student_courses': courses
    }

    return render(request, 'student/courses.html', result)

    # For Testing Only
    # test_result = {
    #     'student_predictions': predictions,
    #     'years': list(years.values()),
    #     'terms': list(terms.values()),
    #     'student_courses': list(courses.values())
    # }
    # return JsonResponse(test_result, safe=False)


@require_POST
def get_student_courses(request):
    # Getting the page
    page = request.POST.get('page')

    # Student All Courses
    courses = student_logic.get_student_courses(student_id=user.id, is_all=True, page=page)

    return JsonResponse(list(courses.values()), safe=False)


@require_GET
def educator_profile(request, educator_id):
    # Educator Info
    educator_info = educator_logic.get_educator_info(educator_id)

    # Educator Accounts
    educator_accounts = educator_logic.get_educator_accounts(educator_id)

    # Review Items
    review_items = general_logic.get_review_items()

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
