from django.urls import path
from . import views


urlpatterns = [ 
    path('register', views.registro, name='registro'),
    path('login', views.login, name='login'),
    path('perfil', views.perfil, name='perfil'),
    path('logout', views.logout, name='logout'),
    path('direcciones', views.direcciones, name='direcciones')
]










