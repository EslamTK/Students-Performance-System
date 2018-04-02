from collections import defaultdict

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
    courses = defaultdict(dict)

    for i in result:
        courses[i.course.year.id][i.course.term.id] = {}
        courses[i.course.year.id][i.course.term.id]['term_name'] = i.course.term.name
        courses[i.course.year.id][i.course.term.id]['courses'].append({
            'id': i.course.id,
            'name': i.course.name,
            'midterm': i.midterm_grade,
            'final': i.final_grade,
            'educator': {
                'id': i.educator.id,
                'name': i.educator.name
            }
        })
        courses[i.course.year.id]['year_id'] = i.course.year.id
        courses[i.course.year.id]['year_name'] = i.course.year.name

    return courses
