lista = []
listaCompletadas = []


def agregarTareas():
    tareaAgregada = input("Ingrese su nueva tarea: ")
    lista.append(tareaAgregada)

def tareaAEliminar():
    tareaAEliminar = input ("Ingrese su tarea a eliminar: ")
    lista.remove(tareaAEliminar)

def tareaCompletada():
    tareaCompletada = input("Ingrese su tarea completada: ")
    if tareaCompletada in lista:
        listaCompletadas.append(tareaCompletada)
        lista.remove(tareaCompletada)
    else:
        print("La tarea ingresada no se encuentra en la lista.")

    
def tareasPendientes():
    return lista

agregarTareas()
tareaCompletada()
tareaAEliminar()
print (lista)