# -*- coding: utf-8 -*-
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
import logging
from . import models
from django.core.mail import send_mail

logger = logging.getLogger("project")


@receiver(post_save, sender=models.SignUp)
def create_order_handler(sender, instance, created, **kwargs):
    #if not created:
     #   return
    if instance.email:
        message = "Nowe zamówienie wzornika uszlachetnień ".format(instance)
        subject = "Nowe zamówienie wzornika"
        send_mail(subject, message, "foliowanie@achilles.pl", ["tio@notowany.pl", ])

    logger.info('New order {} created'.format(instance))
