from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm, UpdateForm
from tienda.models import Producto
from .models import Usuario, Info_Usuario
from carrito.models import Carro
from django.contrib import messages

def registro(request):
    if 'usuario' not in request.session:
        if request.method == 'POST':

            if request.POST.get('password1') == request.POST.get('password2'):
                print('Entro en el segundo if')
                
                nombre = request.POST.get('nombre')
                password1 = request.POST.get('password1')
                correo = request.POST.get('correo')
                try:
                    Usuario(nombre_usuario=nombre, password=password1, correo=correo).save()
                    user = Usuario.objects.get(nombre_usuario = nombre)
                    Carro(cliente = user).save()

                except:
                    messages.warning(request, 'Nombre de usuario o correo ya existentes')
                
                return redirect('login')
            
            else:
                messages.info(request, 'Las contraseñas no coinciden')
                return redirect('registro')
    else:
        return redirect('')
    
    return render(request, 'cliente/registro.html')

def login(request):
    if 'usuario' not in request.session:
        
        if request.method == 'POST':
            user = Usuario.objects.filter(nombre_usuario = request.POST.get('usuario')).first()
            if user:
                if user.password == request.POST.get('password'):

                    request.session['usuario'] = user.nombre_usuario
                    request.session['user_id'] = user.id
                    request.session['email'] = user.correo
                    messages.success(request, f'Bienvenido {user.nombre_usuario}')
                    return redirect('perfil')
                
                else:
                    messages.warning(request, 'Contraseña incorrecta')
                    return redirect('login')
    else:
        redirect('')

    
    return render(request, 'cliente/prueba.html')


def perfil(request):
    
    if 'usuario' not in request.session:
        return redirect('login')
    
    else:
        print('PERFIL')
        sesion = request.session.get('usuario')
        user = Usuario.objects.filter(nombre_usuario = sesion).first()
        print()
        return render(request, 'cliente/perfil.html', {'user': user})
    
def logout(request):
    if 'usuario' in request.session:
        request.session.pop('usuario')
        request.session.pop('user_id')
        request.session.pop('email')
        return redirect('')
    
    else:
        return redirect('')
    

def direcciones(request):
    if 'usuario' not in request.session:
        return redirect('login')
    
    else:

        direcciones = Info_Usuario.objects.filter(id_usuario = request.session.get('user_id')).all()
        if request.method == 'POST':
            municipio = request.POST.get('municipio')
            urbanizacion = request.POST.get('urbanizacion')
            telefono = request.POST.get('telefono')
            cedula = request.POST.get('cedula')
            direccion = request.POST.get('direccion')
            
            sesion_id = request.session.get('user_id')
            user = Usuario.objects.get(id = sesion_id)
            try:
                Info_Usuario(municipio = municipio, 
                            urbanizacion = urbanizacion, 
                            cedula=cedula, 
                            telefono=telefono,
                            direccion=direccion,
                            id_usuario=Usuario.objects.get(id = sesion_id)).save()

                return redirect('direcciones')
            except:
                messages.warning(request, 'El numero de telefono o cedula ingresados ya estan registrados')
                return redirect('direcciones')

    return render(request, 'cliente/direcciones.html', {'direcciones': direcciones})

