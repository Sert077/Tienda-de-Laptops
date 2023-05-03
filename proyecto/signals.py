from django.db.models.signals import pre_save
from django.dispatch import receiver
from proyecto.models import Registrar_Laptop, vender_Laptop

@receiver(pre_save, sender=vender_Laptop)
def restar_valor_tabla2(sender, instance, **kwargs):
    restastock = Registrar_Laptop.objects.first() # Obtener el primer objeto de Tabla2
    instance.stock -= restastock.cantidad # Restar el valor de Tabla2 del valor de Tabla1
