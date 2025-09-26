afirmacion = True
mensaje ='''
__________________________________
|  Opcion 1: Programa de suma    |
|  Opcion 2: Programa de notas   |
|  Opcion 3: Programa de retiro  |
|  Opcion 4: Gestor de tareas    | 
|  Opcion 5: salida              | 
|________________________________|
'''

while afirmacion:
    print(mensaje)
    opcion = int(input("Selecciona una opcion: "))
    print(f"Bienvenido al: Programa {opcion}")
    if opcion == 1:
        print("Has seleccionado el programa de suma.")

        print("Introduce el primer número:")
        num1 = float(input())
        print("Introduce el segundo número:")
        num2 = float(input())
        suma = num1 + num2
        print(f"La suma de {int(num1)} y {int(num2)} es: {int(suma)}")
        print("Gracias por usar el programa de suma.")
    elif opcion == 2:
        print("Has seleccionado el programa de notas.")
        print("atencion las notas deben ser del 1 al 10, si no es asi, el programa se detendra")

        matematicas = int(input("ingrese la nota de matematicas: "))
        español = int(input("ingrese la nota de español: "))
        ingles =   int(input("ingrese la nota de ingles: "))
        biologia = int(input("ingrese la nota de biologia: "))
        quimica = int(input("ingrese la nota de quimica: "))
        religion = int(input("ingrese la nota de religion: "))
        etica = int(input("ingrese la nota de etica: "))
        tegnologia = int(input("ingrese la nota de tegnologia: "))
        educacion_fisica = int(input("ingrese la nota de educacion fisica: "))
        geometria = int(input("ingrese la nota de geometria: "))
        sociales = int(input("ingrese la nota de sociales: "))

        suma = (matematicas + español + ingles + biologia + quimica + religion + etica + tegnologia + educacion_fisica + geometria + sociales)
        promedio = suma // 11

        print(f"Tu promedio de notas es: {promedio}")
        if promedio >= 7:
            print("felicidades, pasaste el año:)")
        elif promedio == 5:
            print("Pasaste raspando pero pasaste el año")
        elif promedio >= 4:
            print("lo siento, no pasaste de año:(")
        else:
            print("error, una o mas notas estan fuera del rango permitido (1-10), el programa se detendra")
                
    elif opcion == 3:
        saldo = 0
        while True:
            Programa_retiro = '''
            __________________________
            |---Programa de Retiro---|
            |________________________|
            |1. Depositar            |
            |2. Retirar              |
            |3. Consultar saldo      |
            |4. Salir                |
            |________________________|
            '''
            print(Programa_retiro)
            opcion_retiro = int(input("Selecciona una opción: "))
            if opcion_retiro == 1:
                monto = int(input("Ingresa el monto a depositar: "))
                saldo += monto
                print(f"Has depositado {int(monto)} . Tu nuevo saldo es: {int(saldo)}")
            elif opcion_retiro == 2:
                monto = int(input("Ingresa el monto a retirar: "))
                if monto > saldo:
                    print("No tienes suficiente saldo.")
                else:
                    saldo -= monto
                    print(f"Has retirado {monto}. Tu nuevo saldo es: {saldo}")
            elif opcion_retiro == 3:
                print(f"Tu saldo actual es: {saldo}")
            elif opcion_retiro == 4:
                break
            else:
                print("Opción no válida.")
    elif opcion == 4:
        print("Has seleccionado el gestor de tareas del hogar.")
        tareas = []    #lista para almacenar las tareas
        while True:
            menu = '''
            ________________________
            |---Gestor de Tareas---|
            |______________________|
            |1. Agregar tarea      |   
            |2. Lista de tareas    |   
            |3. Terminar una tarea |   
            |4. Salir              |
            |______________________|
            '''
            print(menu)
            opcion_tareas = input("Selecciona una opción: ")
            if opcion_tareas == "1":
                nombre = input("Ingresa el nombre de la tarea: ")
                hora = input("Ingresa la hora de inicio (Horario Militar): ")
                tareas.append({'nombre': nombre, 'hora': hora})
                print(f"Tarea agregada: {nombre} a las {hora}")
            elif opcion_tareas == "2":
                if not tareas:
                    print("No hay tareas registradas.")
                else:
                    print("\nLista de tareas:")
                    for idx, tarea in enumerate(tareas, start=1):
                        print(f"{idx}. {tarea['nombre']} (Inicio: {tarea['hora']})")
            elif opcion_tareas == "3":
                if not tareas:
                    print("No hay tareas para terminar.")
                else:
                    print("\nTareas actuales:")
                    for idx, tarea in enumerate(tareas, start=1):
                        print(f"{idx}. {tarea['nombre']} (Inicio: {tarea['hora']})")
                        num = int(input("Ingresa el número de la tarea a terminar: "))
                        if 1 <= num <= len(tareas):
                            tarea_terminada = tareas.pop(num-1)
                            print(f"Tarea '{tarea_terminada['nombre']}' terminada y eliminada de la lista.")
                        else:
                            print("Número inválido.")
            elif opcion_tareas == "4":
                print("Saliendo del gestor de tareas...")
                break
            else:
                print("Opción no válida.")
    elif opcion == 2:
        print("Saliendo del programa. ¡Gracias por usar el sistema, hasta luego!")
        afirmacion = False
    else:
        print("Opción no válida.")