from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.title + ' - ' + self.project.name
    

class Laptop(models.Model):
    marca = models.CharField(max_length=20,unique=True)
    modelo = models.CharField(max_length=20,unique=True)
    stock = models.IntegerField()
    precio = models.IntegerField()
    pantalla = models.FloatField()
    teclado = models.CharField(max_length=10,unique=True)
    procesador = models.CharField(max_length=25,unique=True)
    ram = models.IntegerField()
    color = models.CharField(max_length=15,unique=True)
    m2 = models.IntegerField()
    hdd = models.IntegerField()
    grafica = models.CharField(max_length=25,unique=True)
    descripcion = models.CharField(max_length=300,unique=True)
    imagenes = models.ImageField(upload_to="imagenes/productos", null=True)

