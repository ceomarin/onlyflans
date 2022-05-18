from distutils.command.upload import upload
from django.db import models

# Create your models here.
opciones_consultas = [
    [0,'consulta'],
    [1,'reclamo'],
    [2,'sugerencia'],
    [3,'felicitaciones']
]
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre

class Flan(models.Model):
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='productos')

    def __str__(self):
        return self.nombre