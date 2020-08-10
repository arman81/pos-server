
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
   path('product', views.getProduct, name="getProduct"),
   path('order', views.orderProduct, name="order"),
]
