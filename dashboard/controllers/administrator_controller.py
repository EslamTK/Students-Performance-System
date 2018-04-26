import json

from django.contrib.auth import authenticate
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext
from django.views.decorators.http import require_GET, require_http_methods, require_POST

from dashboard.logic import *

user = authenticate(username='admin', password='a1$$m2IN12')


@require_GET
def index(request):
    # Departments
    departments = general.get_departments()

    # Years
    years = general.get_years()

    # Terms
    terms = general.get_terms()

    # Years Success And Fail Counts
    years_counts = administrator.get_courses_pass_fail_counts()

    # Students
    students, students_num_pages = administrator.get_students()

    result = {
        'departments': departments,
        'years': years,
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
def get_years_counts(request):
    # Getting the department
    department_id = request.GET.get('department_id')

    # Getting the year
    year_id = request.GET.get('year_id')

    # Getting the term
    term_id = request.GET.get('term_id')

    # Years Success And Fail Counts
    years_counts = administrator.get_courses_pass_fail_counts(department_id=department_id,
                                                              year_id=year_id, term_id=term_id)

    result = {
        'result': list(years_counts),
    }

    return JsonResponse(result)


@require_GET
def get_students(request):
    # Getting the page number
    page = request.GET.get('page')

    # Getting the page size
    page_size = request.GET.get('page_size', 6)

    # Getting the search keyword
    keyword = request.GET.get('keyword')

    # Students
    students, students_num_pages = administrator.get_students(keyword=keyword, page=page,
                                                              page_size=page_size)

    result = {
        'students': students,
        'students_num_pages': students_num_pages
    }
    template = 'administrator/pagination.html'

    return render_to_response(template, result, content_type=RequestContext(request))

    # For Testing Only
    # test_result = {
    #     'students': list(students),
    #     'students_num_pages': students_num_pages
    # }
    #
    # return JsonResponse(test_result)


@require_GET
def student_profile(request, student_id=None):
    # User Form
    user_form = None

    # Courses Formset
    courses_formset = None

    if student_id:
        courses_formset = administrator.get_student_courses_formset(student_id=student_id)
    else:
        user_form = administrator.get_user_form()

    # Student Form
    student_form = administrator.get_student_form(student_id=student_id)

    result = {
        'student_id': student_id,
        'student_form': student_form,
        'user_form': user_form,
        'courses_formset': courses_formset
    }

    return render(request, 'administrator/admin_student_profile.html', result)


@require_POST
def student_form_handler(request, student_id=None):
    user_form = None

    student_form = administrator.get_student_form(request_data=request.POST,
                                                  student_id=student_id)
    if student_id:

        if student_form.is_valid():
            administrator.update_student(student_form)

    else:
        user_form = administrator.get_user_form(request_data=request.POST)

        if user_form.is_valid() and student_form.is_valid():
            student_id = administrator.add_student(user_form, student_form)

            return redirect(to='dashboard:administrator_student_update',
                            student_id=student_id)

    result = {
        'student_id': student_id,
        'student_form': student_form,
        'user_form': user_form
    }


@require_POST
def student_courses_formset_handler(request, student_id):
    courses_formset = administrator. \
        get_student_courses_formset(request_data=request.POST, student_id=student_id)

    if courses_formset.is_valid():
        administrator.update_student_courses(course_formset=courses_formset,
                                             student_id=student_id)
    result = {
        'student_id': student_id,
        'courses_formset': courses_formset
    }


@require_GET
def educators(request):
    # Departments
    departments = general.get_departments()

    # Years
    years = general.get_years()

    # Educators
    educators_list, educators_num_pages = administrator.get_educators()

    # Educators Rating
    educators_rating = administrator.get_educators_rating()
    educators_rating = json.dumps(list(educators_rating), cls=DjangoJSONEncoder)

    result = {
        'departments': departments,
        'years': years,
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
def get_educators_rating(request):
    # Getting the department
    department_id = request.GET.get('department_id')

    # Getting the year
    year_id = request.GET.get('year_id')

    # Educators Rating
    educators_rating = administrator.get_educators_rating(department_id=department_id,
                                                          year_id=year_id)
    result = {
        'result': list(educators_rating),
    }

    return JsonResponse(result)


@require_GET
def get_educators(request):
    # Getting the page number
    page = request.GET.get('page')

    # Getting the page size
    page_size = request.GET.get('page_size', 6)

    # Getting the search keyword
    keyword = request.GET.get('keyword')

    # Students
    educators_list, educators_num_pages = administrator.get_educators(keyword=keyword, page=page,
                                                                      page_size=page_size)

    result = {
        'educators': educators_list,
        'educators_num_pages': educators_num_pages,
    }
    template = 'administrator/educators_pagination.html'

    return render_to_response(template, result, content_type=RequestContext(request))

    # For Testing Only
    # test_result = {
    #     'educators': list(educators_list),
    #     'educators_num_pages': educators_num_pages
    # }
    #
    # return JsonResponse(test_result)


@require_http_methods(['GET', 'POST'])
def educator_profile(request, educator_id):
    # Educator profile and accounts forms
    if request.method == 'POST':
        educator_form = administrator.get_educator_form(request_data=request.POST,
                                                        request_files=request.FILES,
                                                        educator_id=educator_id)

        accounts_formset = educator_form.accounts_formset
        if educator_form.is_valid() and accounts_formset.is_valid():
            administrator.update_educator(educator_id=educator_id, educator_form=educator_form,
                                          accounts_formset=educator_form.accounts_formset)
            return HttpResponse('Updated Successfully')
    else:
        educator_form = administrator.get_educator_form(educator_id=educator_id)
        accounts_formset = educator_form.accounts_formset

    # Educator Reviews Rating
    educator_rating = educator.get_educator_rating(educator_id=educator_id)

    # Educator Reviews Years
    educator_reviews_years = educator.get_educator_reviews_years(educator_id=educator_id)

    # Educator Reviews Departments
    educator_reviews_departments = educator.get_educator_reviews_departments(educator_id=educator_id)

    # Educator Reviews
    educator_reviews, educator_reviews_num_pages = educator.get_educator_reviews(educator_id=educator_id)

    result = {
        'educator_id':educator_id,
        'educator_form': educator_form,
        'educator_accounts_form': accounts_formset,
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


@require_http_methods(['GET', 'POST'])
def add_educator(request):
    # Educator profile and accounts forms
    if request.method == 'POST':
        user_form = administrator.get_user_form(request_data=request.POST)

        educator_form = administrator.get_educator_form(request_data=request.POST,
                                                        request_files=request.FILES)

        accounts_formset = educator_form.accounts_formset

        if user_form.is_valid() and educator_form.is_valid() and accounts_formset.is_valid():
            administrator.add_educator(user_form=user_form, educator_form=educator_form,
                                       accounts_formset=accounts_formset)

            return HttpResponse('Added Successfully')
    else:
        user_form = administrator.get_user_form()
        educator_form = administrator.get_educator_form()
        accounts_formset = educator_form.accounts_formset

    result = {
        'user_form': user_form,
        'educator_form': educator_form,
        'educator_accounts_form': accounts_formset
    }

    return render(request, 'administrator/admin_create_user.html', result)
