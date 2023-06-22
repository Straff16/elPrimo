from django.urls import path
from . import views


urlpatterns = [
    path('', views.tienda, name='tienda'),
    path('productos/<str:nombre_categoria>', views.productos, name='productos'),
    path('buscar', views.buscador, name='buscador'),
    path('producto/<str:nombre_prod>', views.producto, name='producto')
]