from django.shortcuts import render, redirect
from .models import Note, Tag

# Para ativar a venv, rode no cmd: env\Scripts\activate.bat

def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        id = request.POST.get('id')
        tag_name = request.POST.get('tag')
        # Verifique se a tag já existe no banco de dados
        tag, created = Tag.objects.get_or_create(name=tag_name)
        note = Note.objects.create(title=title, content=content, id=id)
        note.tags.add(tag)  # Associe a anotação à tag
        note.save()
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        tags = Tag.objects.all()
        notes_data = [{'title': note.title, 'content': note.content, 'id': note.id} for note in all_notes]
        return render(request, 'notes/index.html', {'notes': notes_data, 'tags': tags})

def delete(request):
    if request.method == 'POST':
        note_id = request.POST.get('id')
        note = Note.objects.get(id=note_id)
        # Obtém a tag associada à nota
        tags = note.tags.all()

        note.delete()

        for tag in tags:
            # Verifica se a tag não está associada a mais nenhuma anotação
            if tag.notes.count() == 0:
                tag.delete()
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

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'notes/tags_list.html', {'tags': tags})

def tag_detail(request, tag_id):
    tag = Tag.objects.get(id=tag_id)
    return render(request, 'notes/tag_detail.html', {'tag': tag})

def not_found(request):
    return render(request, 'notes/404.html')