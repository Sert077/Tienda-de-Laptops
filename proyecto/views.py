from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Registrar_Laptop
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
def index(request):
    return render(request, "index.html")

def informacion(request):
    return render(request, "informacion.html")
# Create your views here.

@login_required
def informacionLaptop(request, id):
    laptop = Registrar_Laptop.objects.get(id = id)
    cadena_eliminar = 'proyecto'
    ruta_1 = str(laptop.imagen_1).replace(cadena_eliminar,'')
    ruta_2 = str(laptop.imagen_2).replace(cadena_eliminar,'')
    ruta_3 = str(laptop.imagen_3).replace(cadena_eliminar,'')
    ruta_4 = str(laptop.imagen_4).replace(cadena_eliminar,'')
    return render(request, "informacionLaptop.html",{
        'laptop': laptop,
        'ruta_1': ruta_1,
        'ruta_2': ruta_2,
        'ruta_3': ruta_3,
        'ruta_4': ruta_4,
    })

@login_required
def modificarLaptop(request, id):
    laptop = Registrar_Laptop.objects.get(id = id)
    cadena_eliminar = 'proyecto'
    ruta_1 = str(laptop.imagen_1).replace(cadena_eliminar,'')
    ruta_2 = str(laptop.imagen_2).replace(cadena_eliminar,'')
    ruta_3 = str(laptop.imagen_3).replace(cadena_eliminar,'')
    ruta_4 = str(laptop.imagen_4).replace(cadena_eliminar,'')
    return render(request, "modificar_laptop.html",{
        'laptop': laptop,
        'ruta_1': ruta_1,
        'ruta_2': ruta_2,
        'ruta_3': ruta_3,
        'ruta_4': ruta_4,
    })

def error_404(request, exception):
    return render(request, '403.html', status=404)

@login_required
def laptops(request):
    if request.method == 'GET':
        laptops = Registrar_Laptop.objects.all()
        lista_rutas = []
        for laptop in laptops:
            ruta_fallida =  str(laptop.imagen_1)
            cadena_eliminar = 'proyecto'
            ruta_correcta = ruta_fallida.replace(cadena_eliminar, '')
            lista_rutas.append(ruta_correcta)
            print(ruta_correcta)
            
        laptops_rutas = zip(laptops, lista_rutas)
        return render(request, "laptops.html",{
            'laptops_rutas': laptops_rutas
        })
    else:
        laptop = Registrar_Laptop.objects.create(
            marca=request.POST['marca'],
            modelo=request.POST['modelo'],
            nombre=request.POST['nombre'],
            stock=request.POST['stock'],
            precio=request.POST['precio'],
            pantalla=request.POST['pantalla'],
            teclado=request.POST['teclado'],
            procesador=request.POST['procesador'],
            ram=request.POST['ram'],
            color=request.POST['color'],
            m2=request.POST['m2'],
            hdd=request.POST['hdd'],
            grafica=request.POST['grafica'],
            descripcion=request.POST['descripcion'],
            imagen_1=request.FILES['imagen_1'],
            imagen_2=request.FILES['imagen_2'],
            imagen_3=request.FILES['imagen_3'],
            imagen_4=request.FILES['imagen_4'])
        messages.success(request, f"¡La laptop {laptop.nombre} ha sido registrada exitosamente!")
        return redirect("laptops")
        



def signin(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is None:
                messages.error(request, 'Nombre de usuario o contraseña incorrectos.')
                return render(request, 'login.html')
            else:
                login(request, user)
                return redirect("index")
        except:
            return redirect("signin")


def signout(request):
    logout(request)
    return redirect("index")

