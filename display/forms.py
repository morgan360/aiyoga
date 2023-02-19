from django import forms
from .models import YogaImage


class ImageForm(forms.Form):
    yoga_image = forms.ModelChoiceField(queryset=YogaImage.objects.all())
