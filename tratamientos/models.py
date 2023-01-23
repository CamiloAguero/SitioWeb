from django.db import models

# Create your models here.
class Tratamientos(models.Model):
    nombre = models.CharField(max_length=50)
    valor = models.IntegerField()
    descripcion = models.CharField(max_length=1000)
    imagen = models.ImageField(upload_to='tratamientos', blank=True, null=True)

    class Meta:
        db_table = 'tratamiento'
        verbose_name = 'Tratamiento'
        verbose_name_plural = 'Tratamientos'

    def __str__(self):
        return self.nombre