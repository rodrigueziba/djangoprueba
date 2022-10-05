from django.shortcuts import render
from .models import Categorias
from .models import CertificacionesPedidos
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("INDEX DE LA APP ")

def mostrar(request):
	st=Categorias.objects.all()  # Collect all records from table 
	return render(request,'mostrar.html',{'st':st})

def mostrarCertificacionesPedidos(request):
	st=CertificacionesPedidos.objects.all()  # Collect all records from table 
	return render(request,'mostrarcertificacionespedidos.html',{'st':st})