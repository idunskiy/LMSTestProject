# Generated by Django 3.0.5 on 2020-05-27 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0004_auto_20200527_0723'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='teacher_id',
            new_name='teacher',
        ),
    ]
