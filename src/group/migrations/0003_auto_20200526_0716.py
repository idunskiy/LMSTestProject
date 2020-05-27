# Generated by Django 3.0.5 on 2020-05-26 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0002_group_teacher_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classroom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('floor', models.SmallIntegerField(max_length=128, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='classroom',
            field=models.ManyToManyField(null=True, related_name='groups', to='group.Classroom'),
        ),
    ]
