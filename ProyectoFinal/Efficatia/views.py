from django.shortcuts import render
from Efficatia.models import Consulta, Cliente, Lote
from Efficatia.forms import FormularioRegistroCliente, FormularioLote
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

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

def LogInCliente(request):
    if request.method == "POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            datos=form.cleaned_data
            usuario=datos['username']
            psw=datos['password']
            user= authenticate(username=usuario, password=psw)
            if user:
                login(request, user)
                return render(request, "Efficatia/Inicio.html", {"mensaje": "Bienvenido"})
            else:
                return render(request, "Efficatia/Inicio.html", {"mensaje": "ERROR en datos ingresados"})
        else:
            return render(request, "Efficatia/Inicio.html", {"mensaje": "ERROR en Formulario"})
    else:
        form=AuthenticationForm()
        return render(request, "Efficatia/LogIn.html", {"form": form})

def RegistroUsuario(request):
    if request.method == "POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            form.save()
            return render(request, "Efficatia/Inicio.html", {"mensaje": "Usuario Creado con exito."})
    else:
        form = UserCreationForm()
        return render(request, "Efficatia/RegistroUsuario.html", {"form": form})

def LogOutCliente(request):
    logout(request)
    return render(request, "Efficatia/Inicio.html", {"mensaje": "Gracias, hasta la proxima!"})

def ListaLotes(request):
    if request.user:
        IdCliente=request.user.id

    Lotes=Lote.objects.get(id_cliente=IdCliente)
    contexto={"ListaLotes":Lotes}
    return render(request, "Efficatia/ListaLotes.html", contexto)

def CrearLote(request):
    if request.method == 'POST':
        FormularioLoteNuevo = FormularioLote(request.POST)
        if FormularioLoteNuevo.is_valid():
            InformacionLote=FormularioLoteNuevo.cleaned_data()
            NuevoLote=Lote(id_cliente=InformacionLote[''], campo=InformacionLote['campo'], lote=InformacionLote['lote'], link=InformacionLote['link'])
            NuevoLote.save()
            mensaje= f'Se ha registrado el lote {NuevoLote.lote} con éxito.'
            return render(request, 'Efficatia/Inicio.html', {'mensaje':mensaje})
    
    else:
        FormularioLote=FormularioLote()

        return render(request, 'Efficatia/RegistroCliente.html', {"Formulario":FormularioLote})