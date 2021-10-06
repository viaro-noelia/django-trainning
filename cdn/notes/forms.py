from django import forms
from .models import Alumno, Materias

class AlumnoCreateForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ("first_name", "last_name")

class MateriaCreateForm(forms.ModelForm):
    class Meta:
        model = Materias
        fields = ('clase', 'u1', 'u2', 'u3', 'u4', 'u5', 'alumno')

class MateriaUpdateForm(forms.ModelForm):
    #form for updating patients
    class Meta:
        model = Materias
        fields = ('clase', 'u1', 'u2', 'u3', 'u4', 'u5')
