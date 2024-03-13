from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from .forms import CreateUserForm, LoginForm
from django.shortcuts import render, redirect

# ? - Home page
def home(request):
  return render(request, 'App/index.html')

# ? - Register user
def register(request):
  form = CreateUserForm()
  if request.method == 'POST':
    form = CreateUserForm(request.POST)

    if form.is_valid():
      form.save()
      # return redirect('')

  context = {'form': form}

  return render(request, 'App/register.html', context)

# ? - Login user
def login(request):
  form = LoginForm()
  if request.method == 'POST':
    form = LoginForm(request, data=request.POST)

    if form.is_valid():
      username = request.POST.get('username')
      password = request.POST.get('password')

      user = authenticate(request, username=username, password=password)

      if user is not None:
        auth.login(request, user)
        # return redirect('')

  context = {'form': form}

  return render(request, 'App/login.html', context=context)