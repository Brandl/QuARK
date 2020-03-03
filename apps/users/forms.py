from django.contrib.auth import get_user_model
from django import forms
from allauth.account.forms import SignupForm
from django_countries.fields import CountryField
from .models import Gender_CHOICES


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    birthdate = forms.DateField(input_formats=['%Y-%m-%d',], required=True, widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    citizenship = CountryField().formfield()
    gender = forms.ChoiceField(choices=Gender_CHOICES, required=True)

    def save(self, request):
        # .save() returns a User object.
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.birthdate = self.cleaned_data['birthdate']
        user.citizenship = self.cleaned_data['citizenship']
        user.gender = self.cleaned_data['gender']
        user.save()
        return user
