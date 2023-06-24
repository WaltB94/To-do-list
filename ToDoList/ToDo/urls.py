from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path ("add/", views.add, name='add'),
    path('delete/<int:index>/', views.delete, name='delete'),  # Ruta para eliminar tarea
    path('completar/<int:index>/', views.completar_tarea, name='completar_tarea'),
     path('confirmar-completadas/', views.confirmar_completadas, name='confirmar_completadas'),
]
