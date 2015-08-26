# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
import uuid
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class BaseProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                primary_key=True)
    slug = models.UUIDField(default=uuid.uuid4, blank=True, editable=False)
    # Add more user profile fields here. Make sure they are nullable
    # or with default values
    picture = models.ImageField(_('Moje logo'),
                                upload_to='profile_pics/%Y-%m-%d/',
                                null=True,
                                blank=True)
    bio = models.BooleanField(_("Artykuły Reklamowe"), default=True, blank=True)
    newsp = models.BooleanField(_("Opakowania i materiały POS"), default=True, blank=True)
    newsl = models.BooleanField(_("Usługi dla Poligrafii"), default=True, blank=True)
    email_verified = models.BooleanField(_("Email zweryfikowany"), default=False)

    class Meta:
        abstract = True


@python_2_unicode_compatible
class Profile(BaseProfile):
    def __str__(self):
        return "{}'s profile". format(self.user)
