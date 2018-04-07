from django.contrib.auth import authenticate

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

    result = {
        'educator_reviews': educator_reviews,
        'educator_rating': educator_rating,
        'educator_reviews_years': educator_reviews_years,
        'educator_reviews_departments': educator_reviews_departments
    }

    # For Testing Only
    # test_result = {
    #     'educator_reviews': list(educator_reviews),
    #     'educator_rating': list(educator_rating),
    #     'educator_reviews_years': list(educator_reviews_years),
    #     'educator_reviews_departments': list(educator_reviews_departments)
    # }
    # return JsonResponse(test_result, safe=False)


def student_profile(request, student_id):
    # Student Current Courses Predictions
    predictions = student_logic.get_student_predictions(student_id=student_id)

    # Years
    years = general_logic.get_years()

    # Terms
    terms = general_logic.get_terms()

    # Student Advices
    student_advices = student_logic.get_student_advices(student_id=student_id)

    result = {
        'student_predictions': predictions,
        'years': years,
        'terms': terms,
        'student_advices': student_advices
    }

    # For Testing Only
    # test_result = {
    #     'student_predictions': predictions,
    #     'years': list(years.values()),
    #     'terms': list(terms.values()),
    #     'student_advices': list(student_advices.values())
    # }
    #
    # return JsonResponse(test_result, safe=False)


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

    result = {
        'educator_students': students,
        'departments': departments,
        'years': years,
        'terms': terms,
        'courses_counts': courses_counts
    }

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
