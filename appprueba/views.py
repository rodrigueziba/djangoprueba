from django.shortcuts import render
from .models import Categorias

# Create your views here.
def mostrar(request):
	st=Categorias.objects.all()  # Collect all records from table 
	return render(request,'mostrar.html',{'st':st})