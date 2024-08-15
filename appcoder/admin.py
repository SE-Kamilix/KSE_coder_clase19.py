from django.contrib import admin
from .models import Curso, Estudiante, Profesor, Entregable


class CursoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "comisión")

# Register your models here.

admin.site.register(Curso, CursoAdmin)
admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Entregable)