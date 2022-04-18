from django.urls import path
from Efficatia.views import inicio, FormularioConsulta, Informacion, RegistroCliente
urlpatterns = [
    
    path('', inicio, name='Inicio'  ),
    path('FormularioConsulta/', FormularioConsulta, name='FormularioConsulta'),
    path('Informacion/', Informacion, name= 'Informacion'),
    path('RegistroCliente/', RegistroCliente, name= 'RegistroCliente'),
    

]