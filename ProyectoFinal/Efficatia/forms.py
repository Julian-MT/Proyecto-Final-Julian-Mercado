from django import forms

from Efficatia.models import Consulta, Cliente, Lote, Vuelo


class FormularioConsulta(forms.Form):
    nombre=forms.CharField(max_length=30)
    email=forms.EmailField()
    consulta=forms.CharField(max_length= 500)
        

class FormularioRegistroCliente(forms.Form):
    nombre=forms.CharField(max_length=30)
    email=forms.EmailField()
    empresa=forms.CharField(max_length= 500)


class FormularioLote(forms.ModelForm):
    class Meta:
        model=Lote
        fields=('id_cliente', 'campo', 'lote', 'link' )

class FormularioVuelo(forms.ModelForm):
    class Meta:
        model=Vuelo
        fields=('id_lote', 'fecha')

