from django.contrib import admin

from .models import *
from cliente.models import Usuario, Info_Usuario

# Register your models here.


admin.site.register(Producto)
admin.site.register(CategoriaProd)
admin.site.register(Encabezado_Factura)
admin.site.register(Pedido)
admin.site.register(Usuario)
admin.site.register(Info_Usuario)

