from django.db import models

# Create your models here.
from faker import Faker


class Group(models.Model):
    group_name = models.CharField(max_length=40, null=False)
    group_specialization = models.CharField(max_length=40, null=False)

    @classmethod
    def generate_group(cls, group_name, group_specialization):
        group = cls(
            group_name = group_name,
            group_specialization = group_specialization
        )
        group.save()
        return group

    def __str__(self):
        return f"{self.group_name}, {self.group_specialization}"
