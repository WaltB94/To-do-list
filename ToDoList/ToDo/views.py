from django.shortcuts import render, redirect
from .forms import AgregarTarea, CompletarTarea

# Create your views here.

tareas = []
tareas_completadas = []


def home(request):
    form_completar = CompletarTarea(tareas=tareas)
    form_agregar = AgregarTarea(request.POST or None)  # Obtener el formulario enviado en la solicitud POST
    if request.method == 'POST' and form_agregar.is_valid():  # Verificar si se envió el formulario y es válido
        tarea = form_agregar.cleaned_data["tarea"]
        tareas.append(tarea)
        return redirect('home')  # Redirigir a la misma vista para actualizar la lista de tareas

    context = {
        'tareas': tareas,
        'tareas_completadas': tareas_completadas,
        'form_completar': form_completar,
        'form_agregar': form_agregar,
    }
    return render(request, "todo/home.html", context)
    


def delete(request, index):
    if index < len(tareas):
        tareas.pop(index)
    return redirect('home')


def confirmar_completadas(request):
    return redirect('home')




def completar_tarea(request, index):
    if index < len(tareas):
        tarea_completada = tareas.pop(index)
        tareas_completadas.append(tarea_completada)
    return redirect('home')
