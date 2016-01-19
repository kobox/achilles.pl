from __future__ import unicode_literals
from django import forms
from .models import Quota
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from django.contrib.auth import get_user_model


# Quota is stored in database
class SignUpForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(
            Submit('submit', 'Zamawiam',
                   css_class="btn btn-lg btn-primary btn-block"),
            )

    class Meta:
        model = Quota
        fields = ['email', 'full_name', 'company', 'phone', 'note', 'newsletter']
