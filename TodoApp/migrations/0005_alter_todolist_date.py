# Generated by Django 3.2.15 on 2022-10-03 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TodoApp', '0004_alter_todolist_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='date',
            field=models.DateField(default='10-03-2022'),
        ),
    ]
