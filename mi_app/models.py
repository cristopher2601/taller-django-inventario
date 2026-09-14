from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nombre

class Repuesto(models.Model):
    codigo = models.CharField(max_length=50, unique=True, verbose_name="Código / Ref")
    nombre = models.CharField(max_length=150)
    categoria = models.CharField(max_length=50)
    cantidad = models.IntegerField(default=0)
    precio = models.IntegerField(default=0)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

# Create your models here.
