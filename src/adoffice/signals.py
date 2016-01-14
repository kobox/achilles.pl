# -*- coding: utf-8 -*-
from django.db.models.signals import post_save
from django.dispatch import receiver
import logging
from models import Quota
from django.core.mail import send_mail
from django.utils.translation import ugettext, ugettext_lazy as _
from django.template.loader import get_template
from django.template import Context
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
logger = logging.getLogger("project")


@receiver(post_save, sender=Quota)
def create_quote_handler(sender, instance, created, **kwargs):
    #if not created:
     #   return
    if instance.email:
        message = get_template(settings.BASE_DIR+'/adoffice/templates/emails/hello-email.html').render(Context({
            'full_name': instance.full_name
        }))
        subject = _(u"Autoresponder ze strony Achilles Polska")
        #send_mail(subject, message, "no-replay@achilles.pl", ["tio@notowany.pl", ])
        msg = EmailMultiAlternatives(subject, '', 'no-replay@achilles.pl', [instance.email])
        msg.attach_alternative(message, "text/html")
        msg.send()
    #print('Stored: {}'.format(kwargs['instance'].__dict__))
    logger.info('New quota {} created'.format(instance))
