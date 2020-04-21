from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('', include('djoser.urls.jwt'))
]

