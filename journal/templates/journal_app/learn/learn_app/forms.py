from django import forms
from learn_app.models import Employee
from django.contrib.auth.models import User
from learn_app.models import UserProfile

class EmpForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'


class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        fields=('username','email','password')

class UserProfileForm(forms.ModelForm):
    class Meta():
        model=UserProfile
        fields=('portfolio','pic')
