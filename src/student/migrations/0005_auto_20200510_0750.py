# Generated by Django 3.0.5 on 2020-05-10 07:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_auto_20200509_0812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='birthdate',
            field=models.DateField(default=datetime.datetime(2020, 5, 10, 7, 50, 34, 652441)),
        ),
    ]