from django import forms

class FormularioCurso(forms.Form):
        titulo = forms.CharField()
        genero = forms.CharField()
        director= forms.CharField()