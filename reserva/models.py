from django.db import models

# Create your models here.

horas =[
    ('10:00 a 11:00','10:00 a 11:00'),
    ('11:00 a 12:00','11:00 a 12:00'),
    ('12:00 a 13:00','12:00 a 13:00'),
    ('13:00 a 14:00','13:00 a 14:00'),
    ('14:00 a 15:00','14:00 a 15:00'),
    ('15:00 a 16:00','15:00 a 16:00'),
    ('16:00 a 17:00','16:00 a 17:00'),
    ('17:00 a 18:00','17:00 a 18:00'),
    ('18:00 a 19:00','18:00 a 19:00'),
    ('19:00 a 20:00','19:00 a 20:00'),
]

tratamientos = [
    ('Pie de atleta','Pie de atleta'),
    ('Uña encarnada','Uña encarnada'),
    ('Ojo de gallo','Ojo de gallo'),
    ('Hongos en las uñas','Hongos en las uñas'),
    ('Mantención podológica','Mantención podológica'),
]

class Reservas(models.Model):
    nombre = models.CharField(max_length=50, null=False)
    mail = models.EmailField(null=False)
    telefono = models.CharField(max_length=9,null=False)
    fecha_reserva = models.DateField(null=False)

    hora_reserva = models.CharField(
        choices=horas,
        max_length=50,
        null=False,
        verbose_name="Hora de atención"
    )

    tratamiento = models.CharField(
        choices= tratamientos,
        max_length=100,
        null=False
    )

    domicilio = models.BooleanField(null=False)
    direccion = models.CharField(max_length=1000,null=True)
    precio_total = models.IntegerField(null=False)
    cantidad = models.IntegerField(null=False)


    def __str__(self):
        return f"{self.nombre} Tiene reserva el {self.fecha_reserva} entre las {self.hora_reserva}"
        
