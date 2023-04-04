from rest_framework import serializers
from .models import Registrar_Laptop

class RegistrarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registrar_Laptop
        fields = ('marca', 'modelo', 'nombre', 'stock', 'precio', 'pantalla', 'teclado', 'procesador', 'ram', 'color', 'm2', 'hdd', 'grafica', 'descripcion', 'imagenes')
        