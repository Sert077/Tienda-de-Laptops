from django.contrib import admin
from .models import Registrar_Laptop
from .models import vender_Laptop, crear_factura

# Register your models here.
admin.site.register(Registrar_Laptop)
admin.site.register(vender_Laptop)
admin.site.register(crear_factura)