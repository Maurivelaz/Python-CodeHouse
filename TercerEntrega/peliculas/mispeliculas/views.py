from django.shortcuts import render
from mispeliculas.models import Pelicula
from mispeliculas.forms import FormularioCurso

# Create your views here.

def registroPeli(request):
    if request.method == 'POST':
        
        form1 = FormularioCurso(request.POST)
        print(request.POST['titulo'])
        
        if form1.is_valid():
            informacion = form1.cleaned_data
            Peli = Pelicula(titulo = informacion['titulo'], genero = informacion['genero'], director = informacion['director']) 
            Peli.save()
            return render(request,'formulario.html',{"miform1":form1})
    else:
        form1 = FormularioCurso()
        
    return render(request,'formulario.html', {"miform1":form1})

def buscarPeli1(request):
    return render(request,'buscarPeli.html')

def buscarPeli(request):
    if request.GET['titulo']:
        titulos = request.GET['titulo']
        print(request.GET['titulo'])
        peli= Pelicula.objects.filter(titulo__icontains=titulos)
        return render(request,'resultadoBusqueda.html',{'resultado':peli})
