from django import forms
from app.models import *


class Studentform(forms.Form):
    sid=forms.IntegerField()
    sname=forms.CharField(max_length=100)
    email=forms.EmailField()