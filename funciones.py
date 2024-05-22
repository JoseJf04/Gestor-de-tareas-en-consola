#Lista tareas
tareas = []

#Funciones del programa
def añadir_tareas(tareas):
    #Recibir tarea
    tarea = input("Ingresar tarea: ")

    #Añadir tarea a la lista
    tareas.append(tarea)

    #Informe de tarea añadida
    print("Tarea añadida a la lista de tareas")

    # Imprime la tarea añadida
    print(f"Tarea añadida: {tarea}")

    #Informe del numero de tareas
    print(f"numero de tareas {len(tareas)}")
def ver_tareas(list):
    # Condicional que evalue si hay elementos en la lista

    #Si hay elementos
    if list:
        for i in range(len(list)):
            print(f"{i+1}.{list[i]}")
    #Si no hay elementos
    else:
        print("No hay tareas por realizar")

    #Fin del listado de
    print("Fin del listado de tareas")

def marcar_completada(list):
    #Ver lista de tareas
    ver_tareas(list)

    #Solicitar y capturar numero de la tarea a completar
    completada = int(input("Ingresa el numero de la tarea que desea marcar como completada: "))

    #Verificar si el numero de tarea esta en lista
    if completada > 0 and completada <= len(list):

        #Verificar si la tarea esta marcada como completada

        #Si esta completada
        if "(Completada)" in list[completada -1]:
            print("La tarea ya se encontraba completada")

        #Si no esta completada
        else:
            list[completada-1] += " (Completada)"
            print(f"Se ha marcado la tarea N{completada} como completada")

    else:
        print("No se encuentra en la lista de tareas")

def eliminar_tarea(list):
    #Si la lista contiene elementos
    if list:
        #Llamar a la funcion ver_tareas para mostrar la lista de tareas
        ver_tareas(list)

        #Capturar opcion del usuario
        tarea = int(input("Ingresa el numero de la tarea que desea eliminar: "))

        #Verificar que el numero de tarea sea valido
        #Si es valido
        if tarea > 0 and tarea <= len(list):
            list.pop(tarea-1)
            print("Tarea eliminada")

        #Si no es valido
        else:
            print("numero de tarea introducido no se encuentra en la lista")

    #Si la lista no contiene elementos
    else:
        print("Lista de tareas vacia")