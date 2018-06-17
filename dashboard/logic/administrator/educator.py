from dashboard.forms.educator_form import EducatorForm
from dashboard.logic.logic import Logic
from dashboard.logic.utilities import get_paginated_result_and_num_pages


class AdministratorEducatorLogic(Logic):

    def get_educators(self, keyword=None, page=1, page_size=6):
        educators = self._unit_of_work.educators.get_all(keyword=keyword)

        return get_paginated_result_and_num_pages(result=educators, page_size=page_size, page=page)

    def get_educators_rating(self, department_id=None, year_id=None):
        rating = self._unit_of_work.students_review_items.get_educators_rating(department=department_id,
                                                                               year=year_id)

        return rating

    def get_educator_accounts(self, educator_id):
        accounts = self._unit_of_work.accounts.get_educator_accounts(educator=educator_id)

        return accounts

    def get_educator_form(self, educator_id=None, request_data=None, request_files=None):

        educator, educator_accounts = None, self._unit_of_work.educators_accounts.get_none()

        if educator_id:
            educator = self._unit_of_work.educators.get_one(educator_id)

            educator_accounts = self._unit_of_work.educators_accounts. \
                get_educator_accounts(educator=educator_id)

        accounts = self._unit_of_work.accounts.get_all()

        educator_not_accounts = []

        accounts_dict = {}

        for account in accounts:
            educator_has_account = False
            for educator_account in educator_accounts:
                if account == educator_account.account:
                    educator_has_account = True
                    break
            accounts_dict[account.id] = {
                'name': account.name,
                'logo': account.logo
            }

            if not educator_has_account:
                educator_not_accounts.append({'account': account.id})

        educator_form = EducatorForm(request_data, request_files,
                                     instance=educator, accounts=accounts_dict,
                                     educator_accounts=educator_accounts,
                                     educator_not_accounts=educator_not_accounts)

        return educator_form

    @staticmethod
    def update_educator(educator_id, educator_form, accounts_formset):

        educator_form.save()

        instances = accounts_formset.save(commit=False)

        for instance in instances:
            instance.educator_id = educator_id
            instance.save()

        for instance in accounts_formset.deleted_objects:
            instance.delete()

    def add_educator(self, user_form, educator_form, accounts_formset):

        user = user_form.save()

        educator = educator_form.save(commit=False)
        educator.user_id = user.id
        educator.save()

        educators_group = self._unit_of_work.groups.get_group_by_name('educators')
        user.groups.add(educators_group)

        instances = accounts_formset.save(commit=False)

        for instance in instances:
            instance.educator_id = user.id
            instance.save()

        return user.id

    def close_report(self, review_id):
        self._unit_of_work.reports.set_closed(review_id)

    def delete_review(self, review_id):
        self._unit_of_work.students_reviews.delete(review_id)
