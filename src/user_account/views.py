from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, TemplateView
from django.views.generic.edit import BaseFormView, UpdateView

from user_account.forms import UserAccountRegistrationForm, UserAccountProfileForm


class CreateUserAccountView(CreateView):
    model = User
    template_name = 'registration.html'
    form_class = UserAccountRegistrationForm

    def get_success_url(self):
        return reverse('user_account:success-registration')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Register new user'
        return context


class SuccessRegistrationView(TemplateView):
    template_name = 'success.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=None, **kwargs)
        context['title'] = 'Successfully created a user'
        return context


class UserAccountLoginView(LoginView):
    template_name = 'login.html'
    extra_context = {'title':'Login as a user'}
    success_url = reverse_lazy('index')


class UserAccountLogoutView(LogoutView):
    template_name = 'logout.html'
    extra_context = {'title':'Logout from LMS'}


class UserAccountProfileView(UpdateView):
    template_name = 'profile.html'
    extra_context = {'title': 'Edit current user profile.'}
    form_class = UserAccountProfileForm

    def get_object(self):
        return self.request.user
