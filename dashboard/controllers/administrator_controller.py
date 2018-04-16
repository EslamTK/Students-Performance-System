from django.contrib.auth import authenticate
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET

from dashboard.logic.administrator_logic import AdministratorLogic
from dashboard.logic.educator_logic import EducatorLogic
from dashboard.logic.general_logic import GeneralLogic
from dashboard.logic.student_logic import StudentLogic

user = authenticate(username='admin', password='a1$$m2IN12')

student_logic = StudentLogic()
educator_logic = EducatorLogic()
general_logic = GeneralLogic()
administrator_logic = AdministratorLogic()


@require_GET
def index(request):
    # Departments
    departments = general_logic.get_departments()

    # Terms
    terms = general_logic.get_terms()

    # Years Success And Fail Counts
    years_counts = administrator_logic.get_courses_pass_fail_counts()

    # Students
    students, students_num_pages = administrator_logic.get_students()

    result = {
        'departments': departments,
        'terms': terms,
        'years_counts': years_counts,
        'students': students,
        'students_num_pages': students_num_pages
    }

    # For Testing Only
    # test_result = {
    #     'departments': list(departments.values()),
    #     'terms': list(terms.values()),
    #     'years_counts': list(years_counts),
    #     'students': list(students)
    # }
    # return JsonResponse(test_result, safe=False)
    return render(request, 'administrator/index.html', result)


@require_GET
def get_students(request):
    # Getting the page number
    page = request.GET.get('page')

    # Getting the search keyword
    keyword = request.GET.get('keyword')

    # Students
    students, num_pages = administrator_logic.get_students(keyword=keyword, page=page)

    formatted_students = list(students)

    result = {
        'students': formatted_students,
        'num_pages': num_pages
    }

    return JsonResponse(result)


@require_GET
def student_profile(request, student_id):
    # Student Data
    student = student_logic.get_student_data(student_id=student_id)

    # Departments
    departments = general_logic.get_departments()

    # Years
    years = general_logic.get_years()

    # Available Courses For The Student Year
    courses = administrator_logic.get_available_student_courses(student_id=student_id)

    # Student Courses
    student_courses = student_logic.get_student_courses(student_id=student_id)

    result = {
        'student': student,
        'genders': student.gender_choices,
        'jobs': student.job_choices,
        'family_sizes': student.family_size_choices,
        'parents_status': student.parent_status_choices,
        'guardians': student.guardian_choices,
        'departments': departments,
        'years': years,
        'student_courses': student_courses,
        'courses': courses
    }

    return render(request, 'administrator/admin_student_profile.html', result)
    # For Testing Only
    # test_result = {
    #     'student': model_to_dict(student),
    #     'genders': student.gender_choices,
    #     'jobs': student.job_choices,
    #     'family_sizes': student.family_size_choices,
    #     'parents_status': student.parent_status_choices,
    #     'guardians': student.guardian_choices,
    #     'departments': list(departments.values()),
    #     'years': list(years.values()),
    #     'student_courses': list(student_courses.values()),
    #     'courses': list(courses.values())
    # }
    #
    # return JsonResponse(test_result, safe=False)


@require_GET
def educators(request):
    # Departments
    departments = general_logic.get_departments()

    # Educators
    educators_list, educators_num_pages = administrator_logic.get_educators()

    # Educators Rating
    educators_rating = administrator_logic.get_educators_rating()

    result = {
        'departments': departments,
        'educators': educators_list,
        'educators_num_pages': educators_num_pages,
        'educators_rating': educators_rating
    }

    return render(request, 'administrator/admin_educators.html', result)
    # For Testing Only
    # test_result = {
    #     'departments': list(departments.values()),
    #     'educators': list(educators_list),
    #     'educators_rating': list(educators_rating)
    # }
    #
    # return JsonResponse(test_result, safe=False)


@require_GET
def get_educators(request):
    # Getting the page number
    page = request.GET.get('page')

    # Getting the search keyword
    keyword = request.GET.get('keyword')

    # Students
    educators_list, num_pages = administrator_logic.get_educators(keyword=keyword, page=page)

    formatted_educators = list(educators_list)

    result = {
        'educators': formatted_educators,
        'num_pages': num_pages
    }

    return JsonResponse(result)


@require_GET
def educator_profile(request, educator_id):
    # Educator Info
    educator_info = educator_logic.get_educator_info(educator_id=educator_id)

    # All the accounts including url if the educator has the account
    accounts = administrator_logic.get_educator_accounts(educator_id=educator_id)

    # Educator Reviews Rating
    educator_rating = educator_logic.get_educator_rating(educator_id=educator_id)

    # Educator Reviews Years
    educator_reviews_years = educator_logic.get_educator_reviews_years(educator_id=educator_id)

    # Educator Reviews Departments
    educator_reviews_departments = educator_logic.get_educator_reviews_departments(educator_id=educator_id)

    # Educator Reviews
    educator_reviews, educator_reviews_num_pages = educator_logic.get_educator_reviews(educator_id=educator_id)

    educator_info = model_to_dict(educator_info)
    educator_info['photo'] = educator_info['photo'].url

    educator_accounts = []

    for i in accounts:
        account = {
            'id': i.id,
            'name': i.name,
            'logo': i.logo.url,
            'url': i.url
        }
        educator_accounts.append(account)

    result = {
        'educator_info': educator_info,
        'educator_accounts': educator_accounts,
        'educator_reviews': educator_reviews,
        'educator_reviews_num_pages': educator_reviews_num_pages,
        'educator_rating': educator_rating,
        'educator_reviews_years': educator_reviews_years,
        'educator_reviews_departments': educator_reviews_departments
    }

    return render(request, 'administrator/admin_educator_profile.html', result)
    # For Testing Only
    # educator_info = model_to_dict(educator_info)
    # educator_info['photo'] = educator_info['photo'].url
    #
    # educator_accounts = []
    #
    # for i in accounts:
    #     account = {
    #         'id': i.id,
    #         'name': i.name,
    #         'logo': i.logo.url,
    #         'url': i.url
    #     }
    #     educator_accounts.append(account)
    #
    # test_result = {
    #     'educator_info': educator_info,
    #     'educator_accounts': educator_accounts,
    #     'educator_reviews': list(educator_reviews),
    #     'educator_rating': list(educator_rating),
    #     'educator_reviews_years': list(educator_reviews_years),
    #     'educator_reviews_departments': list(educator_reviews_departments)
    # }
    #
    # return JsonResponse(test_result, safe=False)
