from django.db import models

# Create your models here.
from faker import Faker

from teacher.models import Teacher


class Group(models.Model):
    group_name = models.CharField(max_length=40, null=False)
    group_specialization = models.CharField(max_length=40, null=False)
    teacher_id = models.ForeignKey(to=Teacher, null=True, on_delete=models.SET_NULL)

    @classmethod
    def generate_group(cls, group_name, group_specialization):
        group = cls(
            group_name=group_name,
            group_specialization=group_specialization
        )
        group.save()
        return group

    def __str__(self):
        return f"{self.group_name}, {self.group_specialization}"
