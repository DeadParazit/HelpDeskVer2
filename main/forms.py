from django import forms
from django.forms.widgets import *
from main.models import Request

class AuthorizeForm(forms.Form):
    user_id = forms.CharField(label='user_id', max_length=100)
    password = forms.CharField(label='password', max_length=100)

