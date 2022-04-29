from django.urls import path
from Efficatia.views import inicio, FormularioConsulta, Informacion, RegistroCliente, LogInCliente, RegistroUsuario, LogOutCliente, ListaLotes


urlpatterns = [
    
    path('', inicio, name='Inicio'  ),
    path('FormularioConsulta/', FormularioConsulta, name='FormularioConsulta'),
    path('Informacion/', Informacion, name= 'Informacion'),
    path('RegistroCliente/', RegistroCliente, name= 'RegistroCliente'),
    path('LogIn/', LogInCliente, name='LogIn'),
    path('RegistroUsuario/', RegistroUsuario, name='RegistroUsuario'),
    path('Logout/', LogOutCliente, name='LogOut'),
    path('ListaLotes/', ListaLotes, name='ListaLotes')
    

]