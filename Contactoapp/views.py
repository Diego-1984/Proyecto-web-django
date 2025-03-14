from django.shortcuts import render, redirect
from .forms import FormularioContacto

# Create your views here.
def contacto(request):
    formulario_contacto = FormularioContacto()
    if request.method == "POST":
        formulario_contacto = FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            nombre = request.POST.get("nombre")
            email = request.POST.get("email")
            mensaje = request.POST.get("mensaje")
            return redirect("/contacto/?valido=True")    
    
    return render(request, "contacto/contacto.html",{"miFormulario":formulario_contacto})