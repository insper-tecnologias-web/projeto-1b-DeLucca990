from django.shortcuts import render, redirect
from .models import Note

def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        note = Note.objects.create(title=title, content=content)
        note.save()
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        notes_data = [{'title': note.title, 'content': note.content} for note in all_notes]
        #print(notes_data)
        return render(request, 'notes/index.html', {'notes': notes_data})