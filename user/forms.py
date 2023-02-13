from allauth.account.forms import SignupForm as AccountSignupForm
from allauth.socialaccount.forms import SignupForm
from django import forms
from django.contrib.auth.models import Group
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field


# Social Registration
class SocialSignupForm(SignupForm):
    GROUPS = (
        ('novice', 'Novice'),
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    )
    group = forms.ChoiceField(choices=GROUPS)

    # mobile = forms.CharField(max_length=30, label='Mobile')

    def __init__(self, *args, **kwargs):
        super(SocialSignupForm, self).__init__(*args, **kwargs)

    def save(self, request):
        user = super(SocialSignupForm, self).save(request)
        # user.mobile_phone = self.cleaned_data['mobile']
        user.group = self.cleaned_data['group']
        g = Group.objects.get(name=user.group)
        g.user_set.add(user)
        user.save()
        return user


# Regular sign-up
class CustomSignupForm(AccountSignupForm):
    GROUPS = (
        ('novice', 'Novice'),
        ('beginner', 'Beginner'),
        ('intermediate', 'Intermediate'),
        ('advanced', 'Advanced'),
    )
    group = forms.ChoiceField(choices=GROUPS, label='Your Level of Yoga')
    first_name = forms.CharField(max_length=30, label='First Name', required=False, )
    last_name = forms.CharField(max_length=30, label='Last Name', required=False, )

    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)

        # super().__init__(*args, **kwargs)
        # self.fields['mobile'].widget.attrs.update({
        #     'class': 'red-border'
        # })

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.group = self.cleaned_data['group']
        g = Group.objects.get(name=user.group)
        g.user_set.add(user)
        user.save()
        return user
