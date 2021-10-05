from django.db import models

# Create your models here.
class Alumno(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    def __str__(self):
        return self.first_name + ', ' + self.last_name

class Notes(models.Model):
    clase = models.CharField(max_length=200)
    unidad = models.IntegerField(default=0)
    nota = models.IntegerField(default=0)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    def __str__(self):
        return self.clase
    class Meta:
        ordering = ["unidad"]