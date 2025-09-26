#menu administrativo de inventario para empresa
import colorama 
from colorama import init,Fore, Style

init()

verdadero = True
Menu = '''
______________________________________________
|  ==== MENÚ DE INVENTARIO EMPRESARIAL ====  |
|____________________________________________|
|   1. Resgistrar producto                   |
|   2. Mostrar inventario actual e incial    |
|   3. Valor total del inventario            |
|   4. Buscar producto                       |
|   5. Registrar venta                       |
|   6. Ver productos añadidos                |
|   7. Salir del Programa                    |
|____________________________________________|

'''
while verdadero:
    print(Fore.CYAN+Menu+Style.RESET_ALL)
    opcion = int(input("Selecciona una opcion: "))
    inventario = []
    valor_inventario = 2559.49  
    if opcion == 1:
        valor_inventario = 2559.49  
        print("Has seleccionado la opción 1: Registrar producto")
        print("Ingrese los detalles del producto que quiere registrar:")
        producto = input("Nombre del producto: ")
        cantidad = int(input("Cantidad: "))
        precio = float(input("Precio: "))
        inventario.append({"producto": producto, "cantidad": cantidad, "precio": precio})
        print(f"Producto {producto} registrado exitosamente.")

    
    elif opcion == 2:
        print("Has seleccionado la opcion 2: Mostrar inventario")
        
        inventario_actual = '''
_______________________________________________________
|              ====INVENTARIO ACTUAL====              |
|_____________________________________________________|
|   Producto            |Cantidad | Precio            |
|_____________________________________________________|
| 1. Xbox series X      | 10      | 599.99 dólares    |
| 2. PlayStation 5      | 5       | 749.99 dólares    |
| 3. Nintendo Switch 2  | 8       | 299.99 dólares    |
| 4. Portátil Levono    | 12      | 419.99 dólares    |
| 5. Portatil HP        | 10      | 449.99 dólares    |
| 6. Mouse Logitech     | 30      |  39.99 dólares    |
|_____________________________________________________|
    '''
        print(inventario_actual)
 #dinero actual 2.559,49 doleres
    elif opcion == 3:
            mensaje = "🚧 >>>ATENCION<<< como el programa está en fase de desarrollo puede ser qeu tenga algun problema. 🚧"
            mensaje2 = "🚧 El valor inicial del inventario es de $2559.49 dólares pero a primer vistaso aparece que el valor total del inventario es de $0.00 dólares 🚧"
            print(Fore.CYAN+"Has seleccionado la opción 3: Calcular valor total del inventario")
            print(Fore.RED + mensaje + Style.RESET_ALL)
            print(Fore.RED + mensaje2 + Style.RESET_ALL)
            print(Fore.YELLOW + "Calculando el valor total del inventario..." + Style.RESET_ALL)
            valor_total = sum(+item["cantidad"] * item["precio"] for item in inventario)
            print(Fore.GREEN+f"El valor total del inventario es: ${valor_total:.2f} dólares"+ Style.RESET_ALL)

    elif opcion == 4:
        print("Has seleccionado la opción 4: Buscar producto")
        print(Fore.RED+">>>ADVERTENCIA<<< COLOCAR EL NOMBRE DEL PRODUCTO IGUAL COMO APARECE EN EL INVENTARIO (Opcion2)"+ Style.RESET_ALL)

        Diccionario_Productos = {
            "Xbox series X": {"Cantidad": 10, "Precio": 599.99},
            "PlayStation 5": {"Cantidad": 5, "Precio": 749.99},
            "Nintendo Switch 2": {"Cantidad": 8, "Precio": 299.99},
            "Portátil Levono": {"Cantidad": 12, "Precio": 419.99},
            "Portátil HP": {"Cantidad": 10, "Precio": 449.99},
            "Mouse Logitech": {"Cantidad": 30, "Precio": 39.99}
        }
        nombre_producto = input("Ingrese el nombre del producto a buscar: ")

        if nombre_producto in Diccionario_Productos:
            print(f"Producto encontrado: {nombre_producto}")
            print(f"Cantidad: {Diccionario_Productos[nombre_producto]['Cantidad']}")
            print(f"Precio: {Diccionario_Productos[nombre_producto]['Precio']}")
        else:
            print("Producto no encontrado.")

    elif opcion == 5:
        print("Has seleccionado la opción 5: Registrar venta")
        registro_venta = input("Ingrese el nombre del producto vendido: ")

        Diccionario_Productos = {
            "Xbox series X": {"Cantidad": 10, "Precio": 599.99},
            "PlayStation 5": {"Cantidad": 5, "Precio": 749.99},
            "Nintendo Switch 2": {"Cantidad": 8, "Precio": 299.99},
            "Portátil Levono": {"Cantidad": 12, "Precio": 419.99},
            "Portátil HP": {"Cantidad": 10, "Precio": 449.99},
            "Mouse Logitech": {"Cantidad": 30, "Precio": 39.99}
        }
        
        if registro_venta in Diccionario_Productos:
            cantidad_vendida = int(input("Ingrese la cantidad vendida: "))
            if cantidad_vendida <= Diccionario_Productos[registro_venta]["Cantidad"]:
                Diccionario_Productos[registro_venta]["Cantidad"] -= cantidad_vendida
                print(f"Venta registrada: {cantidad_vendida} unidades de {registro_venta} vendidas.")
                print(f"Cantidad restante en inventario: {Diccionario_Productos[registro_venta]['Cantidad']}")
                print(f"Total de la venta: ${cantidad_vendida * Diccionario_Productos[registro_venta]['Precio']}")
            else:
                print("Cantidad vendida excede la cantidad en inventario.")
        else:
            print("Producto no encontrado.")

    elif opcion == 6:
        print("\nNuevos productos registrados:")
        if not inventario:
            print("Aún no se ha registrado ningún producto nuevo.")
        else:
            for idx, producto in enumerate(inventario, start=1):
                print(f"{idx}. {producto['producto']} (Cantidad: {producto['cantidad']}, Precio: {producto['precio']})")


    elif opcion == 7:
        print("Saliendo del sistema...")
        print("Gracias por utilizar el sistema de gestión de inventario.")
        verdadero = False
    else:
        print("Opción inválida. Por favor, selecciona una opción del menú.")


