# Generated by Django 3.0.5 on 2020-05-10 12:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0010_auto_20200510_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='phone_number',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='birthdate',
            field=models.DateField(default=datetime.datetime(2020, 5, 10, 12, 18, 29, 987244)),
        ),
    ]