from django.db import models

# Create your models here.
from faker import Faker

from teacher.models import Teacher
import random


class Classroom(models.Model):
    name = models.CharField(max_length=64)
    floor = models.SmallIntegerField(max_length=128, null=True)

    @classmethod
    def generate_classroom(cls):
        classroom = cls(
            name=f'Classroom - {random.choice(range(5))}',
            floor=random.choice(range(5))
        )
        classroom.save()
        return classroom

    def __str__(self):
        return f'{self.name} - Floor# {self.floor}'


class Group(models.Model):
    name = models.CharField(max_length=40, null=False)
    specialization = models.CharField(max_length=40, null=False)
    teacher = models.ForeignKey(to=Teacher,
                                null=True,
                                on_delete=models.SET_NULL,
                                related_name='groups')
    classroom = models.ManyToManyField(
        to=Classroom,
        null=True,
        related_name='groups'
    )

    @classmethod
    def generate_group(cls, name, specialization):
        group = cls(
            group_name=name,
            group_specialization=specialization
        )
        group.save()
        return group

    def __str__(self):
        return f"{self.name}, {self.specialization}"
