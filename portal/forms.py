from django import forms
from django.forms import fields
from .models import Inform, models


class Dataform(forms.ModelForm):
    class Meta:
        model = Inform
        fields = ('description', 'file')
