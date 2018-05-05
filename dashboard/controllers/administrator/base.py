from django.contrib.auth.mixins import UserPassesTestMixin

from dashboard.controllers.base import BaseView, PaginatorBaseView, is_group_exist

administrators_group = 'administrators'


class AdministratorBaseView(UserPassesTestMixin, BaseView):

    def test_func(self):
        return is_group_exist(self.request.user, administrators_group)


class AdministratorPaginatorBaseView(UserPassesTestMixin, PaginatorBaseView):

    def test_func(self):
        return is_group_exist(self.request.user, administrators_group)
