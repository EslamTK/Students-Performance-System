from django.views import View


class BaseView(View):

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, user_id=request.user.id, **kwargs)


class PaginatorBaseView(BaseView):

    def dispatch(self, request, *args, **kwargs):
        page = request.GET.get('page', 1)

        page_size = request.GET.get('page_size', 4)

        return super().dispatch(request, *args, page=page, page_size=page_size, **kwargs)


def is_group_exist(user, group):
    return user.groups.filter(name=group).exists()
