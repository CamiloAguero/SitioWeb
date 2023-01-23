from django import forms
from .models import Ficha

class formato_fecha(forms.DateTimeInput):
    input_type = 'date'

class formulario_fichas(forms.ModelForm):

    nacimiento = forms.DateTimeField(label="Fecha de nacimiento",required=True,widget=formato_fecha())

    atencion = forms.DateTimeField(label="Ultima Atención Podologica",required=True,widget=formato_fecha())

    observacion = forms.CharField(label='Observaciones', widget=forms.Textarea)

    class Meta:
            model = Ficha
            fields = ('nombre','rut','telefono','edad','direccion','imagen','morbido','cronico','alergia','medicamentos','amputacion')