from django.contrib import admin
from django.urls import path, include
from main.views import main, object_info


urlpatterns = [
    path('', main, name='main'),
    path('<int:id>/', object_info , name='object')
]