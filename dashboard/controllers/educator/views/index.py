from django.shortcuts import render

from dashboard.controllers.educator.base import EducatorBaseView, EducatorPaginatorBaseView
from dashboard.logic import *


class EducatorIndexView(EducatorBaseView):
    template_name = 'educator/index.html'

    def get(self, request, user_id):
        # Educator Reviews Rating
        educator_rating = educator.get_educator_rating(educator_id=user_id)

        # Educator Reviews Years
        educator_reviews_years = educator.get_educator_reviews_years(educator_id=user_id)

        # Educator Reviews Departments
        educator_reviews_departments = educator.get_educator_reviews_departments(educator_id=user_id)

        # Educator Reviews
        educator_reviews, educator_reviews_num_pages = educator.get_educator_reviews(educator_id=user_id)

        result = {
            'educator_rating': educator_rating,
            'educator_reviews_years': educator_reviews_years,
            'educator_reviews_departments': educator_reviews_departments,
            'educator_reviews': educator_reviews,
            'educator_reviews_num_pages': educator_reviews_num_pages
        }

        return render(request, self.template_name, result)


class EducatorReviewsPaginatorView(EducatorPaginatorBaseView):
    template_name = 'educator/pagination/index.html'

    def get(self, request, user_id, page, page_size):
        # Educator Reviews
        educator_reviews, educator_reviews_num_pages = \
            educator.get_educator_reviews(educator_id=user_id, page=page, page_size=page_size)

        result = {
            'educator_reviews': educator_reviews,
            'educator_reviews_num_pages': educator_reviews_num_pages
        }

        return render(request, self.template_name, result)
