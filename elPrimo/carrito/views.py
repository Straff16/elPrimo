from django.shortcuts import render, redirect
from .models import Carro, ItemsCarro
from tienda.models import Producto, Encabezado_Factura, Detalle_factura, Pedido
from cliente.models import Info_Usuario, Usuario
from django.http import HttpResponse
from .utils import render_to_pdf
from django.core import mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
import random
from pyDolarVenezuela import price
#from cliente.models import Usuario


def Addcarro(usuario_id, producto, cantida):

    aux = Carro.objects.filter(cliente = usuario_id, pagado = False).first()

    items = ItemsCarro.objects.filter(Idcarro = aux.id, producto = producto).first()

    if not items:
        ItemsCarro(Idcarro = aux, producto = producto, cantidad = int(cantida)).save()

    else:
        items.cantidad = int(cantida)
        items.save()

    return redirect('Vercarro')
    
def Vercarro(request):    
    if 'usuario' in request.session:
         usuario_id = request.session.get('user_id')
         ids = list()
         total = 0
         carro = Carro.objects.filter(cliente = usuario_id, pagado = False).first()
         items = ItemsCarro.objects.filter(Idcarro = carro.id).all()
         for i in items:
             ids.append(i.producto.id)
         productos = Producto.objects.filter(id__in = ids).all()

         lista = zip(productos, items)

         for k, j in lista:
             total += (k.precio * j.cantidad)

         if request.POST:
             print(request.POST.get('cantidad'))
         separar = price().get('$bcv')
         dolar = separar.split(' ')[1]
         print(dolar)
         total_bolivares = float(dolar)*total
         context = {
             'contexto': zip(productos, items),
             'total': total,
             'dolar': total_bolivares
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
        correo = request.session.get('email')

        #Si el total es mayor a 80 y el usuario quiere despacho
        if total > 80 and request.POST.get('despacho') == '1': 

            direccion = request.POST.get('direccion')
            if direccion:
                despacho = Info_Usuario.objects.get(id = direccion)
            else:
                despacho = None
            

            registroPago(cliente, despacho, total, carro, correo, flete=True)

            carro.pagado = True
            carro.save()
            Carro(cliente = cliente).save()
            return redirect('Pedidos')
        
        elif total > 80 and request.POST.get('despacho') == '0':

            despacho = None

            registroPago(cliente, despacho, total, carro, correo, flete=False)

            carro.pagado = True
            carro.save()
            Carro(cliente = cliente).save()
            
            return redirect('Pedidos')
        
        else:
            despacho = None
            registroPago(cliente, despacho, total, carro, correo, flete=False)
            carro.pagado = True
            carro.save()
            Carro(cliente = cliente).save()
            return redirect('Pedidos')

    return render(request, 'carrito/pagar.html', {'direcciones': direcciones, 'total': total})


def pedidos(request):
    cliente = request.session.get('user_id')
    #Obtener todas las facturas generadas por el cliente
    encabezado = Encabezado_Factura.objects.filter(id_cliente = cliente).all()
    #Guardar en una lista todas las ids de las facturas
    ids = [p.id for p in encabezado]
    print(len(ids))
    #Obtener todos los pedidos de un cliente usando la lista de ids de facturas y que el estatus sea false
    pedidos = Pedido.objects.filter(id_encabezado__in = ids).all()
    print(len(pedidos))
    contexto = zip(encabezado, pedidos)
    return render(request, 'carrito/pedidos.html', {'pedidos': contexto})

'''
def factura(request, numero_factura):
    factura = Encabezado_Factura.objects.get(numero_factura = numero_factura)
    detalle = Detalle_factura.objects.filter(id_encabezado = factura).all()
    return render(request, 'carrito/factura.html', {'factura': factura, 'detalle': detalle})
'''

def facturapdf(request, numero_factura):
    if 'usuario' in request.session:
        factura = Encabezado_Factura.objects.get(numero_factura = numero_factura)
        cliente = Usuario.objects.filter(id = request.session.get('user_id')).first()
        detalle = Detalle_factura.objects.filter(id_encabezado = factura).all()

        lista = list()
        cantidad = list()
        for i in detalle:
            lista.append(i.id_prod.nombre_prod)
            cantidad.append(i.cantidad)


        productos = Producto.objects.filter(nombre_prod__in = lista).all()

        iva = (factura.dolar * factura.total)*0.16
        
        bolivares = factura.dolar * factura.total

        total = iva + bolivares

        contexto = {
            'factura': factura,
            'productos': zip(productos, detalle),
            'cliente': cliente,
            'iva': iva,
            'bolivares': bolivares,
            'total': total
        }

        pdf = render_to_pdf('carrito/factura.html', contexto)
        return HttpResponse(pdf, content_type='application/pdf')
    else:
        return redirect('login')

def registroPago(cliente, despacho, total, carro, correo, flete) -> None:
    numero = random.getrandbits(32)

    separar = price().get('$bcv')
    dolar = separar.split(' ')[1]

    encabezado = Encabezado_Factura(
        numero_factura = numero,
        id_cliente = cliente,
        iva = 12,
        flete = flete,
        total = total,
        direccion_despacho = despacho,
        dolar = dolar
    ).save()

    encabezado = Encabezado_Factura.objects.get(numero_factura = numero)

    items = ItemsCarro.objects.filter(Idcarro = carro.id).all()

    for i in items:

        Detalle_factura(
            id_encabezado = encabezado,
            id_prod = i.producto,
            cantidad = i.cantidad
            ).save()
        
    detalle = Detalle_factura.objects.get(id_encabezado = encabezado.id)

    enviarEmail(encabezado, detalle, correo)
    
    Pedido(id_encabezado = encabezado).save()

def enviarEmail(encabezado, detalle, correo):
    asunto = 'Compra confirmada'
    html_message = render_to_string('carrito/factura.html', {'factura': encabezado, 'detalle': detalle})
    plain_message = strip_tags(html_message)
    from_email = 'From elprimosa24@gmail.com'
    to = correo

    mail.send_mail(asunto, plain_message, from_email, [to], html_message=html_message)