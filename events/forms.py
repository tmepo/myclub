from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterUserForm(UserCreationForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name=forms.CharField(max_length=20)
    last_name=forms.CharField(max_length=20)
    address=forms.CharField(max_length=30)

    class Meat:
        model=User
        fields=('username','first_name','last_name','email','password1','password2')