from django.contrib.auth.models import User
from django.urls import reverse
from django.views.generic import CreateView, TemplateView
from django.views.generic.edit import BaseFormView

from user_account.forms import UserAccountRegistrationForm


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
