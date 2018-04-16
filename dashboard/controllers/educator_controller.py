from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.http import require_GET

from dashboard.logic.educator_logic import EducatorLogic
from dashboard.logic.general_logic import GeneralLogic
from dashboard.logic.student_logic import StudentLogic

user = authenticate(username='educator', password='3$81jkjjSA')

student_logic = StudentLogic()
educator_logic = EducatorLogic()
general_logic = GeneralLogic()


@require_GET
def index(request):

    # Educator Reviews Rating
    educator_rating = educator_logic.get_educator_rating(educator_id=user.id)

    # Educator Reviews Years
    educator_reviews_years = educator_logic.get_educator_reviews_years(educator_id=user.id)

    # Educator Reviews Departments
    educator_reviews_departments = educator_logic.get_educator_reviews_departments(educator_id=user.id)

    # Educator Reviews
    educator_reviews, educator_reviews_num_pages = educator_logic.get_educator_reviews(educator_id=user.id)

    result = {
        'educator_rating': educator_rating,
        'educator_reviews_years': educator_reviews_years,
        'educator_reviews_departments': educator_reviews_departments,
        'educator_reviews': educator_reviews,
        'educator_reviews_num_pages': educator_reviews_num_pages,
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
def get_educator_reviews(request):
    # Getting the page number
    page = request.GET.get('page')

    # Educator Reviews
    educator_reviews, num_pages = educator_logic.get_educator_reviews(educator_id=user.id, page=page)

    formatted_reviews = list(educator_reviews)

    result = {
        'reviews': formatted_reviews,
        'num_pages': num_pages
    }

    return JsonResponse(result)


@require_GET
def student_profile(request, student_id):
    # Student Current Courses Predictions
    predictions = student_logic.get_student_predictions(student_id=student_id)

    # Years
    years = general_logic.get_years()

    # Terms
    terms = general_logic.get_terms()

    # Student Advices
    student_advices, student_advices_num_pages = student_logic.get_student_advices(student_id=student_id)
    
    result = {
        'student_predictions': predictions,
        'years': years,
        'terms': terms,
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
    students, students_num_pages = educator_logic.get_educator_students(educator_id=user.id)

    # Departments
    departments = general_logic.get_departments()

    # Years
    years = general_logic.get_years()

    # Terms
    terms = general_logic.get_terms()

    # Educator Students Pass & Fail Counts
    courses_counts = educator_logic.get_educator_counts(educator_id=user.id)

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
def get_educator_students(request):
    # Getting the page number
    page = request.GET.get('page')

    # Getting the search keyword
    keyword = request.GET.get('keyword')

    # Educator Students
    students, students_num_pages = educator_logic.get_educator_students(educator_id=user.id,
                                                                        keyword=keyword, page=page)

    formatted_students = list(students)

    result = {
        'students': formatted_students,
        'num_pages': students_num_pages
    }

    return JsonResponse(result)
