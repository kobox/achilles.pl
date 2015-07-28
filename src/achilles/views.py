from django.views import generic
from adoffice.models import Category
from packaging.models import Category as PackagingCategory


class HomePage(generic.TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['office'] = Category.objects.filter(active=True, segment=1).order_by('order')
        context['packaging'] = Category.objects.filter(active=True, segment=2).order_by('order')
        context['services'] = Category.objects.filter(active=True, segment=3).order_by('order')

        return context


class AboutPage(generic.TemplateView):
    template_name = "about.html"
    

