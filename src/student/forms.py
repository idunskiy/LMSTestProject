from django.core.exceptions import ValidationError
from django.forms import ModelForm

from student.models import Student


class StudentBaseForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class StudentAddForm(StudentBaseForm):
    pass


class StudentEditForm(StudentBaseForm):

    def clean_email(self):
        email = self.cleaned_data['email']
        if Student.objects.all().filter(email=email).exists() and email != self.initial['email']:
            raise ValidationError('Email already exists.')
        return email

    def clean(self):
        if self.cleaned_data['first_name'] == self.cleaned_data['last_name']:
            raise ValidationError(f"First name and Last name can't be equal.")


class StudentDeleteForm(StudentBaseForm):
    class Meta(StudentBaseForm.Meta):
        fields = []