from django import forms
from .models import MailForSend

class MailForm(forms.ModelForm):

    class Meta:
        model = MailForSend
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames'
        fields = ('mailer', 'subject', 'text', 'sec_to_send')
