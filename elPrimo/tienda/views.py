from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Producto, CategoriaProd
from carrito.models import ItemsCarro, Carro
from carrito.views import Addcarro

#from cliente.models import Usuario

def tienda(request):

    categorias = CategoriaProd.objects.all()

    print([p.nombre_categoria for p in categorias])

    return render(request, 'tienda/tienda.html', {'categorias': categorias})

def productos(request, nombre_categoria):

    #print(type(request.session.get('user_id')))

    categoria = CategoriaProd.objects.get(nombre_categoria = nombre_categoria)

    productos = Producto.objects.filter(categoria = categoria.id).all()

    categorias = CategoriaProd.objects.all()

    #print(p.nombre_prod for p in productos)

    '''
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
    '''
    
    return render(request, 'tienda/productos.html', {'productos': productos, 'categorias': categorias, 'nombre_categoria': categoria})

def buscador(request):
    nombre = request.GET.get('buscador')
    categorias = CategoriaProd.objects.all()
    print(nombre)
    productos = Producto.objects.filter(nombre_prod__icontains = nombre).all()
    return render(request, 'tienda/productos.html', {'productos': productos, 'categorias': categorias})


def producto(request, nombre_prod):

    producto = Producto.objects.get(nombre_prod = nombre_prod)

    if request.POST:

        if 'usuario' in request.session:

            user_id = request.session.get('user_id')

            cantida = request.POST.get('cantidad')

            #print(f'CANTIDAD {type(cantida)}')

            if int(cantida) <= 0 or cantida == '':
                cantida = 1

            Addcarro(user_id, producto, cantida)

            return redirect('Vercarro')
        
        else:
            return redirect('login')

    return render(request, 'tienda/producto.html', {'producto': producto})



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