from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.LocationList.as_view(), name='locations'),
    path('<slug:slug>/', views.LocationDetail.as_view(), name='location_detail'),
    path('add/', views.LocationAdd.as_view(), name='add_location'),
]