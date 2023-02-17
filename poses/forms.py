# forms.py
from django import forms
from .models import Poses, PoseType


class PoseForm(forms.ModelForm):
    types = forms.ModelMultipleChoiceField(
        queryset=PoseType.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Poses
        fields = ['name', 'description', 'types']
