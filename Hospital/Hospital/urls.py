"""
URL configuration for Hospital project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from .import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('base', views.BASE, name='base'),
    path('Patient/add/', views.Add_Patient, name='add_patient'),
    path('all_patients/', views.all_patients, name='all_patients'),
    path('Doctor/add/', views.Add_Doctor, name='add_doctor'),
    path('all_doctors/', views.all_doctors, name='all_doctors'),
    path('Citas/add/', views.Add_Citas,  name='add_citas'),
    path('buscar_paciente/', views.buscar_paciente, name='buscar_paciente'),
]

