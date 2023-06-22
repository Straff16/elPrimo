from typing import Any
from django.db import models
from cliente.models import Usuario, Info_Usuario

class CategoriaProd(models.Model):
    nombre_categoria = models.CharField(max_length=50)
    imagen_categoria = models.ImageField(upload_to='categoriasIMGs/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'categoriaProd'
        verbose_name_plural = 'categoriasProd'
    
    def __str__(self):
        return self.nombre_categoria
    

class Producto(models.Model):
    nombre_prod = models.CharField(max_length=50)
    categoria = models.ForeignKey(CategoriaProd, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='tienda/', null=True, blank=True)
    precio = models.FloatField()
    cantidad = models.IntegerField()
    dimensiones = models.CharField(max_length=15)
    disponibilidad = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self) -> str:
        return self.nombre_prod

class Encabezado_Factura(models.Model):
    numero_factura = models.CharField(max_length=16)
    fecha_emision = models.DateTimeField(auto_now_add=True)
    id_cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    iva = models.FloatField()
    flete = models.BooleanField()
    total = models.FloatField()
    direccion_despacho = models.ForeignKey(Info_Usuario, on_delete=models.CASCADE, null=True)
    dolar = models.FloatField(default=20)

    def __str__(self) -> str:
        return self.numero_factura

class Detalle_factura(models.Model):
    id_encabezado = models.ForeignKey(Encabezado_Factura, on_delete=models.CASCADE)
    id_prod = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

class Pedido(models.Model):
    id_encabezado = models.ForeignKey(Encabezado_Factura, on_delete=models.CASCADE)
    estatus = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.id_encabezado.numero_factura





