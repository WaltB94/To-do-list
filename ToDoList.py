lista = []
listaCompletadas = []

def agregarTareas():
    tareaAgregada = input("Ingrese su nueva tarea: ")
    lista.append(tareaAgregada)
    print("La tarea se ha agregado correctamente.")

def tareaAEliminar():
    tareaAEliminar = input("Ingrese la tarea a eliminar: ")
    if tareaAEliminar in lista:
        lista.remove(tareaAEliminar)
        print("La tarea se ha eliminado correctamente.")
    else:
        print("La tarea ingresada no se encuentra en la lista.")

def tareaCompletada():
    tareaCompletada = input("Ingrese su tarea completada: ")
    if tareaCompletada in lista:
        listaCompletadas.append(tareaCompletada)
        lista.remove(tareaCompletada)
        print("La tarea se ha marcado como completada.")
    else:
        print("La tarea ingresada no se encuentra en la lista.")
 
def tareasPendientes():
    return lista

def tareasCompletadas():
    print("Tareas completadas:")
    for tarea in listaCompletadas:
        print("- " + tarea)

# Agrego un menú para decidir qué hacer y no tener que andar ejecutando siempre funciones distintas.
while True:
    print("\n----- MENU -----")
    print("1. Agregar tarea")
    print("2. Marcar tarea como completada")
    print("3. Eliminar tarea")
    print("4. Mostrar tareas pendientes")
    print("5. Mostrar tareas completadas")
    print("6. Salir")

    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == "1":
        agregarTareas()
    elif opcion == "2":
        tareaCompletada()
    elif opcion == "3":
        tareaAEliminar()
    elif opcion == "4":
        print("Tareas pendientes:")
        for tarea in tareasPendientes():
            print("- " + tarea)
    elif opcion == "5":
        tareasCompletadas()
    elif opcion == "6":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, ingrese una opción válida del menú.")

