from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    living = forms.IntegerField(max_value=100)


    class Meta:
        model = User
        fields = ['username','email','living','password1','password2']