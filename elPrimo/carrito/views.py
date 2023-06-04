from django.shortcuts import render, redirect
from .models import Carro, ItemsCarro
from tienda.models import Producto, Encabezado_Factura, Detalle_factura
from cliente.models import Info_Usuario, Usuario
import random
#from cliente.models import Usuario


def Addcarro(usuario_id, producto, cantida):

    #usuario_id = request.session.get('user_id')

    aux = Carro.objects.filter(cliente = usuario_id, pagado = False).first()

    items = ItemsCarro.objects.filter(Idcarro = aux.id, producto = producto).first()

    if not items:
        ItemsCarro(Idcarro = aux, producto = producto, cantidad = int(cantida)).save()

    else:
        items.cantidad = int(cantida)
        items.save()

        """
        usuario_id = request.session.get('user_id')
        aux = Carro.objects.filter(cliente = usuario_id, pagado = False).first()
        #prod = Producto.objects.get(id = id_producto)
        #print(f'AUXILIAR {aux.id}')
        items = ItemsCarro.objects.filter(Idcarro = aux.id, producto = id_producto).first()
        #print(items)
        if not items:
            ItemsCarro(Idcarro = aux, producto = Producto.objects.get(id = id_producto)).save()

        else:
            items.cantidad += 1
            items.save()
        """
        '''for i in items:
            print(i.id)
            if id_producto == i.id:
                print(f'CANTIDAD {i.cantidad}')
                i.cantidad += 1
                flag = 1
                i.save()
        if flag == 0:
            ItemsCarro(Idcarro = aux, producto = Producto.objects.get(id=id_producto)).save()'''
        
    return redirect('Vercarro')
    
def Vercarro(request):    
    if 'usuario' in request.session:
         usuario_id = request.session.get('user_id')
         ids = list()
         total = 0
         carro = Carro.objects.filter(cliente = usuario_id, pagado = False).first()
         items = ItemsCarro.objects.filter(Idcarro = carro.id).all()
         print(len(items))
         for i in items:
             ids.append(i.producto.id)
         productos = Producto.objects.filter(id__in = ids).all()

         lista = zip(productos, items)
         #print(items)

         for k, j in lista:
             #print(k.nombre_prod)
             total += (k.precio * j.cantidad)

         if request.POST:
             print(request.POST.get('cantidad'))
         
         context = {
             'contexto': zip(productos, items),
             'total': total,
         }

         request.session['total'] = total
         return render(request, 'carrito/carro.html', context)
    else:
        return redirect('perfil')
    
def Deletecarro(request, id_producto):
    ItemsCarro.objects.filter(producto = id_producto).delete()
    return redirect('Vercarro')
       

def pagar(request):
    direcciones = Info_Usuario.objects.filter(id_usuario = request.session.get('user_id')).all()
    total = request.session.get('total')
    

    if request.POST:
        cliente = Usuario.objects.get(id = request.session.get('user_id'))
        carro = Carro.objects.filter(cliente = cliente.id, pagado = False).first()
        direccion = request.POST.get('direccion')
        despacho = Info_Usuario.objects.get(id = direccion)

        #Si el total es mayor a 80 y ell usuario quiere despacho
        if total > 80 and request.POST.get('despacho') == '1': 
            numero = random.getrandbits(32)
            Encabezado_Factura(
                numero_factura = numero,
                id_cliente = cliente,
                base_imp = 1,
                iva = 12,
                flete = True,
                total = total,
                direccion_despacho = despacho
            ).save()

            encabezado = Encabezado_Factura.objects.get(numero_factura = numero)

            items = ItemsCarro.objects.filter(Idcarro = carro.id).all()

            for i in items:

                Detalle_factura(
                    id_encabezado = encabezado,
                    id_prod = i.producto,
                    cantidad = i.cantidad

                ).save()

            carro.pagado = 1
            carro.save()
            Carro(cliente = cliente).save()
            return redirect('tienda')
        
        elif total > 80 and request.POST.get('despacho') == '0':
            numero = random.getrandbits(32)
            Encabezado_Factura(
                numero_factura = numero,
                id_cliente = cliente,
                base_imp = 1,
                iva = 12,
                flete = False,
                total = total,
                direccion_despacho = None
            ).save()

            encabezado = Encabezado_Factura.objects.get(numero_factura = numero)

            items = ItemsCarro.objects.filter(Idcarro = carro.id).all()

            for i in items:

                Detalle_factura(
                    id_encabezado = encabezado,
                    id_prod = i.producto,
                    cantidad = i.cantidad

                ).save()

            carro.pagado = 1
            carro.save()
            Carro(cliente = cliente).save()
            
            return redirect('Vercarro')
        
        else:
            numero = random.getrandbits(32)
            Encabezado_Factura(
                numero_factura = numero,
                id_cliente = cliente,
                base_imp = 1,
                iva = 12,
                flete = False,
                total = total,
                direccion_despacho = None
            ).save()

            encabezado = Encabezado_Factura.objects.get(numero_factura = numero)

            items = ItemsCarro.objects.filter(Idcarro = carro.id).all()

            for i in items:

                Detalle_factura(
                    id_encabezado = encabezado,
                    id_prod = i.producto,
                    cantidad = i.cantidad

                ).save()

            carro.pagado = 1
            carro.save()
            Carro(cliente = cliente).save()
            return redirect('perfil')


    return render(request, 'carrito/pagar.html', {'direcciones': direcciones, 'total': total})
