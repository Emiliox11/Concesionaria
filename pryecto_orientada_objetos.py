from pathlib import Path

coches = []
trabajadores = []
clientes = []

class Trabajador:

    def __init__(self) -> None:
        self.id = str()
        self.nombre = str()
        self.edad = int()
        self.puesto = str()
        self.salario_anual = float()
        self.contrasena = str()
        self.coches = []
        self.trabajadores = []

    def dar_de_alta_coche(self):
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
        coches.append(coche)
        print("Coche agregado exitosamente.")    
 

    def guardar_coches(self, ruta_archivo):
        with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write("Marca|Modelo|NumSerie|Año|FechaIngreso|Condición|Color|Precio\n")
            for coche in coches:
                linea = f"{coche['Marca']}|{coche['Modelo']}|{coche['NumSerie']}|{coche['Año']}|{coche['FechaIngreso']}|{coche['Condición']}|{coche['Color']}|{coche['Precio']}\n"
                archivo.write(linea)

    def agregar_coche_txt(self, ruta_archivo):
        with open(ruta_archivo, 'a', encoding='utf-8') as archivo:
            # No escribimos la cabecera (header) cada vez que guardamos, solo la primera vez.
            # archivo.write("ID|Nombre|Edad|Puesto|Salario Anual|Contraseña\n")
            for coche in coches:
                linea = f"{coche['Marca']}|{coche['Modelo']}|{coche['NumSerie']}|{coche['Año']}|{coche['FechaIngreso']}|{coche['Condición']}|{coche['Color']}|{coche['Precio']}\n"
                archivo.write(linea)            

    def leer_txt_coches(self, ruta_archivo):
        coches_txt = []
        ruta_archivo = Path(ruta_archivo)
        if ruta_archivo.exists():
            with ruta_archivo.open('r', encoding='utf-8') as archivo:
                encabezados = archivo.readline().strip().split('|')
                for linea in archivo:
                    campos = linea.strip().split('|')
                    registro = {encabezados[i]: campos[i] for i in range(len(encabezados))}
                    coches_txt.append(registro)
            # Asignar la lista de coches leídos a la lista coches de esta instancia
            self.coches = coches_txt
            print("") 
            print("Coches leídos del archivo correctamente.")
            print("")    
        else:
            print("") 
            print(f"El archivo '{ruta_archivo}' no existe.")
            print("") 

    def mostrar_coches(self):
        print("Los coches que tenemos actualmente en el inventario son: ")
        print("")
        for coche in self.coches:
            print(f"Marca: {coche['Marca']}")
            print(f"Modelo: {coche['Modelo']}")
            print(f"Número de Serie: {coche['NumSerie']}")
            print(f"Año del coche: {coche['Año']}")
            print(f"Fecha de ingreso: {coche['FechaIngreso']}")
            print(f"Condición: {coche['Condición']}")
            print(f"Color: {coche['Color']}")
            print(f"Precio: {coche['Precio']}")
            print("")
            print("")         

    def leer_txt_trabajadores(self, ruta_archivo):
        trabajadores_txt = []
        ruta_archivo = Path(ruta_archivo)
        if ruta_archivo.exists():
            with ruta_archivo.open('r', encoding='utf-8') as archivo:
                encabezados = archivo.readline().strip().split('|')
                for linea in archivo:
                    campos = linea.strip().split('|')
                    registro = {encabezados[i]: campos[i] for i in range(len(encabezados))}
                    trabajadores_txt.append(registro)
            # Asignar la lista de coches leídos a la lista coches de esta instancia
            self.trabajadores = trabajadores_txt
            print("") 
            print("Trabajadores leídos del archivo correctamente.")
            print("")    
        else:
            print("") 
            print(f"El archivo '{ruta_archivo}' no existe.")
            print("")

    def dar_de_alta_nuevo_trabajador(self):
        self.ID = input("Ingrese el ID del nuevo trabajador: ")
        self.nombre = input("Ingrese el nombre del nuevo trabajador: ")
        self.edad = int(input("Ingrese la edad del nuevo trabajador: "))
        self.puesto = input("Ingrese el puesto del nuevo trabajador: ")
        self.salario_anual = float(input("Ingrese el salario anual del nuevo trabajador: "))
        self.contrasena = input("Ingrese la contraseña del nuevo trabajador: ")

        trabajador = {
            "ID": self.ID,
            "Nombre": self.nombre,
            "Edad": self.edad,
            "Puesto": self.puesto,
            "Salario Anual": self.salario_anual,
            "Contraseña": self.contrasena
        }
        trabajadores.append(trabajador)
        print("Trabajador agregado exitosamente.")   

    def guardar_trabajador(self, ruta_archivo):
        with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write("ID|Nombre|Edad|Puesto|Salario Anual|Contraseña\n")
            for trabajador in trabajadores:
                linea = f"{trabajador['ID']}|{trabajador['Nombre']}|{trabajador['Edad']}|{trabajador['Puesto']}|{trabajador['Salario Anual']}|{trabajador['Contraseña']}\n"
                archivo.write(linea)    

    def agregar_trabajador_txt(self, ruta_archivo):
        with open(ruta_archivo, 'a', encoding='utf-8') as archivo:
            # No escribimos la cabecera (header) cada vez que guardamos, solo la primera vez.
            # archivo.write("ID|Nombre|Edad|Puesto|Salario Anual|Contraseña\n")
            for trabajador in trabajadores:
                linea = f"{trabajador['ID']}|{trabajador['Nombre']}|{trabajador['Edad']}|{trabajador['Puesto']}|{trabajador['Salario Anual']}|{trabajador['Contraseña']}\n"
                archivo.write(linea)
            

    def desplegar_menu_trabajador(self):
        
        print("Querido trabajador, porfavor ingrese su ID")
        ID = input()

        for trabajador in self.trabajadores:
            if(trabajador['ID']== ID):
                print("Por favor ingrese su contraseña: ")
                contraseña = input()
                if(trabajador['Contraseña']==contraseña):
                    print("Perfecto, se desplegará el menú para trabajador")

                    while True:
                        print("Hola, usted ingresó al menú de trabajadores, por favor elija la tarea a realizar: ")
                        print("")
                        print("1. Dar de alta un coche")
                        print("2. Checar los coches en el inventario")
                        print("3. Dar de Alta un trabajador nuevo")
                        print("4. Salir")
                        print("")
                        print("Elija la opción deseada:")
                        opc_d_c = int(input()) #opc que determina si el trabajador va a Dar de alta un coche o si va a checar los coches en inventario
                        if opc_d_c == 1:
                            self.leer_txt_coches("/Users/nikolospsihas/Downloads/coches.txt")
                            self.dar_de_alta_coche()
                            self.agregar_coche_txt("/Users/nikolospsihas/Downloads/coches.txt")
                        elif opc_d_c==2:
                            self.leer_txt_coches("/Users/nikolospsihas/Downloads/coches.txt")
                            self.mostrar_coches()
                        elif opc_d_c==3:
                            MiTrabajador.leer_txt_trabajadores("/Users/nikolospsihas/Downloads/trabajadores.txt")
                            MiTrabajador.dar_de_alta_nuevo_trabajador()
                            MiTrabajador.agregar_trabajador_txt("/Users/nikolospsihas/Downloads/trabajadores.txt")
                        elif opc_d_c==4:
                            break    
                            

                else:
                    pass     
            else:
                pass  


class Cliente:

    def __init__(self) -> None:
        self.correo = str()
        self.nombre = str()
        self.edad = int()
        self.num_telefónico = str()
        self.clientes = []

    def dar_de_alta_nuevo_cliente(self):
        self.correo = input("Ingrese su correo electrónico: ")
        self.nombre = input("Ingrese su nombre: ")
        self.edad = int(input("Ingrese su edad: "))
        self.num_telefónico = input("Ingrese su número telefónico: ")

        cliente = {
            "Correo": self.correo,
            "Nombre": self.nombre,
            "Edad": self.edad,
            "Número Telefónico": self.num_telefónico,
        }
        clientes.append(cliente)
        print("Trabajador agregado exitosamente.") 

    def guardar_cliente(self, ruta_archivo):
        with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write("Correo|Nombre|Edad|Número telefónico\n")
            for cliente in clientes:
                linea = f"{cliente['Correo']}|{cliente['Nombre']}|{cliente['Edad']}|{cliente['Número Telefónico']}\n"
                archivo.write(linea)    

    def leer_txt_clientes(self, ruta_archivo):
        clientes_txt = []
        ruta_archivo = Path(ruta_archivo)
        if ruta_archivo.exists():
            with ruta_archivo.open('r', encoding='utf-8') as archivo:
                encabezados = archivo.readline().strip().split('|')
                for linea in archivo:
                    campos = linea.strip().split('|')
                    registro = {encabezados[i]: campos[i] for i in range(len(encabezados))}
                    clientes_txt.append(registro)
            # Asignar la lista de coches leídos a la lista coches de esta instancia
            self.clientes = clientes_txt
            print("") 
            print("Trabajadores leídos del archivo correctamente.")
            print("")    
        else:
            print("") 
            print(f"El archivo '{ruta_archivo}' no existe.")
            print("")

    def agregar_cliente_txt(self, ruta_archivo):
        with open(ruta_archivo, 'a', encoding='utf-8') as archivo:
            # No escribimos la cabecera (header) cada vez que guardamos, solo la primera vez.
            # archivo.write("ID|Nombre|Edad|Puesto|Salario Anual|Contraseña\n")
            for cliente in clientes:
                linea = f"{cliente['Correo']}|{cliente['Nombre']}|{cliente['Edad']}|{cliente['Número Telefónico']}\n"
                archivo.write(linea)                     



# Ruta del archivo donde se guardarán y leerán los coches
path_coches = "/Users/nikolospsihas/Downloads/coches.txt"
path_trabajadores = "/Users/nikolospsihas/Downloads/trabajadores.txt"
path_clientes = "/Users/nikolospsihas/Downloads/clientes.txt"

MiTrabajador = Trabajador()
MiCliente = Cliente()

#MiTrabajador.leer_txt_trabajadores(path_trabajadores)
#MiTrabajador.dar_de_alta_nuevo_trabajador()
#MiTrabajador.agregar_trabajador_txt(path_trabajadores)


while True:
    print("Hola, bienvenido, porfavor seleccione 1 si es cliente o 2 si es personal de ventas de la concesionaria: ")
    print("")
    print("1. Cliente")
    print("2. Personal de ventas de la concesionario")
    print("3. Salir")
    print("")
    print("Elija la opción deseada:")
    print("")
    opc_c_p = int(input()) #opc que determina si va a ser cliente o personal de la concesionaria
    if opc_c_p == 1:
        while True:

            print("Bienvenido Cliente, ya había venido antes?")
            print("1. Si")
            print("2. No")
            print("3. Salir")
            print("")
            opc = int(input())

            if opc==1:
                print("Por favor ingrese su correo electrónico: ")
                correo_cliente = input()
                MiCliente.leer_txt_clientes(path_clientes)

                for cliente_individual in MiCliente.clientes:
                    if(cliente_individual['Correo']==correo_cliente):
                        print(f"Bienvenido {cliente_individual['Nombre']}")
                        while True:
                            print("Qué deseas hacer hoy?")
                            print("")
                            print("1. Comprar coche")
                            print("2. Vender Coche")
                            print("3. Salir")
                            print("")
                            opc1111 = int(input())

                            if opc1111 == 1:
                                print("Nos falta que un cliente pueda comprar un coche")
                            elif opc1111 == 2:
                                print("Nos falta que un cliente pueda vender un coche")
                            elif opc1111 == 3:
                                break    
                    else:
                        pass    

            elif opc==2:
                print("Necesito que se registre primero porfavor")
                MiCliente.leer_txt_clientes(path_clientes)
                MiCliente.dar_de_alta_nuevo_cliente()
                MiCliente.agregar_cliente_txt(path_clientes)
            elif opc==3:
                break    

    elif opc_c_p == 2:
        MiTrabajador.leer_txt_trabajadores(path_trabajadores)
        MiTrabajador.desplegar_menu_trabajador()

    elif opc_c_p==3:
        break    
