from django.db.models import Count, Q

from dashboard.models import *
from .repo import Repo


class StudentCourseRepo(Repo):
    def __init__(self):
        super().__init__(StudentCourse)

    def get_student_courses(self, student, is_current=True, is_all=False, keyword=None,
                            year=None, term=None):

        filters = {
            'student': student
        }

        if year:
            filters['course__year'] = year

        if term:
            filters['course__term'] = term

        if keyword:
            filters['course__name__icontains'] = keyword

        courses = self._model.objects.filter(**filters).order_by('-created_at')

        if is_all:
            courses = courses.select_related('course', 'course__year', 'course__term', 'educator')

        else:
            courses = courses.exclude(final_grade__isnull=not is_current)

        return courses

    def get_educator_students(self, educator, keyword=None):

        filters = {
            'educator': educator
        }

        if keyword:
            filters['student__name__icontains'] = keyword

        students = self._model.objects.filter(**filters) \
            .values('student', 'student__name', 'student__department', 'student__department__name',
                    'course', 'course__name', 'course__year', 'course__year__name', 'final_grade',
                    'midterm_grade', 'prediction_grade').order_by('-created_at').exclude(final_grade__isnull=False)

        return students

    def get_educator_students_counts(self, educator, department=None, year=None, term=None):

        filters = {
            'educator': educator
        }

        if department:
            filters['student__department'] = department

        if year:
            filters['course__year'] = year

        if term:
            filters['course__term'] = term

        midterm_pass = Count('midterm_grade', filter=Q(midterm_grade__gte=50))
        final_pass = Count('final_grade', filter=Q(final_grade__gte=50))

        counts = self._model.objects.exclude(final_grade__isnull=True).filter(**filters). \
            values('course', 'course__name') \
            .annotate(midterm_pass=midterm_pass, final_pass=final_pass, total=Count('course'))

        return counts

    def get_courses_success_fail_counts(self, department=None, year=None, term=None):

        filters = {
        }

        if department:
            filters['student__department'] = department

        if term:
            filters['course__term'] = term

        if year:
            filters['course__year'] = year

        years_counts = self._model.objects.exclude(final_grade__isnull=True) \
            .filter(**filters) \
            .extra(select={'year': "EXTRACT(year FROM created_at)"}) \
            .values('year') \
            .annotate(success=Count('final_grade', filter=Q(final_grade__gte=50)),
                      fail=Count('final_grade', filter=Q(final_grade__lt=50)))

        return years_counts
