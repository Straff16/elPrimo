from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm, UpdateForm
from tienda.models import Producto
from .models import Usuario, Info_Usuario
from carrito.models import Carro

def registro(request):
    if 'usuario' not in request.session:
        form = RegisterForm()
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            print('PRIMER IF')
            print(form.is_valid())

            if form.is_valid() and request.POST['password1'] == request.POST['password2']:
                print('Entro en el segundo if')
                
                nombre = form.cleaned_data.get('usuario')
                password1 = form.cleaned_data.get('password1')
                correo = form.cleaned_data.get('correo')
                Usuario(nombre_usuario=nombre, password=password1, correo=correo).save()
                user = Usuario.objects.get(nombre_usuario = nombre)
                Carro(cliente = user).save()

                #Usuario(nombre_usuario = nombre, 
                        #password ='123', correo = 'eduardopaez48@gmail.com', cedula=30, telefono=15).save()
                #Usuario.objects.filter(id=1).update(municipio='los guayos', urbanizacion='los cerrtios')
                
                return redirect('login')
    else:
        return redirect('tienda')
    
    return render(request, 'cliente/registro.html', {'form': form})

def login(request):
    form = LoginForm()
    if 'usuario' not in request.session:
        
        if request.method == 'POST':
            form = LoginForm(request.POST)
            print('PRIMER IF')
            
            if form.is_valid():
                print('SEGUNDO IF')
                user = Usuario.objects.filter(nombre_usuario = request.POST.get('usuario')).first()
                print(type(user.password))
                print(type(form.cleaned_data.get('password')))
                if user.password == form.cleaned_data.get('password'):
                    print('TERCER Y ULTIMO IF')

                    request.session['usuario'] = user.nombre_usuario
                    a = request.session['user_id'] = user.id
                    print(a)
                    return redirect('tienda')
                
                else:
                    redirect('login')

    
    return render(request, 'cliente/login.html', {'form': form})


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
        return redirect('tienda')
    
    else:
        return redirect('tienda')
    

def direcciones(request):
    if 'usuario' not in request.session:
        return redirect('login')
    
    else:
        #user = Info_Usuario.objects.filter(nombre_usuario = sesion).first()

        form = UpdateForm()
        direcciones = Info_Usuario.objects.filter(id_usuario = request.session.get('user_id')).all()
        print(type(direcciones), direcciones)   
        if request.method == 'POST':
            formulario = UpdateForm(request.POST)

            if formulario.is_valid():
                municipio = formulario.cleaned_data.get('municipio')
                urbanizacion = formulario.cleaned_data.get('urbanizacion')
                telefono = formulario.cleaned_data.get('telefono')
                cedula = formulario.cleaned_data.get('cedula')
                direccion = formulario.cleaned_data.get('direccion')
                
                sesion_id = request.session.get('user_id')
                user = Usuario.objects.get(id = sesion_id)

                Info_Usuario(municipio = municipio, 
                             urbanizacion = urbanizacion, 
                             cedula=cedula, 
                             telefono=telefono,
                             direccion=direccion,
                             id_usuario=Usuario.objects.get(id = sesion_id)).save()

                return redirect('direcciones')

    return render(request, 'cliente/direcciones.html', {'form': form, 'direcciones': direcciones})

