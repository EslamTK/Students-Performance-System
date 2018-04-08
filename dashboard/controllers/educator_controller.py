from django.contrib.auth import authenticate
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
    
    paginator = Paginator(educator_reviews, 2) # Show 3 contacts per page

    page = request.GET.get('page')
    try:
        reviews = paginator.page(page)
    except PageNotAnInteger:
        reviews = paginator.page(1)
    except EmptyPage:
        reviews = paginator.page(paginator.num_pages)

    result = {
        'educator_reviews': reviews,
        'educator_rating': educator_rating,
        'educator_reviews_years': educator_reviews_years,
        'educator_reviews_departments': educator_reviews_departments,
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


def student_profile(request, student_id):
    # Student Current Courses Predictions
    predictions = student_logic.get_student_predictions(student_id=student_id)

    # Years
    years = general_logic.get_years()

    # Terms
    terms = general_logic.get_terms()

    # Student Advices
    student_advices = student_logic.get_student_advices(student_id=student_id)

    paginator = Paginator(student_advices, 3) # Show 3 contacts per page

    page = request.GET.get('page')
    try:
        advice = paginator.page(page)
    except PageNotAnInteger:
        advice = paginator.page(1)
    except EmptyPage:
        advice = paginator.page(paginator.num_pages)
    
    result = {
        'student_predictions': predictions,
        'years': years,
        'terms': terms,
        'student_advices': advice
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
    
    paginator = Paginator(students, 3) # Show 3 contacts per page

    page = request.GET.get('page')
    try:
        student = paginator.page(page)
    except PageNotAnInteger:
        student = paginator.page(1)
    except EmptyPage:
        student = paginator.page(paginator.num_pages)

    result = {
        'educator_students': student,
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
