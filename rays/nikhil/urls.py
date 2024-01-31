from django.contrib import admin
from django.urls import path,include
from nikhil import views

urlpatterns = [
    path('', views.index, name='home'),
    path('internship/', views.intern, name='internship'),
    path('dev/', views.application, name='development'),
]
