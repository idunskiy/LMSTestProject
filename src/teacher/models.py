import datetime

from django.db import models

# Create your models here.
class Teacher(models.Model):
    first_name = models.CharField(max_length=40, null=False)
    last_name = models.CharField(max_length=20, null=False)
    email = models.CharField(max_length=50)
    birthdate = models.DateField(default=datetime.datetime.now().date())