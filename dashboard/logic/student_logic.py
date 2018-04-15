from django.core.paginator import Paginator

from machine_learning import api as ml_api
from .unit_of_work import UnitOfWork
from .utilities import convert_boolean_to_yes_no


class StudentLogic:

    def __init__(self):
        self.unit_of_work = UnitOfWork()

    def get_student_advices(self, student_id, page=1, page_size=6):
        advices = self.unit_of_work.educators_advices.get_student_advices(student=student_id)

        advices = Paginator(advices, page_size).get_page(page)

        return advices

    def get_student_courses(self, student_id, is_all=False, year=None, term=None,
                            page=1, page_size=6):
        courses = self.unit_of_work.students_courses. \
            get_student_courses(student=student_id, is_all=is_all, year=year, term=term)

        courses = Paginator(courses, page_size).get_page(page)

        return courses

    def get_student_predictions(self, student_id):
        student_data = self.__get_student_formatted_data(student_id)
        predictions = ml_api.prediction(student_data)

        return predictions

    def get_student_recommendations(self, student_id):
        student_data = self.__get_student_formatted_data(student_id)
        recommendations = ml_api.recommendation(student_data)

        return recommendations

    def get_student_data(self, student_id):
        student = self.unit_of_work.students.get_one(student_id)

        return student

    def __get_student_formatted_data(self, student_id):
        student = self.get_student_data(student_id)
        student_courses = self.get_student_courses(student_id)

        student_data = {
            "sex": student.gender,
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
