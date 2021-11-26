from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.del_connect_home, name='home'),
    path('insert/', views.job_form, name='job_form'),
    path('list/', views.job_list, name='job_list'),
    
    ]

