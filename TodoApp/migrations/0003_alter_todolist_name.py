# Generated by Django 3.2.15 on 2022-10-03 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TodoApp', '0002_alter_todolist_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='name',
            field=models.CharField(default='My task..', max_length=150),
        ),
    ]
