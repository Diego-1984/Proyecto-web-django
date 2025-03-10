from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, "ProyectoWebapp/home.html")



def tienda(request):
    return render(request, "ProyectoWebapp/tienda.html")



def contacto(request):
    return render(request, "ProyectoWebapp/contacto.html")
