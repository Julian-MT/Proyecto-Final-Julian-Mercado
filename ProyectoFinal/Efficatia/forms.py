from django import forms

from Efficatia.models import Consulta


class FormularioConsulta(forms.form):
    class meta:
        model = Consulta
        fields = ('nombre', 'email', 'consulta')