from django.views.generic import ListView
from django.views.generic.detail import SingleObjectMixin
from .models import Category


class CategoryDetail(SingleObjectMixin, ListView):
    paginate_by = 2
    template_name = "category_detail.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Category.objects.all())
        return super(CategoryDetail, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CategoryDetail, self).get_context_data(**kwargs)
        context['category'] = self.object
        return context

    def get_queryset(self):
        return self.object.products.all()
