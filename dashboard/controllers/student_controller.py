from django.contrib.auth import authenticate
from django.http import JsonResponse

from dashboard.logic import educator_logic
from dashboard.logic import student_logic

user = authenticate(username='student', password='1#lklsaK313')


def index(request):
    student_advices = student_logic.get_student_advices(student_id=user.id)

    # For Testing Only
    result = {
        'student_advices': student_advices
    }

    return JsonResponse(result, safe=False)


def student_courses(request):
    courses = student_logic.get_student_courses(student_id=user.id)
    return JsonResponse(courses, safe=False)


def educator_profile(request, educator_id):
    # Educator Info
    educator_info = educator_logic.get_educator_info(educator_id)

    # Educator Accounts
    educator_accounts = educator_logic.get_educator_accounts(educator_id)

    # Review Items
    review_items = educator_logic.get_review_items()

    # For Testing Only
    result = {
        'educator_info': educator_info,
        'educator_accounts': educator_accounts,
        'review_items': review_items
    }

    return JsonResponse(result, safe=False)
