import datetime
from builtins import classmethod

from django.db import models

# Create your models here.
from django.forms import CharField
from faker import Faker

from group.models import Group


class Student(models.Model):
    first_name = models.CharField(max_length=40, null=False)
    last_name = models.CharField(max_length=20, null=False)
    email = models.CharField(max_length=50)
    birthdate = models.DateField(default=datetime.datetime.now())
    phone_number = models.CharField(max_length=40, name='phone_number', null=True)
    group = models.ForeignKey(to=Group, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}, {self.birthdate}," \
            f" {self.email}, {self.phone_number}"

    @classmethod
    def generate_student(cls):
        faker = Faker()
        student = cls(
            first_name=faker.first_name(),
            last_name=faker.last_name(),
            email=faker.email(),
            phone_number=str(faker.phone_number()),
        )
        student.save()
        return student
