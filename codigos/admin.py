from django.contrib import admin
from .models import Codigo


class CodigoAdmin(admin.ModelAdmin):
    model = Codigo
    list_display = ('nombre', 'apellido', 'correo', 'celular', 'codigo')
    search_fields = ('nombre', 'apellido', 'correo', 'celular', 'codigo')


admin.site.register(Codigo, CodigoAdmin)
