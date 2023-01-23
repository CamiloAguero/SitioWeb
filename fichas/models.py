from django.db import models

# Create your models here.
class Ficha(models.Model):
    nombre = models.CharField(max_length=50,null=False)
    rut = models.CharField(max_length=50,null=False)
    telefono = models.IntegerField(null=False)
    nacimiento = models.DateField(null=False)
    imagen = models.ImageField(upload_to='ficha',null=True,blank=True)
    