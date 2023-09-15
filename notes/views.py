from django.shortcuts import render, redirect
from .models import Note, Tag

# Para ativar a venv, rode no cmd: env\Scripts\activate.bat

def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        id = request.POST.get('id')
        tag_names = request.POST.get('tag').split(',')
        # Verifique se a tag já existe no banco de dados
        note = Note.objects.create(title=title, content=content, id=id)
        # Associar as tags ao cartão
        for tag_name in tag_names:
            tag, created = Tag.objects.get_or_create(name=tag_name.strip())
            note.tags.add(tag)
        note.save()
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        tags = Tag.objects.all()
        notes_data = [{'title': note.title, 'content': note.content, 'id': note.id, 'tags': note.tags.all()} for note in all_notes]
        return render(request, 'notes/index.html', {'notes': notes_data, 'tags': tags})

def edit(request):
    if request.method == 'POST':
        note_id = request.POST.get('id')
        note = Note.objects.get(id=note_id)
        return render(request, 'notes/edit.html', {'note': note})
    else:
        note = Note.objects.get(id=note_id)
        return render(request, 'notes/edit.html', {'note': note})

def update(request):
    if request.method == 'POST':
        note_id = request.POST.get('id')
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        new_tag_name = request.POST.get('tag') 
        note = Note.objects.get(id=note_id)
        note.title = title
        note.content = content
        # Obtém a tag associada à nota
        tag = note.tags.first()

        # Verifica se o nome da tag foi atualizado
        if tag.name != new_tag_name:
            # Tenta encontrar uma tag com o novo nome
            new_tag, created = Tag.objects.get_or_create(name=new_tag_name)
            # Remove a nota da tag antiga
            tag.notes.remove(note)
            # Adiciona a nota à nova tag
            new_tag.notes.add(note)
            new_tag.save()

            # Verifica se a tag antiga não está associada a mais nenhuma nota
            if tag.notes.count() == 0:
                tag.delete()
        note.save()
        return redirect('index')
    else:
        return redirect('index')

def delete(request):
    if request.method == 'POST':
        note_id = request.POST.get('id')
        note = Note.objects.get(id=note_id)
        # Obtém a tag associada à nota
        tags = note.tags.all()

        for tag in tags:
            # Verifica se a tag não está associada a mais nenhuma anotação
            if tag.notes.exclude(id=note_id).count() == 0:
                tag.delete()

        note.delete()
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