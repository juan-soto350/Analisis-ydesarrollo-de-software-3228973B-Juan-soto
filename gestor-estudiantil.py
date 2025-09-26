#menu interactivo sobre gestor de archivos de estudiantes del colegio EduTech 

from colorama import init, Fore, Back, Style
init()

menu = '''
________________________________
| Base de datos de estudiantes |
|______________________________|
|1.Registrar datos             |
|2.Ver estudiantes registrados |
|3.Buscar estudiante           |
|4.Promedio del curso          |       
|5.Salir                       |
|______________________________|

'''
registro = ()
base = []
arroz = True
while arroz:
    print(Fore.CYAN+menu)
    opcion = int(input(Fore.CYAN + "Ingrese una opcion: " + Style.RESET_ALL))
    #El programa debe solicitar al usuario el nombre del estudiante, la asignatura en la que está inscrito y su calificación.
    if opcion == 1:
            def registro_estudiantil():
                print(Fore.GREEN+"Registre sus datos para prosegir con el programa:")
                nombre = str(input("Ingrese su nombre:"))
                asignatura = str(input("Ingre el nombre de la asignatura:"))
                calificacion = int(input("Ingrese su calificaion de 1 a 5:"))
                return{
                    "Nombre": nombre,
                    "Asignatura" : asignatura,
                    "Calificaion" : calificacion
                }
            registro = registro_estudiantil()
            base.append(registro)
            print(Fore.GREEN+"Su registro ha sido exitoso." + Style.RESET_ALL)

    elif opcion == 2:
            print(Fore.GREEN + "Has seleccinado la opcion 2: Ver estudiantes registrados")
            if base:
                for idx, hoja in enumerate(base, 1):
                    print(f"{idx}. Nombre:{hoja['Nombre']}, Asignatura: {hoja['Asignatura']}, Calificacion: {hoja['Calificaion']}")
            else:
                print("No hay estudiantes registrados.")

    elif opcion == 3:
            print(Fore.GREEN + "Has seleccinado la opcion 3: Buscar estudiante")
            buscar_nombre = str(input("Ingrese el nombre del estudiante que desea buscar: "))
            encontrados = [hoja for hoja in base if hoja['Nombre'].lower() == buscar_nombre.lower()]
            if encontrados:
                for hoja in encontrados:
                    print(f"Nombre: {hoja['Nombre']}, Asignatura: {hoja['Asignatura']}, Calificacion: {hoja['Calificaion']}")
            else:
                print("Estudiante no encontrado.")

    elif opcion == 4:
            print(Fore.GREEN + "Has seleccinado la opcion 4: Promedio del curso")
            if base:
                total_calificaciones = sum(hoja['Calificaion'] for hoja in base)
                promedio = total_calificaciones / len(base)
                print(f"El promedio del curso es: {promedio:.2f}")
            else:
                print("No hay estudiantes registrados para calcular el promedio.")

    elif opcion == 5:
        print(Fore.RED + "Saliendo del sistema..." + Style.RESET_ALL)

        arroz = False

    else:
        print(Fore.RED + "Opcion no valida, por favor intente de nuevo." + Style.RESET_ALL)


