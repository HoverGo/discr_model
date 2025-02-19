from django.contrib import admin
from django.urls import path, include
from main.views import main, object_info, discret_model, role_model, mandat_model


urlpatterns = [
    path('', main, name='main'),
    path('discret/', discret_model, name='discret_model'),
    path('role/', role_model, name='role_model'),
    path('mandat/', mandat_model, name='mandat_model'),
    path('<str:model>/<int:id>/', object_info , name='object_info'),
]