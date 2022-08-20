from django.contrib import admin
from concursos.models import categoria,participantes,calificacion_acordeonero,calificacion_cancion,calificacion_piqueria
# Register your models here.
admin.site.register(categoria)
admin.site.register(participantes)
admin.site.register(calificacion_acordeonero)
admin.site.register(calificacion_cancion)
admin.site.register(calificacion_piqueria)