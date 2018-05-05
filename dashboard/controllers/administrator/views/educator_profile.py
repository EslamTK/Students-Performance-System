from django.shortcuts import render, redirect

from dashboard.controllers.administrator.base import AdministratorBaseView, \
    AdministratorPaginatorBaseView
from dashboard.logic import *


class AdministratorEducatorProfileView(AdministratorBaseView):
    template_name = 'administrator/educators/educator_profile.html'
    form_template_name = 'administrator/educators/forms/educator_profile.html'

    def get(self, request, user_id, educator_id=None):

        # Educator Form
        educator_form = administrator.get_educator_form(educator_id=educator_id)

        # Educator Accounts Formset
        accounts_formset = educator_form.accounts_formset

        user_form, educator_rating, educator_reviews_years, educator_reviews_departments, \
        educator_reviews, educator_reviews_num_pages = None, None, None, None, None, None

        if educator_id:
            # Educator Reviews Rating
            educator_rating = educator.get_educator_rating(educator_id=educator_id)

            # Educator Reviews Years
            educator_reviews_years = educator.get_educator_reviews_years(educator_id=educator_id)

            # Educator Reviews Departments
            educator_reviews_departments = educator.get_educator_reviews_departments(educator_id=educator_id)

            # Educator Reviews
            educator_reviews, educator_reviews_num_pages = educator.get_educator_reviews(educator_id=educator_id)

        else:
            # User From
            user_form = administrator.get_user_form()

        result = {
            'user_form': user_form,
            'educator_id': educator_id,
            'educator_form': educator_form,
            'educator_accounts_form': accounts_formset,
            'educator_reviews': educator_reviews,
            'educator_reviews_num_pages': educator_reviews_num_pages,
            'educator_rating': educator_rating,
            'educator_reviews_years': educator_reviews_years,
            'educator_reviews_departments': educator_reviews_departments
        }

        return render(request, self.template_name, result)

    def post(self, request, user_id, educator_id=None):

        template_to_render = self.template_name

        user_form = None

        if educator_id:
            educator_form = administrator.get_educator_form(request_data=request.POST,
                                                            request_files=request.FILES,
                                                            educator_id=educator_id)

            accounts_formset = educator_form.accounts_formset

            if educator_form.is_valid() and accounts_formset.is_valid():
                administrator.update_educator(educator_id=educator_id, educator_form=educator_form,
                                              accounts_formset=educator_form.accounts_formset)

            template_to_render = self.form_template_name

        else:
            user_form = administrator.get_user_form(request_data=request.POST)
            educator_form = administrator.get_educator_form(request_data=request.POST,
                                                            request_files=request.FILES)
            accounts_formset = educator_form.accounts_formset

            if user_form.is_valid() and educator_form.is_valid() and accounts_formset.is_valid():
                educator_id = administrator.add_educator(user_form=user_form, educator_form=educator_form,
                                                         accounts_formset=accounts_formset)

                return redirect(to='dashboard:administrator_educator_profile', educator_id=educator_id)

        result = {
            'educator_id': educator_id,
            'educator_form': educator_form,
            'educator_accounts_form': accounts_formset,
            'user_form': user_form
        }

        return render(request, template_to_render, result)


class AdministratorEducatorReviewsPaginatorView(AdministratorPaginatorBaseView):
    template_name = 'administrator/educators/pagination/educator_profile.html'

    def get(self, request, user_id, page, page_size, educator_id):
        # Educator Reviews
        educator_reviews, educator_reviews_num_pages = \
            educator.get_educator_reviews(educator_id=educator_id, page=page, page_size=page_size)

        result = {
            'educator_reviews': educator_reviews,
            'educator_reviews_num_pages': educator_reviews_num_pages
        }

        return render(request, self.template_name, result)
