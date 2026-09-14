from django.contrib import admin
from .models import Repuesto, Proveedor

admin.site.register(Proveedor)
admin.site.register(Repuesto)

# Register your models here.
