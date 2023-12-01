from django.shortcuts import render, HttpResponse


# Create your views here.

def complejos(request):
    return render(request, "core/complejos.html")

def contacto(request):
    return render(request, "core/contacto.html")
    
def pelicula(request):
    return render(request, "core/pelicula.html")
