"""SETI URL Configuration

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
from Project6.views import *
urlpatterns = [
    path('', index, name='index'),
    path('createCity', createCity, name='createCity'),
    path('deleteCity/<int:id>', deleteCity, name="deleteCity"),
    path('updateCity/<int:id>/', updateCity, name="updateCity"),

    path('deleteHuman/<int:id>', deleteHuman, name="deleteHuman"),
    path('updateHuman/<int:id>/', updateHuman, name="updateHuman"),
    path('createHuman', createHuman, name='createHuman'),

    path('deleteReligion/<int:id>', deleteReligion, name="deleteReligion"),
    path('updateReligion/<int:id>/', updateReligion, name="updateReligion"),
    path('createReligion', createReligion, name='createReligion'),

    path('deleteFirm/<int:id>', deleteFirm, name="deleteFirm"),
    path('updateFirm/<int:id>/', updateFirm, name="updateFirm"),
    path('createFirm', createFirm, name='createFirm'),
]
