# Generated by Django 2.2.3 on 2020-06-10 17:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0007_auto_20200527_0723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='birthdate',
            field=models.DateField(default=datetime.date(2020, 6, 10)),
        ),
    ]
