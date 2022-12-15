from django.shortcuts import render
from .models import Direcciones, Familiar, Puesto
from django.http import HttpResponse
from django.template import Template, Context, loader
import datetime
from AppFamilia.forms import DireccionForm, FamiliarForm, PuestoForm
# Create your views here.

#IGNORAR, SE USO EN LA ANTERIOR ENTREGA!!!
"""
def familiar(request):

    persona= Familiar(nombre="Julian", 
    apellido="Servo di Dio", edad="18",)
    persona.save()
    cadena_texto=f"el familiar {persona.nombre} {persona.apellido} ha sido guardado en la base de datos"
    return HttpResponse(cadena_texto)

def mostrarFamiliar(request):

    diccionario= {
        "nombre1":"Julian", "familia1":"Servo", "edad1": "18",
        "nombre2":"Melina", "familia2":"Servo", "edad2": "24",
        "nombre3":"Lulu",   "familia3":"Servo", "edad3": "20"
    }

    template = loader.get_template("template1.html")#De un controlador, te lleva a una template

    documento=template.render(diccionario)
    return HttpResponse(documento)
"""
def direcciones(request):
    return render (request,"AppFamilia/direcciones.html")

def inicio(request):
    return render (request, "AppFamilia/inicio.html")


#HACE QUE FUNCIONE EL FORMULARIO antes de emplear ( API form Django )
"""
def direccionFormulario(request):
    if request.method=="POST":
        calle= request.POST["calle"]
        numero= request.POST["numero"]
        direccion= Direcciones(calle=calle, numero=numero)
        direccion.save()
        return render(request, "AppFamilia/inicio.html", {"mensaje": "Curso guardado correctamente!"})
    else:
        return render(request, "AppFamilia/direccionFormulario.html")"""

#Formulario de ( API FORM django ), llamado de forms.py /// ESTA SUELE SER LA VISTA BASICA!
def direccionFormulario(request):
    form= DireccionForm(request.POST)
    if request.method=="POST":#Si viene por post, guardo la informacion
        form= DireccionForm(request.POST)

        if form.is_valid(): #Si es valida, Limpiala y guardala
            informacion = form.cleaned_data
            calle= informacion["calle"]
            numero= informacion["numero"]
            direccion= Direcciones(calle=calle, numero=numero)
            direccion.save()
            return render(request, "AppFamilia/inicio.html", {"mensaje": "Direccion guardada correctamente!"})
        else:#SI NO ES VALIDA, avisarlo
            return render(request, "AppFamilia/inicio.html", {"mensaje": "Informacion NO valida"})
    
    else:#Si viene por GET, creo formulario vacio, y se lo mando
        form: DireccionForm()
        return render(request, "AppFAmilia/direccionFormulario.html", {"form": form})    


def familiarFormulario(request):
    form= FamiliarForm(request.POST)
    if request.method=="POST":
        form= FamiliarForm(request.POST)

        if form.is_valid():
            informacion = form.cleaned_data
            nombre= informacion["nombre"]
            apellido= informacion["apellido"]
            edad= informacion["edad"]
            familiar = Familiar(nombre=nombre, apellido=apellido, edad=edad)
            familiar.save()
            return render(request, "AppFamilia/inicio.html", {"mensaje": "Familia guardada correctamente!"})
        else:
            return render(request, "AppFamilia/inicio.html", {"mensaje": "Informacion NO valida"})
    else:
        form: DireccionForm()
        return render(request, "AppFAmilia/familiarFormulario.html", {"form": form})


def puestoFormulario(request):
    form= PuestoForm(request.POST)
    if request.method=="POST":
        form= PuestoForm(request.POST)

        if form.is_valid():
            informacion = form.cleaned_data
            profesion= informacion["profesion"]
            antiguedad= informacion["antiguedad"]
            puesto = Puesto(profesion=profesion, antiguedad=antiguedad)
            puesto.save()
            return render(request, "AppFamilia/inicio.html", {"mensaje": "Puesto guardado correctamente!"})
        else:
            return render(request, "AppFamilia/inicio.html", {"mensaje": "Informacion NO valida"})
    else:
        form: DireccionForm()
        return render(request, "AppFamilia/puestoFormulario.html", {"form": form})