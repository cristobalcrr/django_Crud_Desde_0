from django import forms
from django.forms import DateTimeInput, ModelForm
from .models import mantencion, vehiculo

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

class mantencionForm(ModelForm):
    class Meta:
        model = mantencion
        field = ['id_mant', 'desc_mantencion', 'fecha_mant', 'id_patente']
        widget = {
            'id_mant': forms.NumberInput(attrs={'class':'form-control'}),
            'desc_mantencion': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_mant': forms.DateInput(attrs={'class':'form-control'}),
            'id_patente': forms.Select(attrs={'class':'form-control'}),
        }