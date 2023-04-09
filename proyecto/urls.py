from django.urls import path
from . import views
from django.conf.urls import handler404
urlpatterns = [
    path('', views.index, name="index"),
    path('laptops/', views.laptops, name="laptops"),
    path('registro_laptops/', views.registro_laptops, name="registro_laptops"),
    path('logout/', views.signout, name='logout'),
    path('login/', views.signin, name="signin"),
    path('informacionLaptop/<int:id>',views.informacionLaptop, name = "informacionLaptop"),


]


handler404 = 'proyecto.views.error_404'