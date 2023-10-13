from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/notes/', views.api_note),
    path('delete/', views.delete, name='delete'),
    path('edit/', views.edit, name='edit'),
    path('edit/update/', views.update, name='update'),
    path('tags/', views.tags_list, name='tags_list'),
    path('tags/<int:tag_id>/', views.tag_detail, name='tag_detail'),
    #re_path(r'^.*$', views.not_found, name='not_found'),
]