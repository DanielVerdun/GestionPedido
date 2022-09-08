from django import forms 

class FormularioContacto(forms.Form):
    
    nombre = forms.CharField(label="Nombre", max_length= 15)
    
    apellido = forms.CharField(label="Apellido", max_length= 15)
    
    email = forms.EmailField(label="Email")
    
    contenido = forms.CharField(label="contenido", widget=forms.Textarea)
