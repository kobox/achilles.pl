# -*- coding: utf-8 -*-
__author__ = 'ko'

from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions


class SubscribeForm(forms.Form):
    #imie = forms.CharField(max_length=30)
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super(SubscribeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.form_show_labels = False
        self.helper.layout = Layout(
            Field('email'),
            )

    class Meta:
        fields = ['email']
    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass