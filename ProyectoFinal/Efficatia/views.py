from django.shortcuts import render
from Efficatia.models import Consulta, Cliente, Lote
from Efficatia.forms import FormularioRegistroCliente, FormularioLote, FormularioConsulta
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):
    return render(request, 'Efficatia/Inicio.html')

def FormularioConsultaa(request):
    if request.method == "POST":
        Formulario_Consulta= FormularioConsulta(request.POST)
        if Formulario_Consulta.is_valid():
            ContenidoConsulta=Formulario_Consulta.cleaned_data
            NuevaConsulta=Consulta(nombre=ContenidoConsulta['nombre'], email=ContenidoConsulta['email'], consultaa =ContenidoConsulta['consulta'])
            NuevaConsulta.save()
            mensaje= "Su consulta fue tomada con exito. Muchas Gracias!"
    
        return render(request, 'Efficatia/Notificacion.html', {'mensaje': mensaje})
    
    else:
        Consultar=FormularioConsulta()
        
        return render(request, 'Efficatia/FormularioConsulta.html', {'Formulario':Consultar})

def Informacion(request):
    return render(request, 'Efficatia/Informacion.html')

@login_required
def RegistroCliente(request):
    try:
        if request.method == 'POST':
            FormularioCliente = FormularioRegistroCliente(request.POST)
            if FormularioCliente.is_valid():
                InformacionCliente=FormularioCliente.cleaned_data
                NuevoCliente=Cliente(nombre=InformacionCliente['nombre'], email=InformacionCliente['email'], empresa=InformacionCliente['empresa'], user_id=request.user.id)
                NuevoCliente.save()

                mensaje= f'Se ha registrado a {NuevoCliente.nombre} con éxito.'
                return render(request, 'Efficatia/Notificacion.html', {'mensaje':mensaje})
        
        else:
            FormularioCliente=FormularioRegistroCliente()

            return render(request, 'Efficatia/RegistroCliente.html', {"Formulario":FormularioCliente})
    except:
        return render(request, 'Efficatia/Notificacion.html', {'mensaje': 'Este usuario ya tiene un cliente creado'})


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
                if request.user.last_login == None:
                    return render(request, 'Efficatia/RegistroUsuarioExitoso.html')
                else:
                    return render(request, "Efficatia/Notificacion.html", {"mensaje": "Bienvenido"})
            else:
                return render(request, "Efficatia/Notificacion.html", {"mensaje": "ERROR en datos ingresados"})
        else:
            return render(request, "Efficatia/Notificacion.html", {"mensaje": "ERROR en Formulario"})
    else:
        form=AuthenticationForm()
        return render(request, "Efficatia/LogIn.html", {"form": form})

def RegistroUsuario(request):
   
    if request.method == "POST":
        
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            form.save()
        return render(request, "Efficatia/Notificacion.html", {"mensaje": f"Usuario {username} creado con exito"})
    else:
        form = UserCreationForm()
        return render(request, "Efficatia/RegistroUsuario.html", {"form": form})

@login_required
def RegistroUsuarioExitoso(request):
    return render(request, 'Efficatia/RegistroUsuarioExitoso.html')

@login_required
def LogOutCliente(request):
    logout(request)
    return render(request, "Efficatia/Notificacion.html", {"mensaje": "Gracias, hasta la proxima!"})


@login_required
def ListaLotes(request):
    if request.user:
        try:
            cliente=Cliente.objects.get(user_id = request.user.id)

            IdCliente= cliente.id
        except: 
            return render(request, "Efficatia/RegistroUsuarioExitoso.html")
    Lotes= Lote.objects.filter(id_cliente=IdCliente)
    contexto={"ListaLotes":Lotes}
    return render(request, "Efficatia/ListaLotes.html", contexto)


@login_required
def CrearLote(request):
    if request.method == 'POST':
        FormularioLoteNuevo = FormularioLote(request.POST)
        if FormularioLoteNuevo.is_valid():
            InformacionLote=FormularioLoteNuevo.cleaned_data
            
            cliente=Cliente.objects.get(user_id=request.user.id)
            
            

            

            NuevoLote=Lote(id_cliente=InformacionLote['id_cliente'], campo=InformacionLote['campo'], lote=InformacionLote['lote'], link=InformacionLote['link'])
            if NuevoLote.id_cliente == cliente:
                NuevoLote.save()
                mensaje= f'Se ha registrado el lote {NuevoLote.lote} con éxito.'
                
                

                return render(request, 'Efficatia/Notificacion.html', {'mensaje':mensaje})
               
            else:
                 return render(request, 'Efficatia/CrearLote.html', {"Formulario":FormularioLote, 'mensaje':f'El Cliente {NuevoLote.id_cliente} no corresponde con el usuario{cliente}. Intenalo de nuevo.'})
    
    else:
        FormularioLoteNuevo=FormularioLote()

        return render(request, 'Efficatia/CrearLote.html', {"Formulario":FormularioLote})

@login_required
def EditarLote(request, ID):
    LoteRegistrado=Lote.objects.get(id=ID)
    if request.method == "POST":
        FormularioEdicion=FormularioLote(request.POST)
        if FormularioEdicion.is_valid():
            info=FormularioEdicion.cleaned_data
            LoteRegistrado.campo=info['campo']
            LoteRegistrado.lote=info['lote']
            LoteRegistrado.id_cliente=info['id_cliente']
            LoteRegistrado.link=info['link']
            
            LoteRegistrado.save()

            cliente=Cliente.objects.get(user_id = request.user.id)

            IdCliente= cliente.id
            Lotes= Lote.objects.filter(id_cliente=IdCliente)
            contexto={"ListaLotes":Lotes}
            return render(request, 'Efficatia/ListaLotes.html', contexto)
    else:
        FormularioEdicion=FormularioLote(initial={'campo':LoteRegistrado.campo, 'lote':LoteRegistrado.lote, 'id_cliente':LoteRegistrado.id_cliente, 'link':LoteRegistrado.link})
        return render(request, 'Efficatia/EditarLote.html', {'FormularioEdicion':FormularioEdicion})

@login_required
def EliminarLote(request, ID):
    Lot= Lote.objects.get(id=ID)
    Lot.delete()
    cliente=Cliente.objects.get(user_id = request.user.id)

    IdCliente= cliente.id
    Lotes= Lote.objects.filter(id_cliente=IdCliente)
    contexto={"ListaLotes":Lotes}
    return render(request, 'Efficatia/ListaLotes.html', contexto)

def Notificacion(request):
    return render(request, 'Efficatia/Notificacion.html')