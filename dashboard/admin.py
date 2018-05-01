from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(Account)
admin.site.register(Course)
admin.site.register(Term)
admin.site.register(Year)
admin.site.register(Department)
admin.site.register(HomePage)

admin.site.register(Student)
admin.site.register(StudentCourse)
admin.site.register(ReviewItem)
admin.site.register(StudentReview)
admin.site.register(StudentReviewItem)

admin.site.register(Educator)
admin.site.register(EducatorAccount)
admin.site.register(EducatorAdvice)
admin.site.register(Report)
