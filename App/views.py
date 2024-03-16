from .models import Record
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from .forms import CreateUserForm, LoginForm, AddRecordForm, UpdateRecordForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

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
      return redirect('login')

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
        return redirect('dashboard')

  context = {'form': form}

  return render(request, 'App/login.html', context=context)

# ? - Logout user
def logout(request):
  auth.logout(request)
  return redirect('login')

# ? Dashboard
@login_required(login_url='login')
def dashboard(request):
  my_records = Record.objects.all()
  context = {'records': my_records}

  return render(request, 'App/dashboard.html', context=context)

# ? Individual Record
@login_required(login_url='login')
def upload_record(request, record_id):
  # Lógica para obtener y mostrar el registro con el ID dado
  record = Record.objects.get(id=record_id)
  context = {'record': record}

  return render(request, 'App/upload-record.html', context=context)

def mark_completed(request):
  if request.method == 'POST':
    completed_products_ids = request.POST.getlist('completed_products')
    # Marcar los productos como completados en la base de datos
    for product_id in completed_products_ids:
      product = Record.objects.get(id=product_id)
      product.done = True
      product.save()
  return redirect('dashboard')

@login_required(login_url='login')
def create_record(request):
  form = AddRecordForm()

  if request.method == 'POST':
    form = AddRecordForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('dashboard')
    
  context = {'form': form}

  return render(request, 'App/create-record.html', context=context)