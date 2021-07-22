"""gui URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import re_path
from firstform import views
import datetime

urlpatterns = [
    path('', views.index, name='home'),
    path('admin/', admin.site.urls),
    
    path('rooms/', views.rooms),
    path('rooms/editRoom/<int:id>/', views.editRoom),
    path('rooms/delete/<int:id>/', views.deleteRoom),
    path('services/', views.services),
    path('services/editService/<int:id>/', views.editService),
    path('services/delete/<int:id>/', views.deleteService),
    path('clients/', views.clients),
    path('clients/editClient/<int:id>/', views.editClient),
    path('clients/delete/<int:id>/', views.deleteClient),
    path('serviceOrder/', views.clientService),
    path('serviceOrder/editClientService/<int:id>/', views.editClientService),
    path('serviceOrder/delete/<int:id>/', views.deleteClientService),
    path('roomOrder/', views.clientRoom),
    path('roomOrder/editClientRoom/<int:id>/', views.editClientRoom),
    path('roomOrder/delete/<int:id>/', views.deleteClientRoom),
    path('report/', views.report),
]
