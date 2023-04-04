from django.shortcuts import render
from rest_framework import viewsets
from .serializers import RegistrarSerializer
from .models import Registrar_Laptop

# Create your views here.

class TodoView(viewsets.ModelViewSet):
    serializer_class = RegistrarSerializer
    queryset = Registrar_Laptop.objects.all()