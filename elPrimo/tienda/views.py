from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Producto
from carrito.models import ItemsCarro, Carro
from carrito.views import Addcarro

#from cliente.models import Usuario

def tienda(request):
    productos = Producto.objects.all()
    #print(request.session.get('usuario'))
    #print(productos.exists())
    return render(request, 'tienda/home.html', {'productos': productos})

def producto(request, nombre_producto):

    #print(type(request.session.get('user_id')))

    producto = Producto.objects.get(nombre_prod = nombre_producto)

    if request.POST and 'usuario' in request.session:

        user_id = request.session.get('user_id')

        cantida = request.POST.get('cantidad')

        #print(f'CANTIDAD {type(cantida)}')

        if int(cantida) <= 0 or cantida == '':
            cantida = 1

        Addcarro(user_id, producto, cantida)

        """
        usuario_id = request.session.get('user_id')

        aux = Carro.objects.filter(cliente = usuario_id, pagado = False).first()

        items = ItemsCarro.objects.filter(Idcarro = aux.id, producto = producto.id).first()

        if not items:
            ItemsCarro(Idcarro = aux, producto = producto, cantidad = int(cantida)).save()

        else:
            items.cantidad = int(cantida)
            items.save()
        """
        
        return redirect('Vercarro')
    
    return render(request, 'tienda/producto.html', {'producto': producto})

def buscador(request):
    if request.GET:
        nombre = request.GET.get('buscador')
        productos = Producto.objects.filter(nombre_prod__icontains = nombre).all()
        return render(request, 'tienda/home.html', {'productos': productos})


