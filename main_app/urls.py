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
    path('neopets/<int:neopet_id>/add_feeding/', views.add_feeding, name='add_feeding'),
    path('neopets/<int:neopet_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
    path('toys/', views.toys_index, name='toys_index'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]