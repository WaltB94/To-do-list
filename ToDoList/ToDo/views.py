from django.shortcuts import render

# Create your views here.

tareas = ['hola', 'dos', 'tres', 'cuatro']

def home(request):
    context = {'tareas': tareas}
    return render(request, "todo/home.html", context)


def add(request):
    return render(request, "todo/add.html")