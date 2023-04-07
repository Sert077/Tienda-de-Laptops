from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('laptops/', views.laptops, name="laptops"),
    path('registro_laptops/', views.registro_laptops, name="registro_laptops"),
    path('logout/', views.signout, name='logout'),
    path('login/', views.signin, name="signin"),
    #path('formulario/', views.formulario, name='formulario'),
    path('informacion/', views.informacion, name="informacion"),



]
