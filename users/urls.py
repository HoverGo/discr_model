from django.contrib import admin
from django.urls import path, include
from .views import auth, registration, logout

urlpatterns = [
    path('auth/', auth, name='auth'),
    path('registration/', registration, name='registration'),
    path('logout/', logout, name='logout'),
]
