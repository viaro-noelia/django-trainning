from django.shortcuts import render
from notes.models import Alumno,Notes
# Create your views here.

default_data = [
    {'id': 0, 'first_name': 'Gerardo','last_name':'Ramirez'},
    {'id': 1, 'first_name': 'Luis','last_name':'Sanabria'},
    {'id': 2, 'first_name': 'Orlando','last_name':'Moises'},
    {'id': 3, 'first_name': 'Montserrath','last_name':'Olivo'},
    {'id': 4, 'first_name': 'Emilio','last_name':'Guzman'},
]
def index(request):
    data = Alumno.objects.all()
    print(data)
    print(default_data)
    return render(request, 'notes/home.html', {'alumnos': default_data})