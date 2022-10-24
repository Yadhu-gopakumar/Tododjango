
from django import forms
from . models import Todolist

class Todoform(forms.ModelForm):
    class Meta:
        model=Todolist
        fields = ['name','date','priority']
