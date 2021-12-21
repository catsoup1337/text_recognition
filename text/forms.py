from django.forms import ModelForm
from .models import Image
from django import forms

class ImageForm(ModelForm):
    class Meta:
        model = Image
        fields = ['image']

class SearchForm(forms.Form):
    search = forms.CharField(max_length=5)