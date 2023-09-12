from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('delete/', views.delete, name='delete'),
    path('edit/', views.edit, name='edit'),
    path('edit/update/', views.update, name='update')
]