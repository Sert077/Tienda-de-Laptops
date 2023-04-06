from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Registrar_Laptop
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
def index(request):
    return render(request, "index.html")


def laptops(request):
    print(request.method)
    if request.method == 'GET':
        return render(request, "laptops.html")
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
            imagenes=request.POST['imagenes'])
        print(laptop)
        return redirect("laptops")


def registro_laptops(request):
    return render(request, "registrar_laptops.html")


def signin(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        try:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is None:
                return render(request, 'login.html', {
                    'error':
                    'El nombre de usuario o contraseña son incorrectos'
                })
            else:
                login(request, user)
                return redirect("index")
        except:
            return redirect("signin")


def signout(request):
    logout(request)
    return redirect("index")


def formulario(request):

    print(request.method)
    if request.method == 'POST':
        modelo = request.POST.get('modelo')
        marca = request.POST.get('marca')
        nombre = request.POST.get('nombre')
        stock = request.POST.get('stock')
        precio = request.POST.get('precio')
        pantalla = request.POST.get('pantalla')
        teclado = request.POST.get('teclado')
        procesador = request.POST.get('procesador')
        ram = request.POST.get('ram')
        color = request.POST.get('color')
        m2 = request.POST.get('m2')
        hdd = request.POST.get('hdd')

        # Aquí es donde se procesan los datos del formulario.
        # Por ejemplo, puede guardarlos en la base de datos o hacer cualquier otra acción que desee.

        return HttpResponseRedirect(reverse('formulario'))

    return render(request, 'index.html')