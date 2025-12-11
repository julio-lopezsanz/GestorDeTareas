"""Gestor de tareas con listas"""

tasks = []
while True:
    try:
        #Menu
        print()
        print("1- Agregar tarea")
        print("2- Marcar tarea como completada")
        print("3- Eliminar tarea")
        print("4- Ver todas las tareas")
        print("5- Salir")
        option = int(input("Seleccione una opcion: "))

        #Opcion 1 Agregar elemento a la lista
        if option == 1:
            task = input("\nEscribe la tarea que deseas agregar: ").lower()
            tasks.append(task)

        #Opcion 2 Modificar elemento de la lista
        elif option == 2:
            if not tasks:
                print("\nNo hay tareas que completar.")
                continue
            while True:
                task = input("\nEscriba la tarea que ha completado: ").lower()
                FOUND = False
                for index,value in enumerate(tasks):
                    if value == task:
                        tasks[index] = f"{value} ✔"
                        FOUND = True
                if FOUND:
                    print("Los Cambios han sido realizados")
                    break
                else:
                    print(f"{task} no se ha encontrado en la lista")

        #Opcion 3 Eliminar elemento de la lista
        elif option == 3:
            if not tasks:
                print("\nNo hay tareas para eliminar.")
                continue
            while True:
                task = input("\nEscriba la tarea que va a eliminar: ").lower()
                if task in tasks:
                    tasks.remove(task)
                    print("La tarea ha sido eliminada")
                    break
                print("La tarea no ha sido encontrada")

        #Opcion 4 Imprimir toda la lista
        elif option == 4:
            if not tasks:
                print("\nNo hay tareas que mostrar.")
                continue
            print("\n")
            for index,value in enumerate(tasks, start=1):
                print(f"Tarea {index} - {value} ")

        #Opcion 5 Salir del programa
        elif option == 5:
            print("\nSaliendo del programa...")
            break
        else:
            print("Opcion invalida. Solo se permite numeros del 1 al 5")
    except ValueError:
        print("Error: Solo se permiten valores numericos enteros")
