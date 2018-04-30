from django.db import transaction

from dashboard.forms.student_review_form import StudentReviewForm
from machine_learning import api as ml_api
from .logic import Logic
from .utilities import convert_boolean_to_yes_no, get_paginated_result_and_num_pages


class StudentLogic(Logic):

    def get_student_year_and_term(self, student_id):
        return self._unit_of_work.students.get_year_and_term(student=student_id)

    def get_student_advices(self, student_id, page=1, page_size=4):
        advices = self._unit_of_work.educators_advices.get_student_advices(student=student_id)

        return get_paginated_result_and_num_pages(result=advices, page_size=page_size, page=page)

    def get_student_courses(self, student_id, is_current=True, is_all=False, keyword=None,
                            year=None, term=None, page=1, page_size=6):
        courses = self._unit_of_work.students_courses. \
            get_student_courses(student=student_id, is_current=is_current, is_all=is_all,
                                keyword=keyword, year=year, term=term)

        if is_all:
            return get_paginated_result_and_num_pages(result=courses, page_size=page_size, page=page)

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
        student = self._unit_of_work.students.get_one(student_id)

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

    def get_review_forms(self, request_data=None):

        review_items = self._unit_of_work.review_items.get_all()

        review_form = StudentReviewForm(request_data, review_items=review_items)

        return review_form

    @transaction.atomic
    def add_review(self, student_id, educator_id, review_form):

        student = self._unit_of_work.students.get_one(student_id)

        educator = self._unit_of_work.educators.get_one(educator_id)

        review_items = review_form.review_items

        review = review_form.save(commit=False)
        review.student = student
        review.student_year = student.year
        review.educator = educator
        review.save()

        for item in review_items:
            saved_item = item.save(commit=False)
            saved_item.student_review = review
            saved_item.save()
