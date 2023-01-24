from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

def enviar_mail(**kwargs):
    asunto = "RESERVA PODOLÓGICA PARA " + kwargs.get("nombre").upper()
    mensaje = render_to_string("emails/detalle.html",{
        "nombre": kwargs.get("nombre"),
        "mail": kwargs.get("mail"),
        "telefono": kwargs.get("telefono"),
        "fecha": kwargs.get("fecha"),
        "hora": kwargs.get("hora"),
        "tratamiento": kwargs.get("tratamiento"),
        "domicilio": kwargs.get("domicilio"),
        "direccion": kwargs.get("direccion"),
        "precio": kwargs.get("precio"),
        "tipo": kwargs.get("tipo")
    })
    mensaje_propio = render_to_string("emails/propio.html",{
        "nombre": kwargs.get("nombre"),
        "mail": kwargs.get("mail"),
        "telefono": kwargs.get("telefono"),
        "fecha": kwargs.get("fecha"),
        "hora": kwargs.get("hora"),
        "tratamiento": kwargs.get("tratamiento"),
        "domicilio": kwargs.get("domicilio"),
        "direccion": kwargs.get("direccion"),
        "precio": kwargs.get("precio"),
        "tipo": kwargs.get("tipo")
    })

    mensaje_texto = strip_tags(mensaje)
    mensaje_texto_propio = strip_tags(mensaje_propio)
    from_email = "podologiaval@outlook.es"
    to = kwargs.get("mail")
    send_mail(asunto,mensaje_texto,from_email,[to],html_message= mensaje)
    send_mail(asunto,mensaje_texto_propio,from_email,['camilo.aguero02@inacapmail.cl'],html_message= mensaje_propio)