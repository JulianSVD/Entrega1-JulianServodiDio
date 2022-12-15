from django import forms

class DireccionForm(forms.Form):
    calle= forms.CharField(label="Calle", max_length=20) 
    numero= forms.IntegerField(label="Numero")
    #Parecido a un models

class FamiliarForm(forms.Form):
    nombre=forms.CharField(label="Nombre", max_length=20)
    apellido=forms.CharField(label="Apellido", max_length=20)
    edad=forms.IntegerField(label="Numero")

class PuestoForm(forms.Form):
    profesion=forms.CharField(label="Profesion", max_length=20)
    antiguedad=forms.IntegerField(label="Antiguedad", max_value= 90)