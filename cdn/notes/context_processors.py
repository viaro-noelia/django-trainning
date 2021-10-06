from .models import Alumno, Materias


def alumnos(request):
    alumnos = Alumno.objects.all()
    data = [{'name': alumno, 'id': alumno.id, 'control': alumno.control_number} for alumno in alumnos]
    print(data)
    return {'alumnos': data}