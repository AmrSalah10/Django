from django.urls import path, include
from . import views

urlpatterns = [
    path('singup/', views.singup, name='singup'),
]
