from django.urls import path
from Efficatia.views import inicio, FormularioConsulta
urlpatterns = [
    
    path('', inicio, name='Inicio'  ),
    path('FormularioConsulta/', FormularioConsulta, name='FormularioConsulta')
    

]