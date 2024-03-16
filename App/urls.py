from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),

  path('login', views.login, name='login'),
  path('logout', views.logout, name='logout'),
  path('register', views.register, name='register'),
  path('dashboard', views.dashboard, name='dashboard'),
  path('upload_record/<int:record_id>/', views.upload_record, name='upload_record'),
  path('mark_completed/', views.mark_completed, name='mark_completed'),
]