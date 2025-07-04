from django.forms import ModelForm
from django import forms

from administrativo.models import Matricula,Estudiante,Modulo

class MatriculaForm(ModelForm):
    class Meta:
        model = Matricula
        fields = ['estudiante', 'modulo', 'comentario', 'costo']


class MatriculaEditForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(MatriculaEditForm, self).__init__(*args, **kwargs)
        self.initial['estudiante'] = self.instance.estudiante
        self.fields["estudiante"].widget = forms.widgets.HiddenInput()
        self.initial['modulo'] = self.instance.modulo
        self.fields["modulo"].widget = forms.widgets.HiddenInput()

    class Meta:
        model = Matricula
        fields = ['estudiante', 'modulo', 'comentario', 'costo']
        widgets = {
            'comentario': forms.Textarea(attrs={
                'rows': 4,
                'cols': 40,
                'placeholder': 'Escribe aquí tu comentario...'
            }),
            'costo': forms.NumberInput(attrs={
                'placeholder': 'Ingrese el costo de la matrícula',
                'min': 0,
                'step': '0.01'
            })
        }

class EstudianteForm(forms.ModelForm):
    class Meta:
        model = Estudiante
        fields = ['nombre', 'apellido', 'cedula', 'edad', 'tipo_estudiante']
        widgets = {
            'tipo_estudiante': forms.Select(),
            'cedula': forms.TextInput(attrs={'placeholder': 'Ej: 1101234567'}),
            'edad': forms.NumberInput(attrs={'min': 0}),
        }

class ModuloForm(forms.ModelForm):
    class Meta:
        model = Modulo
        fields = ['nombre']
        widgets = {
            'nombre': forms.Select(attrs={
                'placeholder': 'Seleccione un módulo'
            })
        }
