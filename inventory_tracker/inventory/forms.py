from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class AdminRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['name','email','password1','password2']


