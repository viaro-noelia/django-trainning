from django.shortcuts import render
from notes.models import Alumno, Materias
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import AlumnoCreateForm, MateriaUpdateForm, MateriaCreateForm

default_data = [
    {'id': 5, 'first_name': 'Gerardo','last_name':'Ramirez'},
    {'id': 1, 'first_name': 'Luis','last_name':'Sanabria'},
    {'id': 2, 'first_name': 'Orlando','last_name':'Moises'},
    {'id': 3, 'first_name': 'Montserrath','last_name':'Olivo'},
    {'id': 4, 'first_name': 'Emilio','last_name':'Guzman'},
]
def general(request):
    data = Alumno.objects.all()
    print(data)
    context = []
    for alumno in data:
        materias = Materias.objects.all().filter(alumno=alumno)
        for materia in materias:
            promedio = (materia.u1 + materia.u2 + materia.u3 + materia.u4 + materia.u5) / 5
            status = 'Necesita recuperacion'
            if promedio > 75:
                status = 'Ganada'
            elif promedio < 55:
                status = 'Perdida'
            context.append({'name': alumno, 
                            'id': alumno.id, 
                            'clase': materia.clase,
                            'u1': materia.u1,
                            'u2': materia.u2,
                            'u3': materia.u3,
                            'u4': materia.u4,
                            'u5': materia.u5,
                            'promedio': promedio,
                            'status': status
                            })
    return render(request, 'notes/general_table.html', {'alumnos': context})

def index(request):
    data = Alumno.objects.all()
    print(data)
    context = []
    for alumno in data:
        context.append({'name': alumno, 'id': alumno.id})
    return render(request, 'notes/home.html', {'alumnos': context})
def notes(request,pk):
    print('Buscando datos de usuario con clave: ', pk)
    alumno = Alumno.objects.get(id=pk)
    materias = Materias.objects.all().filter(alumno=alumno)
    result = []
    for item in materias:
        promedio = (item.u1 + item.u2 + item.u3 + item.u4 + item.u5) / 5
        status = 'Necesita recuperacion'
        if promedio > 75:
            status = 'Ganada'
        elif promedio < 55:
            status = 'Perdida'
        result.append({'clase' : item.clase,'u1' : item.u1, 'u2' : item.u2, 'u3' : item.u3, 'u4' : item.u4, 'u5' : item.u5, 'promedio': promedio, 'status': status, 'id': item.id})
    # print(Materias.objects.get(alumno=alumno))
    print(result)
    return render(request, 'notes/notes_list.html', {'materias': result, 'name': alumno})

class AlumnoCreate(CreateView):
    model = Alumno
    template_name = 'notes/alumno_create.html'
    form_class = AlumnoCreateForm
    
class AlumnoDelete(DeleteView):
    model = Alumno
    template_name = 'notes/alumno_delete.html'
    success_url = "/"

class MateriaUpdate(UpdateView):
    model = Materias
    template_name = 'notes/notes_update.html'
    form_class = MateriaUpdateForm

class MateriaCreate(CreateView):
    model = Materias
    template_name = 'notes/notes_create.html'
    form_class = MateriaCreateForm
    