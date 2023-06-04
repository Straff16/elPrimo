from typing import Any
from django.db import models
from cliente.models import Usuario, Info_Usuario

class CategoriaProd(models.Model):
    nombre_categoria = models.CharField(max_length=50)
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
    stock_max = models.IntegerField()
    stock_min = models.IntegerField()
    cantidad = models.IntegerField()
    dimensiones = models.CharField(max_length=15)
    disponibilidad = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

class Encabezado_Factura(models.Model):
    numero_factura = models.CharField(max_length=16)
    fecha_emision = models.DateTimeField(auto_now_add=True)
    id_cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    base_imp = models.FloatField()
    iva = models.FloatField()
    flete = models.BooleanField()
    total = models.FloatField()
    direccion_despacho = models.ForeignKey(Info_Usuario, on_delete=models.CASCADE, null=True)

class Detalle_factura(models.Model):
    id_encabezado = models.ForeignKey(Encabezado_Factura, on_delete=models.CASCADE)
    id_prod = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

class Almacen(models.Model):
    nombre_almacen = models.CharField(max_length=40)


    class Meta:
        verbose_name = 'Almacen'
        verbose_name_plural = 'Almacenes'


class Distribuidor(models.Model):
    nombre = models.CharField(max_length=60)
    rif = models.IntegerField(7)
    direccion = models.CharField(max_length=40)
    telefono = models.IntegerField()
    correo = models.CharField(max_length=60)

    class Meta:
        verbose_name = 'Distribuidor'
        verbose_name_plural = 'Distribuidores'

    #upload_to='tienda', null=True, blank=True





