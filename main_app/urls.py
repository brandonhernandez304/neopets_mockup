from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('neopets/', views.neopets_index, name='index'),
    path('neopets/<int:neopet_id>/', views.neopets_detail, name='detail'),
    path('neopets/create/', views.NeopetCreate.as_view(), name='neopets_create'),
    path('neopets/<int:pk>/update/', views.NeopetUpdate.as_view(), name='neopets_update'),
    path('neopets/<int:pk>/delete/', views.NeopetDelete.as_view(), name='neopets_delete'),
]