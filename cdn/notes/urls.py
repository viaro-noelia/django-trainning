from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("general/", views.general, name="general"),
    path("alumno/create", views.AlumnoCreate.as_view(), name="alumnocreate"),
    path("alumno/new", views.AlumnoNew, name="alumnonew"),
    path("alumno/delete/<pk>", views.AlumnoDelete.as_view(), name="alumnodelete"),
    path("notes/new/<pk>", views.NotesNew, name="notesnew"),
    path("notes/edit/<pk>", views.NotesEdit, name="notesedit"),
    path("notes/list/<pk>", views.notes, name="noteslist"),
    path("notes/update/<pk>", views.MateriaUpdate.as_view(), name="notesupdate"),
    path("notes/create", views.MateriaCreate.as_view(), name="notescreate"),

]