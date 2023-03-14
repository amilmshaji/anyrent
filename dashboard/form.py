from django import forms
from .models import Productgallery

class ProductgalleryForm(forms.ModelForm):
    class Meta:
        model = Productgallery
        fields = ['image']
