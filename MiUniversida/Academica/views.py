from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from Academica.models import *
from Academica.formularios import *
# from Universidad.models import *
# from Universidad.formularios import *

# Create your views here.

def base(request):
    return render(request, "base.html")

#---------Carrera-------------
def AgregarCarrera(request):
    if request.method == "POST":
        formulario = CarreraFormulario(request.POST)

        if formulario.is_valid():
            codigo = formulario.cleaned_data.get("codigo", "")
            nombre = formulario.cleaned_data.get("nombre", "")
            duracion = formulario.cleaned_data.get("duracion", "")

            insert = Carrera(codigo=codigo, nombre=nombre, duracion=duracion)
            insert.save()
            return render(request, "Principal.html")
    else:
        formulario = CarreraFormulario()
    return render(request, "AgregarCarrera.html", {"form": formulario})

def EliminarCarrera(request):
    if request.method == "POST":
        formulario = DeleteCarrera(request.POST)

        if formulario.is_valid():
            codigo = formulario.cleaned_data.get("codigo", "")
            borrar = Carrera.objects.get(codigo=codigo)
            borrar.delete()
            return render(request, "Principal.html")

    else:
        formulario = DeleteCarrera()
    return render(request, "EliminarCarrera.html", {"formE": formulario})

def MostrarCarreras(request):
    carreras = Carrera.objects.all()
    return render(request, "Carreras.html", {"carreras": carreras})

#---------Estudiante-------------
def AgregarEstudiante(request):
    if request.method == "POST":
        formulario = EstudianteFormulario(request.POST)

        if formulario.is_valid():
            dni = formulario.cleaned_data.get("dni", "")
            apellidopaterno = formulario.cleaned_data.get("apellidoPaterno", "")
            apellidomaterno = formulario.cleaned_data.get("apellidoMaterno", "")
            nombres = formulario.cleaned_data.get("nombres", "")
            fechanacimient = formulario.cleaned_data.get("fechaNacimiento", "")
            sexo = formulario.cleaned_data.get("sexo", "")
            carrera = formulario.cleaned_data.get("carrera", "")
            vigencia = formulario.cleaned_data.get("vigencia", "")

            insert = Estudiante(dni=dni, apellidoPaterno=apellidopaterno, apellidoMaterno=apellidomaterno, nombres=nombres, fechaNacimiento=fechanacimient, sexo=sexo, carrera_id=carrera, vigencia=vigencia)
            insert.save()
            return render(request, "Principal.html")
    else:
        formulario = EstudianteFormulario()
    return render(request, "AgregarEstudiante.html", {"formEstudiante": formulario})

def EliminarEstudiante(request):
    if request.method == "POST":
        formulario = DeleteEstudiante(request.POST)

        if formulario.is_valid():
            dni = formulario.cleaned_data.get("dni", "")
            borrar = Estudiante.objects.get(dni=dni)
            borrar.delete()
            return render(request, "Principal.html")

    else:
        formulario = DeleteEstudiante()
    return render(request, "EliminarEstudiante.html", {"formDltEstudiante": formulario})

def MostrarEstudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, "Estudiantes.html", {"estudiantes": estudiantes})

#---------Curso-------------
def AgregarCurso(request):
    if request.method == "POST":
        formulario = CursoFormulario(request.POST)

        if formulario.is_valid():
            codigo = formulario.cleaned_data.get("codigo", "")
            nombre = formulario.cleaned_data.get("nombre", "")
            creditos = formulario.cleaned_data.get("creditos", "")
            docente = formulario.cleaned_data.get("docente", "")

            insert = Curso(codigo=codigo, nombre=nombre, creditos=creditos, docente=docente)
            insert.save()
            return render(request, "Principal.html")
    else:
        formulario = CursoFormulario()
    return render(request, "AgregarCurso.html", {"formCurso": formulario})

def EliminarCurso(request):
    if request.method == "POST":
        formulario = DeleteCarrera(request.POST)

        if formulario.is_valid():
            codigo = formulario.cleaned_data.get("codigo", "")
            borrar = Curso.objects.get(codigo=codigo)
            borrar.delete()
            return render(request, "Principal.html")

    else:
        formulario = DeleteCurso()
    return render(request, "EliminarCurso.html", {"formDltCurso": formulario})

def MostrarCurso(request):
    cursos = Curso.objects.all()
    return render(request, "Cursos.html", {"cursos": cursos})

#---------Matrícula-------------
def AgregarMatricula(request):
    if request.method == "POST":
        formulario = MatriculaFormulario(request.POST)

        if formulario.is_valid():
            id = formulario.cleaned_data.get("estudiante", "")
            estudiante = formulario.cleaned_data.get("estudiante", "")
            curso = formulario.cleaned_data.get("curso", "")

            insert = Matricula(id=id, estudiante_id=estudiante, curso_id=curso)
            insert.save()
            return render(request, "Principal.html")
    else:
        formulario = MatriculaFormulario()
    return render(request, "AgregarMatricula.html", {"formMatricula": formulario})

def EliminarMatricula(request):
    if request.method == "POST":
        formulario = DeleteMatricula(request.POST)

        if formulario.is_valid():
            id = formulario.cleaned_data.get("id", "")
            borrar = Matricula.objects.get(id=id)
            borrar.delete()
            return render(request, "Principal.html")

    else:
        formulario = DeleteMatricula()
    return render(request, "EliminarMatricula.html", {"formMat": formulario})

def MostrarMatriculas(request):
    matriculas = Matricula.objects.all()
    return render(request, "Matriculas.html", {"matriculas": matriculas})

def Principal(request):
    return render(request, "Principal.html")
