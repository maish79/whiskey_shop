from django.urls import path 
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about_us/', views.about_us, name='about_us'),
    path('FAQ/', views.FAQ, name='FAQ'),
    path('sitemap', views.sitemap, name='sitemap'),
    
]