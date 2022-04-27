from django import forms

from Efficatia.models import Consulta, Cliente, Lote


class FormularioConsulta(forms.Form):
    class meta:
        model = Consulta
        fields = ('nombre', 'email', 'consulta')

class FormularioRegistroCliente(forms.Form):
    nombre=forms.CharField(max_length=30)
    email=forms.EmailField()
    empresa=forms.CharField(max_length= 500)


class FormularioLote(forms.Form):
    class meta:
        model = Lote
        fields = ('campo', 'lote', 'id_cliente', 'link')
