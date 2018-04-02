from .unit_of_work import UnitOfWork

unit_of_work = UnitOfWork()


def get_student_advices(student_id):
    result = unit_of_work.educators_advices.get_student_advices(student=student_id)
    advices = []
    for i in result:
        advice = {
            'educator_id': i.educator.user_id,
            'educator_name': i.educator.name,
            'educator_image_url': i.educator.image_url,
            'advice_content': i.content,
            'date': i.created_at
        }
        advices.append(advice)
    return advices


def get_student_courses(student_id):
    result = unit_of_work.students_courses.get_student_courses(student=student_id)

    courses = {}

    for i in result:

        if i.final_grade is None:
            continue

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

        courses[i.course.year.id]['terms'][i.course.term.id]['courses'].append({
            'id': i.course.id,
            'name': i.course.name,
            'midterm': i.midterm_grade,
            'final': i.final_grade,
            'educator': {
                'id': i.educator.user_id,
                'name': i.educator.name
            }
        })

    formated_courses = []

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

        formated_courses.append(year)

    return formated_courses
