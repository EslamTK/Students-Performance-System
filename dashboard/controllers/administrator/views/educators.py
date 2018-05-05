import json

from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render

from dashboard.controllers.administrator.base import AdministratorBaseView, \
    AdministratorPaginatorBaseView
from dashboard.logic import *


class AdministratorEducatorsView(AdministratorBaseView):
    template_name = 'administrator/educators/educators_performance.html'

    def get(self, request, user_id):
        # Departments
        departments = general.get_departments()

        # Years
        years = general.get_years()

        # Educators
        educators_list, educators_num_pages = administrator.get_educators()

        # Educators Rating
        educators_rating = administrator.get_educators_rating()
        educators_rating = json.dumps(list(educators_rating), cls=DjangoJSONEncoder)

        result = {
            'departments': departments,
            'years': years,
            'educators': educators_list,
            'educators_num_pages': educators_num_pages,
            'educators_rating': educators_rating
        }

        return render(request, self.template_name, result)


class AdministratorEducatorsPaginatorView(AdministratorPaginatorBaseView):
    template_name = 'administrator/educators/pagination/educators_performance.html'

    def get(self, request, user_id, page, page_size):
        # Getting the search keyword
        keyword = request.GET.get('keyword')

        # Students
        educators_list, educators_num_pages = administrator.get_educators(keyword=keyword,
                                                                          page=page,
                                                                          page_size=page_size)

        result = {
            'educators': educators_list,
            'educators_num_pages': educators_num_pages,
        }

        return render(request, self.template_name, result)
