from django.views import generic
from adoffice.models import Category, Page
from forms import ContactForm

class HomePage(generic.TemplateView):
    template_name = "home.html"

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        if context["form"].is_valid():
            print 'Dziekujemy za Twoje zainteresowanie, sprawdz swoja poczte email.'

        return super(generic.TemplateView, self).render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        form = ContactForm(self.request.POST or None)
        context["form"] = form
        context['office'] = Category.objects.filter(active=True, segment=1).order_by('order')
        context['packaging'] = Category.objects.filter(active=True, segment=2).order_by('order')
        context['services'] = Category.objects.filter(active=True, segment=3).order_by('order')
        context['page'] = Page.objects.get(pageclass=1)
        return context


class AboutPage(generic.TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super(AboutPage, self).get_context_data(**kwargs)
        context['page'] = Page.objects.get(pageclass=2)

        return context
    

class ContactPage(generic.TemplateView):
    template_name = "contact.html"

    def get_context_data(self, **kwargs):
        context = super(ContactPage, self).get_context_data(**kwargs)
        context['page'] = Page.objects.get(pageclass=3)

        return context