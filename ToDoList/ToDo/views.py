from django.shortcuts import render, redirect
from .forms import AgregarTarea, CompletarTarea

# Create your views here.

tareas = []
tareas_completadas = []


def home(request):
    form_completar = CompletarTarea(tareas=tareas)
    context = {'tareas': tareas, 'tareas_completadas': tareas_completadas, 'form_completar': form_completar}
    return render(request, "todo/home.html", context)





def add(request):
    if request.method == 'POST':
        form = AgregarTarea(request.POST)
        if form.is_valid():
            tarea = form.cleaned_data["tarea"]
            tareas.append(tarea)
            return redirect ('home')
    else:
        form = AgregarTarea()
        context = {'form' : form}
        return render(request, "todo/add.html", context)
    


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
