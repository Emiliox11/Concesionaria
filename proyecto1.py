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
    print("Hola, bienvenido, porfavor seleccione 1 si es cliente o 2 si es personal de ventas de la concesionaria: ")
    print("")
    print("1. Cliente")
    print("2. Personal de ventas de la concesionario")
    print("3. Salir")
    print("")
    print("Elija la opción deseada:")
    opc_c_p = int(input()) #opc que determina si va a ser cliente o personal de la concesionaria

    if opc_c_p == 1:
        band1=True
        while band1 == True:
            print("Hola Cliente, por favor seleccione la opción que desee ejecutar: ")
            print("")
            print("1. Comprar un coche")
            print("2. Vender un coche")
            print("3. Salir")
            print("")
            print("Elija la opción deseada:")
            opc_c_v = int(input()) #opc que determina si va a ser cliente va a comprar o a vender
            if opc_c_v == 1:
                if len(coches)>0:
                    mostrar_coches()
                    print("")
                    print("Le gustaría comprar algún coche? (Por favor responda si o no) ")
                    deci = str(input())
                    deci = deci.lower()
                    if deci == "si":
                        print("El usuario si quiso comprar uno de los coches")#esto se va a eliminar cuando se continúe con esta parte del código 
                        pass #eso se va a modificar más adelante en el código
                    elif deci == "no":
                        print("Es una pena que no le gustara ninguno, vuelva pronto para ver más opciones")
                    else:
                        print("No ingresó una respuesta válida, volviendo al menú ")
                else:
                    print("Lo sentimos, no tenemos coches en existencia, vuelva al menú principal")
            elif opc_c_v==2:
                pass #Falta agregar aquí para que el usuario registre los datos del coche nuevo
            elif opc_c_v==3:
                band1 = False
                print("Volviendo al menú principal")
    elif opc_c_p == 2:
        band2=True
        while band2 == True:
            print("Hola, usted ingresó al menú de trabajadores, por favor elija la tarea a realizar: ")
            print("")
            print("1. Dar de alta un coche")
            print("2. Checar los coches en el inventario")
            print("3. Salir")
            print("")
            print("Elija la opción deseada:")
            opc_d_c = int(input()) #opc que determina si el trabajador va a Dar de alta un coche o si va a checar los coches en inventario
            if opc_d_c == 1:
                dar_de_alta_coche()
            elif opc_d_c==2:
                if len(coches)>0:
                    mostrar_coches()
                else:
                    print("No hay coches registrados en el inventario")
            elif opc_d_c==3:
                band2 = False
                print("Volviendo al menú principal")
    elif opc_c_p == 3:
        band = False
        print("Eso es todo, hasta luego ")
