from django import forms
from .models import Record
from django.forms import TypedChoiceField
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
  
  Large_Fruit = forms.ChoiceField(
    label = 'Large Fruit',
    choices=Record.QUANTITYS,
    widget=forms.Select(
      attrs={
        'class': 'form-select form-select-sm',
      }
    )
  )

  Medium_Fruit = forms.ChoiceField(
    label = 'Medium Fruit',
    choices=Record.QUANTITYS,
    widget=forms.Select(
      attrs={
        'class': 'form-select form-select-sm',
      }
    )
  )

  Small_Fruit = forms.ChoiceField(
    label = 'Small Fruit',
    choices=Record.QUANTITYS,
    widget=forms.Select(
      attrs={
        'class': 'form-select form-select-sm',
      }
    )
  )

  Parfait = forms.ChoiceField(
    label = 'Parfait',
    choices=Record.QUANTITYS,
    widget=forms.Select(
      attrs={
        'class': 'form-select form-select-sm',
      }
    )
  )

  Grilled_Wrap = forms.ChoiceField(
    label = 'Grilled Wrap',
    choices=Record.QUANTITYS,
    widget=forms.Select(
      attrs={
        'class': 'form-select form-select-sm',
      }
    )
  )

  Spicy_Wrap = forms.ChoiceField(
    label = 'Spicy Wrap',
    choices=Record.QUANTITYS,
    widget=forms.Select(
      attrs={
        'class': 'form-select form-select-sm',
      }
    )
  )

  Kale_Salad = forms.ChoiceField(
    label = 'Kale Salad',
    choices=Record.QUANTITYS,
    widget=forms.Select(
      attrs={
        'class': 'form-select form-select-sm',
      }
    )
  )

  Market_Salad = forms.ChoiceField(
    label = 'Market Salad',
    choices=Record.QUANTITYS,
    widget=forms.Select(
      attrs={
        'class': 'form-select form-select-sm',
      }
    )
  )

  Southwest_Salad = forms.ChoiceField(
    label = 'Southwest Salad',
    choices=Record.QUANTITYS,
    widget=forms.Select(
      attrs={
        'class': 'form-select form-select-sm',
      }
    )
  )

  Cobb_Salad = forms.ChoiceField(
    label = 'Cobb Salad',
    choices=Record.QUANTITYS,
    widget=forms.Select(
      attrs={
        'class': 'form-select form-select-sm',
      }
    )
  )

  Side_Salad = forms.ChoiceField(
    label = 'Side Salad',
    choices=Record.QUANTITYS,
    widget=forms.Select(
      attrs={
        'class': 'form-select form-select-sm',
      }
    )
  )

  date = forms.DateField(
    label = 'Date',
    widget=forms.DateInput(
      attrs={
        'class': 'form-control form-control-sm',
        'type': 'date',
      }
    )
  )

  class Meta:
    model = Record
    fields = ['Large_Fruit', 'Medium_Fruit', 'Small_Fruit', 'Parfait', 'Grilled_Wrap', 'Spicy_Wrap', 'Kale_Salad', 'Market_Salad', 'Southwest_Salad', 'Cobb_Salad', 'Side_Salad', 'date']


# ? - Update Record
class UpdateRecordForm(forms.ModelForm):
  class Meta:
    model = Record
    fields = ['Large_Fruit', 'Medium_Fruit', 'Small_Fruit', 'Parfait', 'Grilled_Wrap', 'Spicy_Wrap', 'Kale_Salad', 'Market_Salad', 'Southwest_Salad', 'Cobb_Salad', 'Side_Salad']