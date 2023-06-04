from django.db import models

class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=16)
    correo = models.EmailField(max_length=250, unique=True)
    

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

class Info_Usuario(models.Model):
    municipio = models.CharField(max_length=50)
    urbanizacion = models.CharField(max_length=50)
    cedula = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=12 ,unique=True)
    direccion = models.TextField(max_length=150)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
