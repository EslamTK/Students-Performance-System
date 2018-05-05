from django.contrib.auth.mixins import UserPassesTestMixin

from dashboard.controllers.base import BaseView, PaginatorBaseView, is_group_exist

educators_group = 'educators'


class EducatorBaseView(UserPassesTestMixin, BaseView):

    def test_func(self):
        return is_group_exist(self.request.user, educators_group)


class EducatorPaginatorBaseView(UserPassesTestMixin, PaginatorBaseView):

    def test_func(self):
        return is_group_exist(self.request.user, educators_group)
