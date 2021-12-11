from django import forms

#--------Formularios de Docente------------
class DocenteFormulario (forms.Form):
    matricula = forms.CharField()
    nombre = forms.CharField()
    titulo = forms.CharField()

class DeleteDocente (forms.Form):
    matricula = forms.CharField()
    nombre = forms.CharField(required=False)
    titulo = forms.CharField(required=False)

#--------Formularios de Facultad------------
class FacultadFormulario (forms.Form):
    id = forms.CharField()
    nombre = forms.CharField()

class DeleteFacultad (forms.Form):
    id = forms.CharField()
    nombre = forms.CharField(required=False)


#--------Formularios de Grupo------------
class GrupoFormulario (forms.Form):
    numero = forms.CharField()

class DeleteGrupo (forms.Form):
    numero = forms.CharField()


#--------Formularios de Materia------------
class MateriaFormulario (forms.Form):
    id = forms.CharField()
    nombre = forms.CharField()

class DeleteMateria (forms.Form):
    id = forms.CharField()
    nombre = forms.CharField(required=False)
