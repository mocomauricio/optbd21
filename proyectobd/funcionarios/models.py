from django.db import models
from django.utils.html import mark_safe

# Create your models here.
class Funcionario(models.Model):
	nombre = models.CharField(max_length=256)
	apellido = models.CharField(max_length=256)
	cedula = models.CharField(max_length=256)
	email = models.EmailField()
	telefono = models.CharField(max_length=256)
	direccion = models.CharField(max_length=512)
	fecha_nacimiento = models.DateField()
	activo = models.BooleanField(default=True)

	def __str__(self):
		return self.nombre + " " + self.apellido

class Marcacion(models.Model):
	funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE, related_name="marcaciones")
	fecha = models.DateField()
	hora = models.TimeField()
	temperatura = models.DecimalField(max_digits=5, decimal_places=2)
	imagen = models.ImageField(upload_to='fotos')

	def __str__(self):
		return self.funcionario.nombre + " " + self.funcionario.apellido

	def imagen_tag(self):
		return mark_safe('<img src="/media/%s" width="150" height="150" />' % (self.imagen))