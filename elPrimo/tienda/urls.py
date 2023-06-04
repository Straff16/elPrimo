from django.urls import path
from . import views


urlpatterns = [
    path('', views.tienda, name='tienda'),
    path('producto/<str:nombre_producto>', views.producto, name='producto'),
]