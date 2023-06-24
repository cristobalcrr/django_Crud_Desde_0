from django.contrib import admin
from .models import Categoria, vehiculo, mantencion

# Register your models here.
admin.site.register(Categoria)
admin.site.register(vehiculo)
admin.site.register(mantencion)

