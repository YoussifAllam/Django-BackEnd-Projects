from django.forms import ModelForm
from .models import CarPhoto

class CarPhotoForm(ModelForm):
    class Meta:
        model = CarPhoto
        fields = ['photo']

from django.forms import inlineformset_factory
from .models import Cars_Info, CarPhoto
from .forms import CarPhotoForm

CarPhotoFormSet = inlineformset_factory(Cars_Info, CarPhoto, form=CarPhotoForm, extra=3)

# cars/forms.py
from django import forms
from .models import Cars_Info

class CarsInfoForm(forms.ModelForm):
    class Meta:
        model = Cars_Info
        fields = '__all__'  # Adjust this based on the fields you want to include in the form

