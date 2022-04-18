from django import forms

from Efficatia.models import Consulta, Cliente, Lote


class FormularioConsulta(forms.Form):
    class meta:
        model = Consulta
        fields = ('nombre', 'email', 'consulta')

class FormularioRegistroCliente(forms.Form):
    class meta:
        model = Cliente
        fields = ('nombre', 'email', 'empresa')

class FormularioLote(forms.Form):
    class meta:
        model = Lote
        fields = ('campo', 'lote', 'id_cliente', 'link')
