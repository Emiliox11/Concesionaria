coches = {} 

def dar_de_alta_coche():
    marca = input("Ingrese la marca del coche: ")
    modelo = input("Ingrese el modelo del coche: ")
    num_serie = input("Ingrese el número de serie del coche: ")
    año = input("Ingrese el año del coche: ")
    año = int(año)
    fecha_ingreso = input("Ingrese la fecha de ingreso del coche en formato dd/mm/aa: ")
    condicion = input("Ingrese la condición del coche (Excelente, Buena, Regular, Mala): ")
    color = input("Ingrese el color del coche: ")
    precio = input("Ingrese el precio del coche en pesos Mexicanos: ")
    precio = int(precio)

    coche = {
        "Marca": marca,
        "Modelo": modelo,
        "NumSerie": num_serie,
        "Año": año,
        "FechaIngreso": fecha_ingreso,
        "Condición": condicion,
        "Color": color,
        "Precio": precio
    }

    clave_coche = f"coche_{len(coches) + 1}"
    coches[clave_coche] = coche
    print("Coche agregado exitosamente.")

def mostrar_coches():
    print("Los coches que tenemos actualmente en el inventario son: ")
    print("")
    for clave, coche in coches.items():
        marca = coche.get("Marca")
        modelo = coche.get("Modelo")
        NumSerie = coche.get("NumSerie")
        Anio = coche.get("Año")
        fecha_ingreso = coche.get("FechaIngreso")
        condicion = coche.get("Condición")
        color = coche.get("Color")
        precio = coche.get("Precio")

        print(clave)
        print("")
        print(f"Marca: {marca}")
        print(f"Modelo: {modelo}")
        print(f"Número de Serie: {NumSerie}")
        print(f"Año: {Anio}")
        print(f"Fecha de Ingreso: {fecha_ingreso}")
        print(f"Condición: {condicion}")
        print(f"Color: {color}")
        print(f"Precio: {precio}")
        print("")

band = True

while band == True:
    print("Menú ")
    print("")
    print("1. Agregar Coche")
    print("2. Mostrar coches")
    print("3. Salir")
    print("")
    print("Elija la opción deseada:")
    opc = int(input())

    if opc == 1:
        dar_de_alta_coche()
    elif opc == 2:
        mostrar_coches()
    elif opc == 3:
        band = False
        print("Eso es todo, hasta luego ")
