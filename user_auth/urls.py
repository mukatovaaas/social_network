from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('', include('djoser.urls')),
    path('', include('djoser.urls.authtoken')),
]

# login http://localhost:8000/auth/token/login
# register http://localhost:8000/auth/users