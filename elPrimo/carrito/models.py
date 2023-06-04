from django.db import models
from cliente.models import Usuario
from tienda.models import Producto

class Carro(models.Model):
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='carro')
    pagado = models.BooleanField(default=False)

class ItemsCarro(models.Model):
    Idcarro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True, blank=True)
    cantidad = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.producto.nombre_prod
