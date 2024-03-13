from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

# ? - Register/Create User
class CreateUserForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'password1', 'password2']

# ? - Login user
class LoginForm(AuthenticationForm):
  username = forms.CharField(widget=TextInput())
  password = forms.CharField(widget=PasswordInput())