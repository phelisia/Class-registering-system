from dataclasses import fields
from pyexpat import model
from django import forms
from. models import Members


class Members_registsration_form(forms.ModelForm):
    class Meta:
        model=Members
        fields="__all__"
        Widgets={}
