from django.db import models

# Create your models here.


class Group(models.Model):
    group_name = models.CharField(max_length=40, null=False)
    group_specialization = models.CharField(max_length=40, null=False)

    def __str__(self):
        return f"{self.group_name}, {self.group_specialization}"
