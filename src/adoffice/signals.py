# -*- coding: utf-8 -*-
from django.db.models.signals import post_save
from django.dispatch import receiver
import logging
from models import Quota
from django.core.mail import send_mail
from django.utils.translation import ugettext, ugettext_lazy as _
logger = logging.getLogger("project")


@receiver(post_save, sender=Quota)
def create_quote_handler(sender, **kwargs):
    print('Stored: {}'.format(kwargs['instance'].__dict__))
    #if not created:
     #   return
    if kwargs['instance'].email:
        message = _("Zapytanie strona www").format(kwargs['instance'])
        subject = _(u"Autoresponder ze strony Achilles Polska")
        send_mail(subject, message, "no-replay@achilles.pl", ["tio@notowany.pl", ])
    #print('Stored: {}'.format(kwargs['instance'].__dict__))
    logger.info('New quota {} created'.format(kwargs['instance']))
