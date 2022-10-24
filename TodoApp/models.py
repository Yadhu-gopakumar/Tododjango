from django.db import models


# Create your models here.
class Todolist(models.Model):
    name = models.CharField(max_length=150)
    date = models.DateField()
    priority = models.IntegerField()

    def __str__(self):
        return self.name
