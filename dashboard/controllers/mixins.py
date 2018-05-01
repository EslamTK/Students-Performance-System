from django.contrib.auth.mixins import UserPassesTestMixin


def is_group_exist(user, group):
    return user.groups.filter(name=group).exists()


class StudentPassesTestMixin(UserPassesTestMixin):
    students_group = 'students'

    def test_func(self):
        return is_group_exist(self.request.user, self.students_group)


class EducatorPassesTestMixin(UserPassesTestMixin):
    educators_group = 'educators'

    def test_func(self):
        return is_group_exist(self.request.user, self.educators_group)
