from django.core.paginator import Paginator


def convert_boolean_to_yes_no(value):
    if value:
        return 'yes'
    return 'no'


def get_paginated_result_and_num_pages(result, page_size, page):
    paginator = Paginator(result, page_size)

    result = paginator.get_page(page)

    return result, paginator.num_pages
