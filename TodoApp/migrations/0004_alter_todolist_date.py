# Generated by Django 3.2.15 on 2022-10-03 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TodoApp', '0003_alter_todolist_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='date',
            field=models.DateField(default='2022-03-10'),
        ),
    ]
