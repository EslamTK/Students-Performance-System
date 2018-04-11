from django.contrib.auth import authenticate
from django.forms import model_to_dict
from django.http import JsonResponse

from dashboard.logic.administrator_logic import AdministratorLogic
from dashboard.logic.educator_logic import EducatorLogic
from dashboard.logic.general_logic import GeneralLogic
from dashboard.logic.student_logic import StudentLogic

user = authenticate(username='admin', password='a1$$m2IN12')

student_logic = StudentLogic()
educator_logic = EducatorLogic()
general_logic = GeneralLogic()
administrator_logic = AdministratorLogic()


def index(request):
    # Departments
    departments = general_logic.get_departments()

    # Terms
    terms = general_logic.get_terms()

    # Students
    students = administrator_logic.get_students()

    test_result = {
        'departments': list(departments.values()),
        'terms': list(terms.values()),
        'students': list(students)
    }
    return JsonResponse(test_result, safe=False)


def educators(request):
    # Departments
    departments = general_logic.get_departments()

    # Educators
    educators_list = administrator_logic.get_educators()

    # Educators Rating
    educators_rating = administrator_logic.get_educators_rating()

    test_result = {
        'departments': list(departments.values()),
        'educators': list(educators_list),
        'educators_rating': list(educators_rating)
    }

    return JsonResponse(test_result, safe=False)


def educator_profile(request, educator_id):
    # Educator Info
    educator_info = educator_logic.get_educator_info(educator_id=educator_id)

    # Available Accounts
    accounts = administrator_logic.get_educator_accounts(educator_id=educator_id)

    # Educator Accounts
    educator_accounts = educator_logic.get_educator_accounts(educator_id=educator_id)

    # Educator Reviews Rating
    educator_rating = educator_logic.get_educator_rating(educator_id=educator_id)

    # Educator Reviews Years
    educator_reviews_years = educator_logic.get_educator_reviews_years(educator_id=educator_id)

    # Educator Reviews Departments
    educator_reviews_departments = educator_logic.get_educator_reviews_departments(educator_id=educator_id)

    # Educator Reviews
    educator_reviews = educator_logic.get_educator_reviews(educator_id=educator_id)

    # For Testing Only
    educator_info = model_to_dict(educator_info)
    educator_info['photo'] = educator_info['photo'].url

    test_result = {
        'educator_info': educator_info,
        'educator_accounts': list(accounts),
        'educator_reviews': list(educator_reviews),
        'educator_rating': list(educator_rating),
        'educator_reviews_years': list(educator_reviews_years),
        'educator_reviews_departments': list(educator_reviews_departments)
    }

    return JsonResponse(test_result, safe=False)
