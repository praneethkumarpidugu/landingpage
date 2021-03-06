__author__ = 'praneethkumar'
from django import forms

from .models import PersonalInfo

class ContactForm(forms.Form):
    full_name = forms.CharField(required=False)
    email = forms.EmailField()
    message = forms.CharField()

class PersonalInfoForm(forms.ModelForm):

    class Meta:
        model = PersonalInfo
        fields = ['full_name', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split('@')
        domain, extension = provider.split('.')
        if not domain == 'gmail':
            raise forms.ValidationError("Please make sure you use your USC email")
        if not extension == 'com':
            raise forms.ValidationError("Please use a valid .EDU email address")
        return email

    def clean_full_name(self):
        full_name = self.cleaned_data.get('full_name')

        return full_name

