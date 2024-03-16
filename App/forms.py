from django import forms
from .models import Record
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

# ? - Add Record
class AddRecordForm(forms.ModelForm):
  class Meta:
    model = Record
    fields = ['Large_Fruit', 'Medium_Fruit', 'Small_Fruit', 'Parfait', 'Grilled_Wrap', 'Spicy_Wrap', 'Kale_Salad', 'Market_Salad', 'Southwest_Salad', 'Cobb_Salad', 'Side_Salad']

# ? - Update Record
class UpdateRecordForm(forms.ModelForm):
  class Meta:
    model = Record
    fields = ['Large_Fruit', 'Medium_Fruit', 'Small_Fruit', 'Parfait', 'Grilled_Wrap', 'Spicy_Wrap', 'Kale_Salad', 'Market_Salad', 'Southwest_Salad', 'Cobb_Salad', 'Side_Salad']