
# def trabajadores_de_empresa():
proyecto1 = [
        #ejemplo:
            #{
            #  "nombre": "juan perez",
            #   "desempeño": (8,9 ,6 ,7.8, 4.9)
            #},
            #{
            #   "nombre": "Mariana gomez",
            #  "desempeño": (8,5,9.2,7.8,)
            #},
            #{
            #   "nombre": "leandro ruperes",
            #  "desempeño": (9 ,6 ,7.8, 4.9)
            #},
            #{
            #   "nombre": " samanta sanchez",
            #  "desempeño": (8,9 ,6 ,7.8, 4.9)
            #},
            #{
            #   "nombre": "gaberiel mendez",
            #   "desempeño": (8,9 ,6 ,7.8, 4.9)
            #}
]
#registrar datos
def registar_nombre():
        print("ha selecionado la opcion 1: Registrar rendimiento de un empleado")
        print("\n=== REGISTRAR EMPLEADO ===")
        nombre = input("Ingrese el nombre completo del empleado: ").strip().title()
        
        if not nombre:
            print("Error: El nombre no puede estar vacío")
            return
        
        for empleado in proyecto1:
            if empleado["nombre"].lower() == nombre.lower():
                print(f"El empleado '{nombre}' ya está registrado")
                return
            
        print("Ingrese las calificaciones de desempeño (0-10)")
        calificaciones = []
        
        while True:
            try:
                entrada = input("Calificación (o presiona Enter para terminar): ").strip()
                if entrada == "":
                    if len(calificaciones) == 0:
                        print("Debe ingresar al menos una calificación")
                        continue
                    break
                
                calificacion = float(entrada)
                if 0 <= calificacion <= 10:
                    calificaciones.append(calificacion)
                    print(f"Calificación {calificacion} agregada")
                else:
                    print("La calificación debe estar entre 0 y 10")
            
            except ValueError:
                print("Por favor ingrese un número válido")
    
    # Crear el registro del empleado
        empleado = {
            "nombre": nombre,
            "desempeño": tuple(calificaciones)
        }
        
        proyecto1.append(empleado)
        print(f"✓ Empleado '{nombre}' registrado exitosamente con {len(calificaciones)} calificaciones")

                    
#calcular promedios
def pormedio_semanal(calificaciones):
    if not calificaciones:
        return 0
    return sum(calificaciones) /len(calificaciones)
    

#clasificar rendimiento
def mostrar_promedios():
    """Muestra los promedios de todos los empleados"""
    print("\n=== PROMEDIOS DE EMPLEADOS ===")
    
    if not proyecto1:
        print("No hay empleados registrados por lo tanto no se puede sacar un promedio")
        return
    
    for i, empleado in enumerate(proyecto1, 1):
        promedio = pormedio_semanal(empleado["desempeño"])
        print(f"{i}. {empleado['nombre']}: {promedio:.2f}")
        print(f"   Calificaciones: {empleado['desempeño']}")
        
def calificaion_promedio(promedio):
    if promedio == 10:
        return "Excelente"
    elif promedio >= 8.5:
        return "Sobresaliente"
    elif promedio >=7.5:
        return "Aceptable"
    elif promedio >=5:
        return "Bajo, necesita mejorar"
    else:
        return "Necesita Mejorar"
    
def evaluar_empleado():
    """Permite evaluar o actualizar las calificaciones de un empleado"""
    print("\n=== EVALUAR EMPLEADO ===")
    
    if not proyecto1:
        print("No hay empleados registrados")
        return
    
    # Mostrar lista de empleados
    print("Empleados disponibles:")
    for i, empleado in enumerate(proyecto1, 1):
        print(f"{i}. {empleado['nombre']}")
    
    try:
        seleccion = int(input("Seleccione el número del empleado: ")) - 1
        
        if 0 <= seleccion < len(proyecto1):
            empleado = proyecto1[seleccion]
            print(f"\nEmpleado seleccionado: {empleado['nombre']}")
            print(f"Calificaciones actuales: {empleado['desempeño']}")
            
            opcion = input("¿Desea (1) agregar nueva calificación o (2) reemplazar todas? [1/2]: ")
            
            if opcion == "1":
                # Agregar nueva calificación
                nueva_cal = float(input("Nueva calificación (0-10): "))
                if 0 <= nueva_cal <= 10:
                    calificaciones_actuales = list(empleado["desempeño"])
                    calificaciones_actuales.append(nueva_cal)
                    empleado["desempeño"] = tuple(calificaciones_actuales)
                    print("✓ Nueva calificación agregada")
                else:
                    print("Error: La calificación debe estar entre 0 y 10")
            
            elif opcion == "2":
                # Reemplazar todas las calificaciones
                print("Ingrese las nuevas calificaciones:")
                nuevas_calificaciones = []
                
                while True:
                    entrada = input("Calificación (o Enter para terminar): ").strip()
                    if entrada == "":
                        if len(nuevas_calificaciones) == 0:
                            print("Debe ingresar al menos una calificación")
                            continue
                        break
                    
                    calificacion = float(entrada)
                    if 0 <= calificacion <= 10:
                        nuevas_calificaciones.append(calificacion)
                    else:
                        print("La calificación debe estar entre 0 y 10")
                
                empleado["desempeño"] = tuple(nuevas_calificaciones)
                print("✓ Calificaciones actualizadas")
            
        else:
            print("Selección no válida")
    
    except (ValueError, IndexError):
        print("Error: Selección no válida")
    
    
#mostrar reporte   
def mostrar_reporte():
    """Muestra un reporte completo de todos los empleados"""
    print("\n" + "="*50)
    print("           REPORTE SEMANAL DE DESEMPEÑO")
    print("="*50)
    
    if not proyecto1:
        print("No hay empleados registrados")
        return
    
    total_empleados = len(proyecto1)
    promedio_general = 0
    
    for i, empleado in enumerate(proyecto1, 1):
        promedio = pormedio_semanal(empleado["desempeño"])
        clasificacion = calificaion_promedio(promedio)
        promedio_general += promedio
        
        print(f"\n{i}. EMPLEADO: {empleado['nombre']}")
        print(f"   Calificaciones: {empleado['desempeño']}")
        print(f"   Promedio: {promedio:.2f}")
        print(f"   Clasificación: {clasificacion}")
        print(f"   Total evaluaciones: {len(empleado['desempeño'])}")
    
    promedio_general = promedio_general / total_empleados if total_empleados > 0 else 0
    
    print("\n" + "-"*50)
    print(f"RESUMEN GENERAL:")
    print(f"Total de empleados: {total_empleados}")
    print(f"Promedio general: {promedio_general:.2f}")
    print(f"Clasificación general: {calificaion_promedio(promedio_general)}")
    print("="*50)

menu = """
╔═══════════════════════════════════╗
║        GESTIÓN DE DESEMPEÑO       ║
╠═══════════════════════════════════╣
║ 1. Registrar empleado             ║
║ 2. Mostrar promedios              ║
║ 3. Evaluar empleado               ║
║ 4. Mostrar reporte completo       ║
║ 0. Salir del programa             ║
╚═══════════════════════════════════╝
"""

while True:
    try:
        print(menu)
        opcion = int(input("Seleccione una de las opciones para avanzar con el programa: "))
        if opcion == 1:
            registrar = registar_nombre()
            if registrar:  # Solo agrega si no es None
                proyecto1.append(registrar)
            
        elif opcion ==2:
            mostrar_promedios()
            
        elif opcion == 3:
            evaluar_empleado()
            
        elif opcion == 4:
            mostrar_reporte()
            
        elif opcion == 0:
            break
        
        else:
            print("opcion no valida")
        
    except ValueError:
        print("Opcion no valida, seleccione una de las opcines del menu")
        
    except Exception as e:
        print(f"Se produjo un error inesperado: {e}")
