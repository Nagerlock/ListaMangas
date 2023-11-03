from django.shortcuts import render, redirect
from .models import manga, Usuario
from django.views.decorators.csrf import csrf_exempt


def list_manga(request):
    lists = manga.objects.all()
    return render(request, 'lista.html', {"lists": lists})


def create_manga(request):
    Manga = manga(titulo=request.POST['titulo'], descripcion=request.POST['descripcion'])
    Manga.save()
    return redirect('/lista/')


def delete_manga(request, manga_id):
    Manga = manga.objects.get(id=manga_id)
    Manga.delete()
    return redirect('/lista/')

def vista_u(request):
    usuarios = Usuario.objects.all()
    return render(request, 'personas.html', context= {"usuarios": usuarios})


def views_usuario(request):

    return render(request, 'personaReg.html')

def create_usuario(request):

    usuario = Usuario(nombre=request.POST['nombre'], correo=request.POST['correo'])
    usuario.save()
    return redirect('/lista/')
