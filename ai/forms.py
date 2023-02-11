from django import forms
from datetime import timedelta


class DurationChoiceField(forms.ChoiceField):
    def __init__(self, *args, **kwargs):
        kwargs['choices'] = [
            (timedelta(minutes=10), '10 minutes'),
            (timedelta(minutes=15), '15 minutes'),
            (timedelta(minutes=20), '20 minutes'),
            (timedelta(minutes=25), '25 minutes'),
            (timedelta(minutes=30), '30 minutes'),
            (timedelta(minutes=45), '45 minutes'),
        ]
        super().__init__(*args, **kwargs)


class CreateAiForm(forms.Form):
    SKILL_LEVELS = [
        ('novice', 'Novice'),
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    ]
    skill_level = forms.ChoiceField(choices=SKILL_LEVELS)

    duration = DurationChoiceField()
    instructions = forms.BooleanField(label="Instructions", required=False)
    audio = forms.BooleanField(label="Instructions Audio", required=False)
    images = forms.BooleanField(label="Pose Images", required=False)
    video = forms.BooleanField(label="Pose Video", required=False)
    name = forms.CharField(label="Session Name", max_length=100)
