from django.views import generic
from adoffice.models import Category


class HomePage(generic.TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['office'] = Category.objects.filter(active=True).order_by('order')
        return context


class AboutPage(generic.TemplateView):
    template_name = "about.html"

