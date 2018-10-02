from django import forms
from django.contrib.auth.models import User
from .models import *


class UserForm(forms.Form):
    username = forms.CharField(label='username', max_length=100)
    password = forms.CharField(label='password',widget=forms.PasswordInput(attrs={'class': "input100"}))