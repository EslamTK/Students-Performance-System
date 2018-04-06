from machine_learning import api as ml_api
from .unit_of_work import UnitOfWork

unit_of_work = UnitOfWork()


def get_student_advices(student_id):
    advices = unit_of_work.educators_advices.get_student_advices(student=student_id)

    return advices


def get_student_courses(student_id, is_all=False):
    courses_prediction = None
    if is_all:
        result = unit_of_work.students_courses.get_student_courses(student=student_id, is_all=True)
        courses_prediction = get_student_predictions(student_id)
    else:
        result = unit_of_work.students_courses.get_student_courses(student=student_id, is_current=False)

    courses = {}

    for i in result:
        if i.course.year.id not in courses:
            courses[i.course.year.id] = {}

        courses[i.course.year.id]['year_id'] = i.course.year.id
        courses[i.course.year.id]['year_name'] = i.course.year.name

        if 'terms' not in courses[i.course.year.id]:
            courses[i.course.year.id]['terms'] = {}

        if i.course.term.id not in courses[i.course.year.id]['terms']:
            courses[i.course.year.id]['terms'][i.course.term.id] = {}

        courses[i.course.year.id]['terms'][i.course.term.id]['term_id'] = i.course.term.id
        courses[i.course.year.id]['terms'][i.course.term.id]['term_name'] = i.course.term.name

        if 'courses' not in courses[i.course.year.id]['terms'][i.course.term.id]:
            courses[i.course.year.id]['terms'][i.course.term.id]['courses'] = []

        course = {
            'id': i.course.id,
            'name': i.course.name,
            'midterm': i.midterm_grade,
            'educator': {
                'id': i.educator.user_id,
                'name': i.educator.name
            }
        }

        if i.final_grade:
            course['final'] = i.final_grade
        else:
            for j in courses_prediction['courses']:
                if j['id'] == i.course.id:
                    course['prediction'] = j['prediction']

        courses[i.course.year.id]['terms'][i.course.term.id]['courses'].append(course)

    formatted_courses = []

    for i in courses:
        year = {
            'year_id': courses[i]['year_id'],
            'year_name': courses[i]['year_name'],
            'terms': []
        }

        for j in courses[i]['terms']:
            term = {
                'term_id': courses[i]['terms'][j]['term_id'],
                'term_name': courses[i]['terms'][j]['term_name'],
                'courses': courses[i]['terms'][j]['courses']
            }
            year['terms'].append(term)

        formatted_courses.append(year)

    return formatted_courses


def get_student_predictions(student_id):
    student_data = get_student_data(student_id)
    predictions = ml_api.prediction(student_data)

    return predictions


def get_student_recommendations(student_id):
    student_data = get_student_data(student_id)
    recommendations = ml_api.recommendation(student_data)

    return recommendations


def get_student_data(student_id):
    student = unit_of_work.students.get_one(student_id)
    student_courses = unit_of_work.students_courses.get_student_courses(student=student_id)

    student_data = {
        "sex": student.sex,
        "age": student.age,
        "famsize": student.family_size,
        "Pstatus": student.parent_status,
        "Medu": student.mother_education,
        "Fedu": student.father_education,
        "Mjob": student.mother_job,
        "Fjob": student.father_job,
        "guardian": student.guardian,
        "traveltime": student.travel_time,
        "health": student.health_status,
        "activities": convert_boolean_to_yes_no(student.do_extra_activity),
        "higher": convert_boolean_to_yes_no(student.wants_higher_education),
        "internet": convert_boolean_to_yes_no(student.has_internet),
        "romantic": convert_boolean_to_yes_no(student.has_relationship),
        "freetime": student.free_time,
        "goout": student.go_out_time,
        "famrel": student.family_relation_quality,
        "courses": []
    }

    for i in student_courses:
        course = {
            "id": i.course.id,
            "name": i.course.name,
            "studytime": i.study_time,
            "failures": i.failures,
            "absences": i.absences,
            "famsup": convert_boolean_to_yes_no(i.has_family_support),
            "paid": convert_boolean_to_yes_no(i.take_paid_class),
            "midterm": i.midterm_grade
        }
        student_data['courses'].append(course)

    return student_data


def convert_boolean_to_yes_no(value):
    if value:
        return 'yes'
    return 'no'
