from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path("", views.index),
    path("create/", views.create),
    # Film
    path('createfilm/',views.MovieCreate.as_view()),
    path('updatefilm/<int:pk>/',views.MovieUpdate.as_view()),
    # Here ID must be pk
    path('deletefilm/<int:pk>/',views.MovieDelete.as_view()),
  
    # 
    path('signup/',views.api_signup),
    path('signin/',obtain_auth_token),
]
