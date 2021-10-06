from django.contrib import admin

from .models import Alumno, Materias, Notes

admin.site.register(Alumno)
admin.site.register(Notes)
admin.site.register(Materias)

# Register your models here.
