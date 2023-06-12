from django.urls import path
from . import views


urlpatterns = [
    path('', views.Vercarro, name='Vercarro'),
    path('Addcarro/<int:id_producto>', views.Addcarro, name='Addcarro'),
    path('Deletecarro/<int:id_producto>', views.Deletecarro, name='Deletecarro'),
    path('pagar/', views.pagar, name='Pagar'),
    path('pedidos/', views.pedidos, name='Pedidos'),
    path('factura/<str:numero_factura>', views.facturapdf, name='Factura')
]