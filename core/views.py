from django.shortcuts import render, redirect
from .models import vehiculo, mantencion
from .forms import VehiculoForm, mantencionForm


# Create your views here.
class persona:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
        super().__init__()


def home(request):

    vehiculos = vehiculo.objects.all()

    hijo=persona("Juan Perez", "7")
    lista=["Lasaña","Charquican","Porotos Granados"]
    contexto={"nombre":"Claudia Andrea", "comidas":lista, "hijo":hijo, "vehiculos":vehiculos}

    return render(request, 'core/home.html',contexto)

def form_vehiculo(request):
    datos = {
        'form': VehiculoForm()
    }

    if request.method=='POST':
        formulario= VehiculoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardado Correctamente"


    return render(request, 'core/form_vehiculo.html', datos)

def form_mod_vehiculo(request, id):
    auto = vehiculo.objects.get(patente=id)
    datos = {
        'form': VehiculoForm(instance=auto)
    }
    if request.method=='POST':
        formulario= VehiculoForm(data=request.POST, instance=auto)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Modificado Correctamente"

    return render(request, 'core/form_mod_vehiculo.html', datos)


def listar_mod_vehiculo(request):
    vehiculos = vehiculo.objects.all()
    datos = {
        "vehiculos":vehiculos
    }
    return render(request, 'core/listar_mod_vehiculo.html',datos)

def form_del_vehiculo(request, id):
    aut = vehiculo.objects.get(patente=id)
    datos = {
        'form': VehiculoForm(instance=aut)
    }
    if request.method=='POST':
        formulario= VehiculoForm(data=request.POST, instance=aut)
        aut.delete()
        datos['mensaje'] = "Eliminado Correctamente"

    return render(request, 'core/form_del_vehiculo.html', datos)



def form_mantencion(request):
    dato = {
        'form': mantencionForm()
    }

    if request.method=='POST':
        formulario= mantencionForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardado Correctamente"

    return render(request, 'core/form_mantencion.html', dato)

def form_mod_mantencion(request, id):
    auto = mantencion.objects.get(patente=id)
    datos = {
        'forn': mantencionForm(instance=auto)
    }
    if request.method=='POST':
        formulario= mantencionForm(data=request.POST, instance=auto)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Modificado Correctamente"

    return render(request, 'core/form_mod_mantencion.html', datos)




def listar_mod_mantencion(request):
    mantencion = mantencion.objects.all()
    datos = {
        "mantencion":mantencion
    }
    return render(request, 'core/listar_mod_mantencion.html',datos)



def form_del_mantencion(request, id):
    aut = mantencion.objects.get(id_mantencion=id)
    datos = {
        'forn': mantencionForm(instance=aut)
    }
    if request.method=='POST':
        formulario= mantencionForm(data=request.POST, instance=aut)
        aut.delete()
        datos['mensaje'] = "Eliminado Correctamente"

    return render(request, 'core/form_del_mantencion.html', datos)