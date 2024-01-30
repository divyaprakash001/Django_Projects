from django.urls import path,include
from divya import views

urlpatterns = [
    path('',views.index,name='home'),
]
