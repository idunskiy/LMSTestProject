# Generated by Django 3.0.5 on 2020-05-16 11:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0003_teacher_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='birthdate',
            field=models.DateField(default=datetime.date(2020, 5, 16)),
        ),
    ]