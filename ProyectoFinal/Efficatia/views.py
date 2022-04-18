from django.shortcuts import render
from Efficatia.models import Consulta, Cliente, Lote
from Efficatia.forms import FormularioRegistroCliente


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

def Informacion(request):
    return render(request, 'Efficatia/Inicio.html')

def RegistroCliente(request):
    if request.method == 'POST':
        FormularioCliente = FormularioRegistroCliente(request.POST)
        if FormularioCliente.is_valid():
            InformacionCliente=FormularioCliente.cleaned_data()
            NuevoCliente=Cliente(nombre=InformacionCliente['nombre'], email=InformacionCliente['email'], empresa=InformacionCliente['empresa'])
            NuevoCliente.save()
            mensaje= f'Se ha registrado a {NuevoCliente.nombre} con éxito.'
            return render(request, 'Efficatia/Inicio.html', {'mensaje':mensaje})
    
    else:
        FormularioCliente=FormularioRegistroCliente()

        return render(request, 'Efficatia/RegistroCliente.html', {"Formulario":FormularioCliente})
