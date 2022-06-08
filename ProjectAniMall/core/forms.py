from django import forms
from django.forms import ModelForm
from .models import comidagatos

class comidagatoform(ModelForm):
    class Meta:
        model = comidagatos
        fields='__all__'