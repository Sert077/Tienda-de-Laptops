from django.shortcuts import render
from rest_framework import viewsets
from .serializers import RegistrarSerializer
from .models import Registrar_Laptop
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
  

# Create your views here.

class TodoView(viewsets.ModelViewSet):
    serializer_class = RegistrarSerializer
    queryset = Registrar_Laptop.objects.all()


