from django.contrib.auth.mixins import UserPassesTestMixin

from dashboard.controllers.base import BaseView, PaginatorBaseView, is_group_exist

students_group = 'students'


class StudentBaseView(UserPassesTestMixin, BaseView):

    def test_func(self):
        return is_group_exist(self.request.user, students_group)


class StudentPaginatorBaseView(UserPassesTestMixin, PaginatorBaseView):

    def test_func(self):
        return is_group_exist(self.request.user, students_group)
