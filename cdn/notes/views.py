from django.shortcuts import render
from notes.models import Alumno,Notes
# Create your views here.
def index(request):
    data = Alumno.objects.all()
    print(data)
    return render(request, 'notes/home.html')