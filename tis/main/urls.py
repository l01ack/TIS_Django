from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about_us', views.about, name='about'),
    path('Registration', views.Registration, name='Registration'),
    path('testing', views.test, name='test'),
    path('results', views.Results, name='results')
]
