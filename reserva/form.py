from django import forms
from .models import Reservas

class formato_fecha(forms.DateTimeInput):
    input_type = 'date'

class formulario_reserva(forms.ModelForm):
    nombre = forms.CharField(label="Nombre", required=True,widget=forms.TextInput(attrs={'placeholder':'Nombre Completo'}))

    mail = forms.EmailField(label="Correo Electronico",required=True, widget=forms.TextInput(attrs={'placeholder':'Correo Electronico'}))

    telefono = forms.CharField(label="Celular",required=True,max_length='9', widget=forms.TextInput(attrs={'placeholder':'Celular +56'}))

    fecha_reserva = forms.DateTimeField(label="Fecha de atención",required=True,widget=formato_fecha())

    domicilio = forms.BooleanField(label="¿Requiere atencion a domicilio?",required=False)

    direccion = forms.CharField(label="Direccion", required=False,widget=forms.TextInput(attrs={'placeholder':'Direccion de Domicilio'}))

    cantidad = forms.IntegerField(label="Cantidad", required=True,widget=forms.NumberInput())

    class Meta:
        model = Reservas
        fields = ('hora_reserva','tratamiento')