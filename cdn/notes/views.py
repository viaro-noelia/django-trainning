from django.shortcuts import render
from notes.models import Alumno, Materias
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import AlumnoCreateForm, MateriaUpdateForm, MateriaCreateForm
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
default_data = [
    {'id': 5, 'first_name': 'Gerardo','last_name':'Ramirez'},
    {'id': 1, 'first_name': 'Luis','last_name':'Sanabria'},
    {'id': 2, 'first_name': 'Orlando','last_name':'Moises'},
    {'id': 3, 'first_name': 'Montserrath','last_name':'Olivo'},
    {'id': 4, 'first_name': 'Emilio','last_name':'Guzman'},
]
clases = {'MT': 'Matematicas','FS': 'Fisica','BL': 'Biologia','CL': 'Calculo','ES': 'Español','EN': 'Ingles','HS': 'Historia',}

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
                            'clase': clases[materia.clase],
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
        context.append({'name': alumno, 'id': alumno.id, 'control': alumno.control_number})
    return render(request, 'notes/home.html', {'alumnos': context})

def AlumnoNew(request):
    if request.method == 'POST':
        print(request.POST['name_input'],request.POST['last_name_input'],request.POST['control_number'])
        try:
            print(Alumno.objects.get(control_number=request.POST['control_number']))
            return render(request, 'notes/alumno_error.html')
        except ObjectDoesNotExist:
            new_alumno = Alumno(first_name=request.POST['name_input'], last_name=request.POST['last_name_input'], control_number = request.POST['control_number'])
            new_alumno.save()
            print('Alumno creado correctamente')
            return render(request, 'notes/alumno_success.html')
    return render(request, 'notes/alumno_new.html')

def NotesEdit(request, pk):
    if request.method == 'POST':
        print('Metodo POST', pk)
        materia = Materias.objects.get(id=pk)
        materia.u1 = request.POST['u1']
        materia.u2 = request.POST['u2']
        materia.u3 = request.POST['u3']
        materia.u4 = request.POST['u4']
        materia.u5 = request.POST['u5']
        materia.save()
        return render(request, 'notes/notes_success.html')
    elif request.method == 'GET':
        materia = Materias.objects.get(id=pk)
        context =  {'alumno' : materia.alumno.first_name + ' ' + materia.alumno.last_name,
                    'clase': clases[materia.clase],
                    'u1': materia.u1,
                    'u2': materia.u2,
                    'u3': materia.u3,
                    'u4': materia.u4,
                    'u5': materia.u5,
                    }
        print(context)
        return render(request, 'notes/notes_edit.html', {'data': context})

def NotesNew(request, pk):
    alumno = Alumno.objects.get(id=pk)
    if request.method == 'POST':
        print('Metodo POST', pk)
        for key in request.POST:
            print(key, request.POST[key])
        new_materia =  Materias(clase=request.POST['select'],
                                u1 = request.POST['u1'],
                                u2 = request.POST['u2'],
                                u3 = request.POST['u3'],
                                u4 = request.POST['u4'],
                                u5 = request.POST['u5'],
                                alumno = alumno,
                                )
        new_materia.save()
        return render(request, 'notes/notes_success.html')
    elif request.method == 'GET':
        context =  {'alumno' : alumno.first_name + ' ' + alumno.last_name}
        print(context)
        materias = Materias.objects.all().filter(alumno=alumno)
        actual_materia = []
        for materia in materias:
            actual_materia.append(materia.clase)
        print(actual_materia)
        select_list = []
        for key in clases:
            if key not in actual_materia:
                select_list.append({'key': key, 'value': clases[key]})
        print(select_list)
        if len(select_list) == 0:
            return render(request, 'notes/notes_all.html', {'data': context, 'select_list': select_list})
        return render(request, 'notes/notes_new.html', {'data': context, 'select_list': select_list})

def notes(request,pk):
    print('Buscando datos de usuario con clave: ', pk)
    alumno = Alumno.objects.get(id=pk)
    materias = Materias.objects.all().filter(alumno=alumno)
    result = []
    for item in materias:
        promedio = (item.u1 + item.u2 + item.u3 + item.u4 + item.u5) / 5
        status = 'Necesita recuperacion'
        if promedio >= 75:
            status = 'Ganada'
        elif promedio < 55:
            status = 'Perdida'
        result.append({'clase' : clases[item.clase],'u1' : item.u1, 'u2' : item.u2, 'u3' : item.u3, 'u4' : item.u4, 'u5' : item.u5, 'promedio': promedio, 'status': status, 'id': item.id})
    # print(Materias.objects.get(alumno=alumno))
    print(result)
    return render(request, 'notes/notes_list.html', {'materias': result, 'name': alumno, 'alumno_id': alumno.id})

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
    