from django import forms

#--------Formularios de Estudiantes------------
class EstudianteFormulario(forms.Form):
    dni = forms.CharField()
    apellidoPaterno = forms.CharField()
    apellidoMaterno = forms.CharField()
    nombres = forms.CharField()
    fechaNacimiento = forms.DateField()
    sexos = (
        ("Femenino","F"),
        ("Masculino","M"),
        ("Otro","O")
    )
    sexo = forms.ChoiceField(choices=sexos)
    carrera = forms.CharField()
    vigencia = forms.BooleanField()

class DeleteEstudiante(forms.Form):
    dni = forms.CharField()
    apellidoPaterno = forms.CharField(required=False)
    apellidoMaterno = forms.CharField(required=False)
    nombres = forms.CharField(required=False)
    fechaNacimiento = forms.DateField(required=False)
    sexos = (
        ("1","Femenino"),
        ("2","Masculino"),
        ("3","Otro")
    )
    sexo = forms.ChoiceField(choices=sexos)
    carrera = forms.CharField(required=False)
    vigencia = forms.BooleanField(required=False)

#--------Formularios de Carreras------------
class CarreraFormulario(forms.Form):
    codigo = forms.CharField()
    nombre = forms.CharField()
    duracion = forms.IntegerField(initial=5)

class DeleteCarrera (forms.Form):
    codigo = forms.CharField()
    nombre = forms.CharField(required=False)
    duracion = forms.IntegerField(required=False)

#--------Formularios de Cursos------------
class CursoFormulario (forms.Form):
    codigo = forms.CharField()
    nombre = forms.CharField()
    creditos = forms.IntegerField()
    docente = forms.CharField()

class DeleteCurso (forms.Form):
    codigo = forms.CharField()
    nombre = forms.CharField(required=False)
    creditos = forms.IntegerField(required=False)
    docente = forms.CharField(required=False)

#--------Formularios de Matrículas------------
class MatriculaFormulario (forms.Form):
    id = forms.CharField()
    estudiante = forms.CharField()
    curso = forms.CharField()
    # fechaMatricula = forms.DateTimeField()

class DeleteMatricula (forms.Form):
    id = forms.CharField()
    estudiante = forms.CharField(required=False)
    curso = forms.CharField(required=False)
    fechaMatricula = forms.DateTimeField(required=False)