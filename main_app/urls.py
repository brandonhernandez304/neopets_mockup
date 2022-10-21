from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('neopets/', views.neopets_index, name='index'),
    path('neopets/<int:neopet_id>/', views.neopets_detail, name='detail'),
]