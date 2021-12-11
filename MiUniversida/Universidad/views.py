from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from Universidad.models import *
from Universidad.formularios import *

# Create your views here.
#---------Docente-------------
def AgregarDocente(request):
    if request.method == "POST":
        formulario = DocenteFormulario(request.POST)

        if formulario.is_valid():
            matricula = formulario.cleaned_data.get("matricula", "")
            nombre = formulario.cleaned_data.get("nombre", "")
            titulo = formulario.cleaned_data.get("titulo", "")

            insert = Docente(matricula=matricula, nombre=nombre, titulo=titulo )
            insert.save()
            return render(request, "Principal.html")
    else:
        formulario = DocenteFormulario()
    return render(request, "AgregarDocente.html", {"formDocente": formulario})

def EliminarDocente(request):
    if request.method == "POST":
        formulario = DeleteDocente(request.POST)

        if formulario.is_valid():
            matricula = formulario.cleaned_data.get("matricula", "")
            borrar = Docente.objects.get(matricula=matricula)
            borrar.delete()
            return render(request, "Principal.html")

    else:
        formulario = DeleteDocente()
    return render(request, "EliminarDocente.html", {"formDltDocente": formulario})

def MostrarDocentes(request):
    docentes = Docente.objects.all()
    return render(request, "Docentes.html", {"docentes": docentes})

#---------Facultad-------------
def AgregarFacultad(request):
    if request.method == "POST":
        formulario = FacultadFormulario(request.POST)

        if formulario.is_valid():
            id = formulario.cleaned_data.get("id", "")
            nombre = formulario.cleaned_data.get("nombre", "")

            insert = Facultad(id=id, nombre=nombre)
            insert.save()
            return render(request, "Principal.html")
    else:
        formulario = FacultadFormulario()
    return render(request, "AgregarFacultad.html", {"formFacultad": formulario})

def EliminarFacultad(request):
    if request.method == "POST":
        formulario = DeleteFacultad(request.POST)

        if formulario.is_valid():
            id = formulario.cleaned_data.get("id", "")
            borrar = Facultad.objects.get(id=id)
            borrar.delete()
            return render(request, "Principal.html")

    else:
        formulario = DeleteFacultad()
    return render(request, "EliminarFacultad.html", {"formDltFacul": formulario})

def MostrarFacultades(request):
    facultades = Facultad.objects.all()
    return render(request, "Facultad.html", {"facultades": facultades})

#---------Grupo-------------
def AgregarGrupo(request):
    if request.method == "POST":
        formulario = GrupoFormulario(request.POST)

        if formulario.is_valid():
            numero = formulario.cleaned_data.get("numero", "")

            insert = Grupo(numero=numero)
            insert.save()
            return render(request, "Principal.html")
    else:
        formulario = GrupoFormulario()
    return render(request, "AgregarGrupo.html", {"formGrupo": formulario})

def EliminarGrupo(request):
    if request.method == "POST":
        formulario = DeleteGrupo(request.POST)

        if formulario.is_valid():
            numero = formulario.cleaned_data.get("numero", "")
            borrar = Grupo.objects.get(numero=numero)
            borrar.delete()
            return render(request, "Principal.html")

    else:
        formulario = DeleteGrupo()
    return render(request, "EliminarGrupo.html", {"formDltGrupo": formulario})

def MostrarGrupos(request):
    grupos = Grupo.objects.all()
    return render(request, "Grupos.html", {"grupos": grupos})

#---------Materia-------------
def AgregarMateria(request):
    if request.method == "POST":
        formulario = MateriaFormulario(request.POST)

        if formulario.is_valid():
            id = formulario.cleaned_data.get("id", "")
            nombre = formulario.cleaned_data.get("nombre", "")

            insert = Materia(id=id, nombre=nombre)
            insert.save()
            return render(request, "Principal.html")
    else:
        formulario = MateriaFormulario()
    return render(request, "AgregarMateria.html", {"formMateria": formulario})

def EliminarMateria(request):
    if request.method == "POST":
        formulario = DeleteMateria(request.POST)

        if formulario.is_valid():
            id = formulario.cleaned_data.get("id", "")
            borrar = Materia.objects.get(id=id)
            borrar.delete()
            return render(request, "Principal.html")

    else:
        formulario = DeleteMateria()
    return render(request, "EliminarMateria.html", {"formDltMateria": formulario})

def MostrarMaterias(request):
    materias = Materia.objects.all()
    return render(request, "Materias.html", {"materias": materias})