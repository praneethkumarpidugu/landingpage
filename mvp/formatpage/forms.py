__author__ = 'praneethkumar'
from django import forms

from .models import PersonalInfo

class PersonalInfoForm(forms.ModelForm):

    class Meta:
        model = PersonalInfo
        fields = ['full_name', 'email']

