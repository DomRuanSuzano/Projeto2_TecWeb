from ast import Not
from turtle import title
from django.shortcuts import render, redirect
from .models import Note


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        nota = Note(title=title, content=content)
        nota.save()
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})

def delete(request):
    id = request.POST.get('id')
    nota = Note.objects.get(id=id)
    nota.delete()
    return redirect('index')

def index_update(request):
    id = request.POST.get('id')
    note = Note.objects.get(id=id)
    return render(request, 'notes/update.html', {'note': note})

def update(request):
    title = request.POST.get('titulo')
    content = request.POST.get('detalhes')
    id = request.POST.get('id')
    nota = Note.objects.get(id=id)
    nota.title = title
    nota.content = content
    nota.save()
    return redirect('index')