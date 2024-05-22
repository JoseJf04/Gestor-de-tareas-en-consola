import funciones

#Menu de opciones

while True:
    # Menu para mostrar opciones
    print("\n********----Gestor de tareas----********\n")
    print("1.Añadir tarea")
    print("2.Ver tareas")
    print("3.Marcar tarea como completada")
    print("4.Eliminar tarea")
    print("5.Salir")

    #Entrada de opcion para el usuario
    opcion = int(input("\nIngresar opcion: "))

    #Menu de opciones
    if opcion == 1:
        funciones.añadir_tareas(funciones.tareas)
    elif opcion == 2:
        funciones.ver_tareas(funciones.tareas)
    elif opcion == 3:
        funciones.marcar_completada(funciones.tareas)
    elif opcion == 4:
        funciones.eliminar_tarea(funciones.tareas)
    elif opcion == 5:
        break
    else:
        print("opcion no valida")