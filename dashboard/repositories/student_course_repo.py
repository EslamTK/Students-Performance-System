from django.db.models import Count, Q

from dashboard.models import *
from .repo import Repo


class StudentCourseRepo(Repo):
    def __init__(self):
        super().__init__(StudentCourse)

    def get_student_courses(self, student, is_current=True, is_all=False):

        courses = StudentCourse.objects.filter(student=student) \
            .order_by('-course__year', 'course__term')

        if is_all or not is_current:
            courses = courses.select_related('course', 'course__year', 'course__term', 'educator')

        if not is_all:
            courses = courses.exclude(final_grade__isnull=not is_current)

        return courses

    def get_educator_students(self, educator):

        students = StudentCourse.objects.filter(educator=educator) \
            .values('student', 'student__name', 'student__department', 'student__department__name',
                    'course', 'course__name', 'course__year', 'course__year__name', 'final_grade',
                    'prediction_grade').order_by('-created_at')

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

        counts = StudentCourse.objects.filter(**filters). \
            values('course', 'course__name') \
            .annotate(midterm_pass=midterm_pass, final_pass=final_pass, total=Count('course'))

        return counts
