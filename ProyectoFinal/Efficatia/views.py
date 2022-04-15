from django.shortcuts import render
from Efficatia.models import Consulta

# Create your views here.

def inicio(request):
    return render(request, 'Efficatia/Inicio.html')

def FormularioConsulta(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        email = request.POST["email"]
        Consultaa = request.POST["Consulta"]
        NuevaConsulta=Consulta(nombre=nombre, email=email, consultaa =Consultaa)
        NuevaConsulta.save()
        mensaje= "Su consulta fue tomada con exito. Muchas Gracias!"
    
    return render(request, 'Efficatia/inicio.html', {'mensaje': mensaje})