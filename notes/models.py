from django.db import models

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    tags = models.ManyToManyField(Tag, related_name='notes')
    
    def __str__(self):
        return f'{self.id}.{self.title}'