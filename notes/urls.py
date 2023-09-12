from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/', views.delete, name='delete'),
    path('edit/', views.edit, name='edit'),
    path('edit/update/', views.update, name='update'),
    re_path(r'^.*$', views.not_found, name='not_found'),
]