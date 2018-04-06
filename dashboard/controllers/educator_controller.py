from django.contrib.auth import authenticate
from django.http import JsonResponse

from dashboard.logic import educator_logic, student_logic, general_logic

user = authenticate(username='educator', password='3$81jkjjSA')


def index(request):
    # Educator Reviews Rating
    educator_rating = educator_logic.get_educator_rating(educator_id=user.id)

    # Educator Reviews Years
    educator_reviews_years = educator_logic.get_educator_reviews_years(educator_id=user.id)

    # Educator Reviews Departments
    educator_reviews_departments = educator_logic.get_educator_reviews_departments(educator_id=user.id)

    # Educator Reviews
    educator_reviews = educator_logic.get_educator_reviews(educator_id=user.id)

    # For Testing Only
    result = {
        'educator_reviews': list(educator_reviews),
        'educator_rating': list(educator_rating),
        'educator_reviews_years': list(educator_reviews_years),
        'educator_reviews_departments': list(educator_reviews_departments)
    }

    return JsonResponse(result, safe=False)


def student_profile(request, student_id):
    # Student Courses
    student_courses = student_logic.get_student_courses(student_id=student_id, is_all=True)

    # Student Advices
    student_advices = student_logic.get_student_advices(student_id=student_id)

    # For Testing Only
    result = {
        'student_courses': student_courses,
        'student_advices': list(student_advices.values())
    }

    return JsonResponse(result, safe=False)


def educator_students(request):
    # Educator Students
    students = educator_logic.get_educator_students(educator_id=user.id)

    # Departments
    departments = general_logic.get_departments()

    # Years
    years = general_logic.get_years()

    # Terms
    terms = general_logic.get_terms()

    # Educator Students Pass & Fail Counts
    courses_counts = educator_logic.get_educator_counts(educator_id=user.id)

    # For Testing Only
    result = {
        'educator_students': list(students),
        'departments': list(departments.values()),
        'years': list(years.values()),
        'terms': list(terms.values()),
        'courses_counts': list(courses_counts)
    }

    return JsonResponse(result, safe=False)
