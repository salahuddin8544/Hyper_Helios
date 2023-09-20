
from django.contrib import admin
from django.urls import path
from .views import index,create,delete
urlpatterns = [
    path('',index),
    path('create/',create),
    path('delete/<id>/',delete)
]
