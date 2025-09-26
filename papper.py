#Hoja de vida para asignar trabajos las personas
from colorama import init, Fore, Back, Style
init()
 #opciones del mensaje registrar hoja de vida,registrsar vacante, consultar hojasde vida,consultar vacantes,asignar hojas de vida a vacantes y salir
 
mensaje = '''
________________________________
| BIENVENIDO A TU HOJA DE VIDA |
|______________________________|
|1.Regsitrar hoja de vida      |
|2.Registrar vacante           |
|3.Consultar hojas de vida     |
|4.Consultar vacantes          |
|5.Asignar hojas de vida       |  
|a vacantes                    |
|6.Salir                       |
|______________________________|
'''
arroz = True
lista_hojas_de_vida = []
while arroz:
    print(Fore.GREEN + mensaje + Style.RESET_ALL) 
    opcion = int(input(Fore.LIGHTGREEN_EX + "Ingrese una opcion: " + Style.RESET_ALL))
    if opcion == 1:
        print(Fore.YELLOW + "Ha seleccionado la opcion 1: Resgistrar hoja de vida" + Style.RESET_ALL)
        def crear_hoja_de_vida():
            print(Fore.CYAN + "Registro de hoja de vida:" + Style.RESET_ALL)
            nombre = input("Ingrese su nombre completo: ")
            edad = input("Ingrese su edad: ")
            cc = input("Ingrese su numero de cedula: ")
            telefono = input("Ingrese su numero de telefono: ")
            nivel_educativo = input("Ingrese su nivel educativo: ")
            pregunta = input("Ha tenido experiencia laboral? si/no: ")
            if pregunta.lower() == "si":
                experiencia_laboral = input("Describa su experiencia laboral: ")
                empresa = input("Ingrese el nombre de la empresa donde trabajo: ")
                tiempo = input("Ingrese el tiempo que trabajo en la empresa: ")
                experiencia_laboral += f", Empresa: {empresa}, Tiempo: {tiempo}"
            elif pregunta.lower() == "no":
                experiencia_laboral = "No tiene experiencia laboral"
            else:
                print(Fore.RED + "Respuesta no valida. Asumiendo que no tiene experiencia laboral." + Style.RESET_ALL)
                experiencia_laboral = "No tiene experiencia laboral"
            return {
                "nombre": nombre,
                "edad": edad,
                "CC": cc,
                "telefono": telefono,
                "nivel_educativo": nivel_educativo,
                "experiencia_laboral": experiencia_laboral
            }
        hoja = crear_hoja_de_vida()
        lista_hojas_de_vida.append(hoja)
        print(Fore.GREEN + "Hoja de vida registrada exitosamente." + Style.RESET_ALL)
        
    elif opcion == 2:
        print(Fore.YELLOW + "Ha seleccionado la opcion 2: Registrar vacante" + Style.RESET_ALL)
        def registrar_vacante():
            print(Fore.CYAN + "Registro de vacante:" + Style.RESET_ALL)
            titulo = input("Ingrese el titulo del puesto: ")
            descripcion = input("Ingrese una breve descripcion del puesto: ")
            requisitos = input("Ingrese los requisitos del puesto: ")
            salario = input("Ingrese el salario ofrecido: ")
            return {
                "titulo": titulo,
                "descripcion": descripcion,
                "requisitos": requisitos,
                "salario": salario
            }
        vacante = registrar_vacante()
        print(Fore.GREEN + "Vacante registrada exitosamente." + Style.RESET_ALL)
        
    elif opcion == 3:
        print(Fore.YELLOW + "Ha seleccionado l aopcion3: Consulta de hojas de vida:" + Style.RESET_ALL)
        if lista_hojas_de_vida:
            for idx, hoja in enumerate(lista_hojas_de_vida, 1):
                print(f"{idx}. Nombre: {hoja['nombre']}, Edad: {hoja['edad']}, CC: {hoja['CC']}, Teléfono: {hoja['telefono']}, Nivel educativo: {hoja['nivel_educativo']}, Experiencia laboral: {hoja['experiencia_laboral']}")
        else:
            print("No hay hojas de vida registradas.")
            
    elif opcion == 4:
        print(Fore.YELLOW + "Ha seleccionado la opcion 4: Consultar vacantes" + Style.RESET_ALL)
        if 'vacante' in locals():
            print(f"Titulo: {vacante['titulo']}, Descripcion: {vacante['descripcion']}, Requisitos: {vacante['requisitos']}, Salario: {vacante['salario']}")
        else:
            print("No hay vacantes registradas.")
            
    elif opcion == 5:
        print(Fore.YELLOW + "Ha seleccionado la opcion 5: Asignar hojas de vida a vacantes" + Style.RESET_ALL)
        if not lista_hojas_de_vida:
            print(Fore.RED + "No hay hojas de vida disponibles para asignar." + Style.RESET_ALL)
        elif 'vacante' not in locals():
            print(Fore.RED + "No hay vacantes disponibles para asignar." + Style.RESET_ALL)
        else:
            print("Hojas de vida disponibles:")
            for idx, hoja in enumerate(lista_hojas_de_vida, 1):
                print(f"{idx}. Nombre: {hoja['nombre']}, CC: {hoja['CC']}")
            seleccion = int(input("Seleccione el numero de la hoja de vida que desea asignar a la vacante: "))
            if 1 <= seleccion <= len(lista_hojas_de_vida):
                hoja_seleccionada = lista_hojas_de_vida[seleccion - 1]
                print(Fore.GREEN + f"Hoja de vida de {hoja_seleccionada['nombre']} asignada a la vacante de {vacante['titulo']} exitosamente." + Style.RESET_ALL)
            else:
                print(Fore.RED + "Seleccion no valida." + Style.RESET_ALL)
            
    elif opcion == 6:
        print(Fore.RED + "Saliendo del sistema..." + Style.RESET_ALL)
        arroz = False
    else:
        print(Fore.RED + "Opcion no valida, por favor intente de nuevo." + Style.RESET_ALL)
