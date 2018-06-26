from django import forms
from .models import Codigo


class CodigoForm(forms.ModelForm):

    class Meta:
        model = Codigo
        fields = (
            'nombre',
            'apellido',
            'celular',
            'correo',
            'terminos',
            'politica'
            )
