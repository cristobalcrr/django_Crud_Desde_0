from django import forms
from django.forms import ModelForm
from .models import vehiculo

class VehiculoForm(ModelForm):
    class Meta:
        model = vehiculo
        fields =['patente','marca','modelo','categoria']

        widget = {
            'patente': forms.TextInput(attrs={'class':'form-control'}),
            'marca': forms.TextInput(attrs={'class':'form-control'}),
            'modelo': forms.TextInput(attrs={'class':'form-control'}),
            'categoria': forms.Select(attrs={'class':'form-control'}),
        }