from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm

from user_account.models import UserAccountProfile


class UserAccountRegistrationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        fields = ("username", 'first_name', 'last_name', 'email')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.all().filter(email = email).exists() and email != self.initial['email']:
            raise ValidationError('Email already exists.')
        return email


class UserAccountProfileForm(UserChangeForm):

    class Meta(UserCreationForm.Meta):
        fields = ("username", 'first_name', 'last_name', 'email')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.all().filter(email = email).exists() and email != self.initial['email']:
            raise ValidationError('Email already exists.')
        return email


class UserProfileUpdateForm(ModelForm):
    class Meta:
        model = UserAccountProfile
        fields = ['image']
