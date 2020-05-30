from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from student.views import generate_student
from user_account.views import CreateUserAccountView, SuccessRegistrationView

app_name = 'user_account'

urlpatterns = [
    path('register/', CreateUserAccountView.as_view(), name='registration'),
    path('success-registration/', SuccessRegistrationView.as_view(), name='success-registration'),

]
