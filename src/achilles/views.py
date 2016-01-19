from django.views import generic
from adoffice.models import Category, Page
from forms import SubscribeForm
from django.shortcuts import redirect
from django.template.loader import get_template
from django.template import Context
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.utils.translation import ugettext, ugettext_lazy as _


class HomePage(generic.TemplateView):
    template_name = "home.html"

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        if context["form"].is_valid():
            email = context["form"].cleaned_data.get('email')
            message = get_template(settings.BASE_DIR+'/adoffice/templates/emails/subscription-email.html').render(Context({'full_name': email}))
            subject = _(u"Newsletter Achilles Polska")
            msg = EmailMultiAlternatives(subject, '', 'no-replay@achilles.pl', [email])
            msg.attach_alternative(message, "text/html")
            msg.send()
            return redirect('/thanks/')

        return super(generic.TemplateView, self).render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        form = SubscribeForm(self.request.POST or None)
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


class SubscriberPage(generic.TemplateView):
    template_name = "subscribed.html"