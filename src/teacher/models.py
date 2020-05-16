import datetime

from django.core.validators import RegexValidator
from django.db import models


# Create your models here.
from django.forms import CharField
from faker import Faker
from phonenumber_field.modelfields import PhoneNumberField


class Teacher(models.Model):
    first_name = models.CharField(max_length=40, null=False)
    last_name = models.CharField(max_length=20, null=False)
    email = models.CharField(max_length=50)
    birthdate = models.DateField(default=datetime.datetime.now().date())
    phone_number = models.CharField(max_length=50, name='phone_number', null=True)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.birthdate}, {self.email}"

    @classmethod
    def generate_teacher(cls):
        faker = Faker()
        teacher = cls(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            email=faker.email(),
            phone_number=str(faker.phone_number()),
        )
        teacher.save()
        return teacher
