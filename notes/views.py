from django.shortcuts import render, redirect
from .models import Note

def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        id = request.POST.get('id')
        note = Note.objects.create(title=title, content=content, id=id)
        note.save()
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        notes_data = [{'title': note.title, 'content': note.content, 'id': note.id} for note in all_notes]
        #print(notes_data)
        return render(request, 'notes/index.html', {'notes': notes_data})

def delete(request):
    if request.method == 'POST':
        note_id = request.POST.get('id')
        note = Note.objects.get(id=note_id)
        note.delete()
        return redirect('index')
    else:
        return redirect('index')

def edit(request):
    if request.method == 'POST':
        note_id = request.POST.get('id')
        note = Note.objects.get(id=note_id)
        return render(request, 'notes/edit.html', {'note': note})

def update(request):
    if request.method == 'POST':
        note_id = request.POST.get('id')
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        note = Note.objects.get(id=note_id)
        note.title = title
        note.content = content
        note.save()
        return redirect('index')
    else:
        return redirect('index')

def not_found(request):
    return render(request, 'notes/404.html')