from django.urls import path
from Efficatia.views import inicio, FormularioConsultaa, Informacion, RegistroCliente, LogInCliente, RegistroUsuario, RegistroUsuarioExitoso, LogOutCliente, ListaLotes, CrearLote, EliminarLote, EditarLote, Notificacion


urlpatterns = [
    
    path('', inicio, name='Inicio'  ),
    path('FormularioConsulta/', FormularioConsultaa, name='FormularioConsulta'),
    path('Informacion/', Informacion, name= 'Informacion'),
    path('RegistroCliente/', RegistroCliente, name= 'RegistroCliente'),
    path('LogIn/', LogInCliente, name='LogIn'),
    path('RegistroUsuario/', RegistroUsuario, name='RegistroUsuario'),
    path('Logout/', LogOutCliente, name='LogOut'),
    path('ListaLotes/', ListaLotes, name='ListaLotes'),
    path('CrearLote/', CrearLote, name='CrearLote' ),
    path('RegistroUsuarioExitoso/', RegistroUsuarioExitoso, name='RegistroUsuarioExitoso'),
    path('EditarLote/<ID>', EditarLote, name='EditarLote' ),
    path('EliminarLote/<ID>', EliminarLote, name='EliminarLote'),
    path('Notificacion/', Notificacion, name='Notificacion' ),

]