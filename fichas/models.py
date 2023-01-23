from django.db import models

# Create your models here.

cronicas=[
    ("NO","NO"),
    ("XD","XD"),
    ("HTA","HTA"),
]

opcion=[
    ("NO","NO"),
    ("SI","SI"),
]

class Ficha(models.Model):
    nombre = models.CharField(max_length=50,null=False, verbose_name="Nombre")
    rut = models.CharField(max_length=50,null=False, verbose_name="Rut")
    telefono = models.IntegerField(null=False, verbose_name="Celular")
    nacimiento = models.DateField(null=False, verbose_name="Fecha de nacimiento")
    edad = models.IntegerField(null=False, verbose_name="Edad")
    direccion = models.CharField(max_length=1000,null=False)
    imagen = models.ImageField(upload_to='ficha',null=True,blank=True, verbose_name="Adjuntar imagen")
    morbido = models.CharField(null=True, verbose_name="Morbidos",choices=opcion,default='NO',max_length=10)
    cronico = models.CharField(choices=cronicas,null=True, verbose_name="Enf. Cronicas", default='NO',max_length=50)
    alergia = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Alergias")
    medicamentos = models.CharField(max_length=1000, null=True, blank=True, verbose_name="Medicamentos")
    atencion = models.DateField(null=False, verbose_name="Ultima Atención Podologica")
    amputacion = models.CharField(null=True,blank=True, verbose_name="Amputacion",choices=opcion,default='NO',max_length=10)
    observacion = models.CharField(null=False, verbose_name="Observaciones", max_length=100000)

    class Meta:
        verbose_name: 'Ficha'