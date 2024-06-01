import sys
from pathlib import Path
from datetime import datetime
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QGridLayout, QFileDialog, QListWidgetItem, QDialog, QInputDialog, QComboBox, QWidget, QListWidget, QLabel, QPushButton, QFormLayout, QLineEdit, QMessageBox
from PyQt6.QtGui import QIcon, QColor

class Trabajador:

    def __init__(self, id:int, nombre, edad, puesto, salario_anual, contrasena) -> None:
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.puesto = puesto
        self.salario_anual = salario_anual 
        self.contrasena = contrasena

class Coche:

    def __init__(self, marca, modelo, num_serie, ano, fecha_ingreso, condicion, color, precio) -> None:
        self.marca = marca
        self.modelo = modelo
        self.num_serie = num_serie
        self.ano = ano
        self.fecha_ingreso = fecha_ingreso
        self.condicion = condicion
        self.color = color
        self.precio = precio

class Cliente:

    def __init__(self, correo, nombre, edad, num_telefonico) -> None:
        self.correo = correo
        self.nombre = nombre
        self.edad = edad
        self.num_telefonico = num_telefonico

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setCentralWidget(self.iniciarventana())
        self.show()
        self.clientes = []
        self.trabajadores = [] 
        self.coches = []

    def iniciarventana(self):
        self.setWindowTitle("Concecionaria SAHISP")
        self.setGeometry(100, 100, 500, 500)

        # Widget central
        central_widget = QWidget(self)
        form_layout = QGridLayout(central_widget)

        self.label_consecionaria = QLabel("Concecionaria SAHISP")
        self.label_elegir_rol = QLabel("          Elija su rol") #Tiene los espacios para que quede centrado 
        self.seleccionar_rol1 = QPushButton("Trabajador")
        self.seleccionar_rol11 = QPushButton("Cliente")

        form_layout.addWidget(self.label_consecionaria, 0,1)
        form_layout.addWidget(self.label_elegir_rol, 1,1)
        form_layout.addWidget(self.seleccionar_rol1, 2,0,1,3)
        form_layout.addWidget(self.seleccionar_rol11, 3,0,1,3)

        self.seleccionar_rol1.clicked.connect(self.show_login_window)
        self.seleccionar_rol11.clicked.connect(self.ventana1_cliente)

        central_widget.setLayout(form_layout)

        return central_widget

    def show_login_window(self):
        self.setWindowTitle("Log in")
        self.setGeometry(100, 100, 500, 500)

        # Widget central
        central_widget = QWidget(self)
        form_layout = QGridLayout(central_widget)

        self.label_usuario = QLabel("ID")
        self.label_contraseña = QLabel("Contraseña")
        self.line_edit_usuario = QLineEdit()
        self.line_edit_password = QLineEdit()
        self.pushbotton_login = QPushButton("Login")
        self.pushbotton_back = QPushButton("Back")

        self.line_edit_password.setEchoMode(QLineEdit.EchoMode.Password)

        form_layout.addWidget(self.label_usuario, 0,0)
        form_layout.addWidget(self.line_edit_usuario, 0,1)
        form_layout.addWidget(self.label_contraseña, 1,0)
        form_layout.addWidget(self.line_edit_password, 1,1)
        form_layout.addWidget(self.pushbotton_login, 2,0,1,2)
        form_layout.addWidget(self.pushbotton_back, 3,0,1,2)

        self.pushbotton_login.clicked.connect(self.newWindow_bienvenido)
        self.pushbotton_back.clicked.connect(self.show_inicio)

        self.setCentralWidget(central_widget)
        self.show()
        return central_widget

    def newWindow_bienvenido(self):
        username = self.line_edit_usuario.text()
        password = self.line_edit_password.text()
        path = Path("Trabajadores.txt")

        self.leer_txt_trabajadores(path)

        for trabajador in self.trabajadores:
            if username == trabajador.id and password == trabajador.contrasena:
                band = True
                break
            else:
                band = False

        if band:
            QMessageBox.information(
                self, "Bienvenido", f"Bienvenido a sistema"
            )
            self.ventana1_trabajador()
        else:
            QMessageBox.critical(self, "Error", f"El usuario o el password no son correctos")
            self.refresh()

    def refresh(self):
        self.line_edit_usuario.clear()
        self.line_edit_password.clear()

    def refresh_agregar_coches(self):
        self.linedit_marca.clear()
        self.linedit_modelo.clear()
        self.linedit_num_serie.clear()
        self.linedit_ano.clear()
        self.linedit_fecha_ingreso.clear()
        self.linedit_condicion.clear()
        self.linedit_color.clear()
        self.linedit_precio.clear()

    def refresh_agregar_trabajador(self):
        self.linedit_nombre.clear()
        self.linedit_edad.clear()
        self.linedit_puesto.clear()
        self.linedit_salario_anual.clear()
        self.linedit_contrasena_usuario.clear()

    def close(self):
        super().close()

    def show_inicio(self):
        self.setCentralWidget(self.iniciarventana())

    def show_ventana1_trabajador(self):
        self.setCentralWidget(self.ventana1_trabajador())

    def show_log_in(self):
        self.setCentralWidget(self.show_login_window())

    def leer_txt_trabajadores(self, ruta_archivo):
        ruta_archivo = Path(ruta_archivo)
        if ruta_archivo.exists():
            with ruta_archivo.open('r', encoding='utf-8') as archivo:
                encabezados = archivo.readline().strip().split('|')
                for linea in archivo:
                    campos = linea.strip().split('|')
                    registro = Trabajador(
                        campos[0], campos[1], campos[2], campos[3], campos[4], campos[5]
                    )
                    self.trabajadores.append(registro)
            print("Trabajadores leídos del archivo correctamente.")

    def agregar_trabajador_txt(self, ruta_archivo):
        with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write("ID|Nombre|Edad|Puesto|Salario Anual|Contraseña\n")
            for trabajador in self.trabajadores:
                linea = f"{trabajador.id}|{trabajador.nombre}|{trabajador.edad}|{trabajador.puesto}|{trabajador.salario_anual}|{trabajador.contrasena}\n"
                archivo.write(linea)

    def ventana1_trabajador(self):
        self.setWindowTitle("Menú Trabajador")
        self.setGeometry(100, 100, 500, 500)

        # Widget central
        central_widget = QWidget(self)
        form_layout = QGridLayout(central_widget)

        self.botton_dar_alta_coche = QPushButton("Dar de alta coche")
        self.botton_ver_coches = QPushButton("Ver Coches en Inventario")
        self.botton_dar_alta_trabajador = QPushButton("Dar de alta a un nuevo trabajador")
        self.botton_volver_menu_trabajador = QPushButton("Back")

        form_layout.addWidget(self.botton_dar_alta_coche, 0,0)
        form_layout.addWidget(self.botton_ver_coches, 1,0)
        form_layout.addWidget(self.botton_dar_alta_trabajador, 2,0)
        form_layout.addWidget(self.botton_volver_menu_trabajador, 3,0)

        self.botton_dar_alta_coche.clicked.connect(self.ventana_dar_alta_coche)
        self.botton_ver_coches.clicked.connect(self.ventana_ver_coches_en_inventario)
        self.botton_dar_alta_trabajador.clicked.connect(self.ventana_dar_alta_trabajador)
        self.botton_volver_menu_trabajador.clicked.connect(self.show_log_in)

        self.setCentralWidget(central_widget)
        self.show()
        return central_widget

    def ventana_dar_alta_coche(self):
        self.setWindowTitle("Dar de alta coche")
        self.setGeometry(100, 100, 500, 500)

        # Widget central
        central_widget = QWidget(self)
        form_layout = QGridLayout(central_widget)

        self.label_dar_alta_coche = QLabel("Ingrese los datos del coche: ")
        self.label_marca = QLabel("Marca: ")
        self.linedit_marca = QLineEdit()
        self.label_modelo = QLabel("Modelo: ")
        self.linedit_modelo = QLineEdit()
        self.label_num_serie = QLabel("Número de Serie: ")
        self.linedit_num_serie = QLineEdit()
        self.label_ano = QLabel("Año: ")
        self.linedit_ano = QLineEdit()
        self.label_fecha_ingreso = QLabel("Fecha de ingreso del coche en formato dd/mm/aa: ")
        self.linedit_fecha_ingreso = QLineEdit()
        self.label_condicion = QLabel("Condición del coche (Excelente, Buena, Regular, Mala): ")
        self.linedit_condicion = QLineEdit()
        self.label_color = QLabel("Color: ")
        self.linedit_color = QLineEdit()
        self.label_precio = QLabel("Precio en MXN: ")
        self.linedit_precio = QLineEdit()
        back_botton = QPushButton("Back")
        agregar_botton = QPushButton("Agregar")

        form_layout.addWidget(self.label_dar_alta_coche, 0,0)
        form_layout.addWidget(self.label_marca, 1,0)
        form_layout.addWidget(self.linedit_marca, 1,1)
        form_layout.addWidget(self.label_modelo, 2,0)
        form_layout.addWidget(self.linedit_modelo, 2,1)
        form_layout.addWidget(self.label_num_serie, 3,0)
        form_layout.addWidget(self.linedit_num_serie, 3,1)
        form_layout.addWidget(self.label_ano, 4,0)
        form_layout.addWidget(self.linedit_ano, 4,1)
        form_layout.addWidget(self.label_fecha_ingreso, 5,0)
        form_layout.addWidget(self.linedit_fecha_ingreso, 5,1)
        form_layout.addWidget(self.label_condicion, 6,0)
        form_layout.addWidget(self.linedit_condicion, 6,1)
        form_layout.addWidget(self.label_color, 7,0)
        form_layout.addWidget(self.linedit_color, 7,1)
        form_layout.addWidget(self.label_precio, 8,0)
        form_layout.addWidget(self.linedit_precio, 8,1)
        form_layout.addWidget(back_botton, 10,0,1,2)
        form_layout.addWidget(agregar_botton, 9,0,1,2)

        agregar_botton.clicked.connect(self.newWindow_coche_agregado_exitosamente)
        back_botton.clicked.connect(self.show_ventana1_trabajador)

        self.setCentralWidget(central_widget)
        self.show()

    def newWindow_coche_agregado_exitosamente(self):
        coche_objeto = Coche(
            marca = self.linedit_marca.text(),
            modelo = self.linedit_modelo.text(),
            num_serie = self.linedit_num_serie.text(),
            ano = self.linedit_ano.text(),
            fecha_ingreso = self.linedit_fecha_ingreso.text(),
            condicion = self.linedit_condicion.text(),
            color = self.linedit_color.text(),
            precio = self.linedit_precio.text()
        )

        self.coches.clear()

        path = Path("Coches.txt")

        self.leer_txt_coches(path)

        for coche in self.coches:
            if coche.num_serie == coche_objeto.num_serie:
                QMessageBox.critical(
                    self, "Error", f"Ese coche ya fue agregado previamente"
                )
                self.refresh_agregar_coches()
                break
        else:
            QMessageBox.information(self, "Coche agregado exitosamente", f"El coche fue agregado correctamente")
            self.coches.append(coche_objeto)
            self.agregar_coche_txt(path)
            self.refresh_agregar_coches()

    def leer_txt_coches(self, ruta_archivo):
        ruta_archivo = Path(ruta_archivo)
        if ruta_archivo.exists():
            with ruta_archivo.open('r', encoding='utf-8') as archivo:
                encabezados = archivo.readline().strip().split('|')
                for linea in archivo:
                    campos = linea.strip().split('|')
                    registro = Coche(
                        campos[0], campos[1], campos[2], campos[3], campos[4], campos[5], campos[6], campos[7]
                    )
                    self.coches.append(registro)
            print("Coches leídos del archivo correctamente.")

    def agregar_coche_txt(self, ruta_archivo):
        with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write("Marca|Modelo|Número de Serie|Año|Fecha de Ingreso|Condición|Color|Precio\n")
            for coche in self.coches:
                linea = f"{coche.marca}|{coche.modelo}|{coche.num_serie}|{coche.ano}|{coche.fecha_ingreso}|{coche.condicion}|{coche.color}|{coche.precio}\n"
                archivo.write(linea)

    def ventana_ver_coches_en_inventario(self):
        self.setWindowTitle("Ver coches")
        self.setGeometry(100, 100, 500, 500)

        # Widget central
        central_widget = QWidget(self)
        form_layout = QGridLayout(central_widget)
        back_botton = QPushButton("Back")

        self.list_coches = QListWidget() #despliega una lista

        form_layout.addWidget(self.list_coches, 0,0)
        form_layout.addWidget(back_botton, 1,0)

        self.setCentralWidget(central_widget)
        self.show()

        self.imprimir_coches()

        back_botton.clicked.connect(self.show_ventana1_trabajador)

    def imprimir_coches(self):
        self.coches.clear()

        self.leer_txt_coches("Coches.txt")

        self.list_coches.clear()

        for coche in self.coches:
            item_coche = QListWidgetItem(f"Marca: {coche.marca}, Modelo: {coche.modelo}, Número de Serie: {coche.num_serie}, Año: {coche.ano}, Fecha Ingreso: {coche.fecha_ingreso}, Condición: {coche.condicion}, Color: {coche.color}, Precio: {coche.precio}")
            self.list_coches.addItem(item_coche)

    def ventana_dar_alta_trabajador(self):
        self.setWindowTitle("Dar de alta trabajador")
        self.setGeometry(100, 100, 500, 500)

        # Widget central
        central_widget = QWidget(self)
        form_layout = QGridLayout(central_widget)

        self.label_dar_alta_trabajador = QLabel("Ingrese los datos del nuevo trabajador: ")
        self.label_nombre = QLabel("Nombre: ")
        self.linedit_nombre = QLineEdit()
        self.label_edad = QLabel("Edad: ")
        self.linedit_edad = QLineEdit()
        self.label_puesto = QLabel("Puesto: ")
        self.linedit_puesto = QLineEdit()
        self.label_salario_anual = QLabel("Salario Anual en MXN: ")
        self.linedit_salario_anual = QLineEdit()
        self.label_contrasena_usuario = QLabel("Contraseña: ")
        self.linedit_contrasena_usuario = QLineEdit()

        agregar_botton = QPushButton("Agregar nuevo usuario")
        back_botton = QPushButton("Back")

        form_layout.addWidget(self.label_dar_alta_trabajador, 0,0)
        form_layout.addWidget(self.label_nombre, 1,0)
        form_layout.addWidget(self.linedit_nombre, 1,1)
        form_layout.addWidget(self.label_edad, 2,0)
        form_layout.addWidget(self.linedit_edad, 2,1)
        form_layout.addWidget(self.label_puesto, 3,0)
        form_layout.addWidget(self.linedit_puesto, 3,1)
        form_layout.addWidget(self.label_salario_anual, 4,0)
        form_layout.addWidget(self.linedit_salario_anual, 4,1)
        form_layout.addWidget(self.label_contrasena_usuario, 5,0)
        form_layout.addWidget(self.linedit_contrasena_usuario, 5,1)

        form_layout.addWidget(agregar_botton, 6,0,1,2)
        form_layout.addWidget(back_botton, 7,0,1,2)

        agregar_botton.clicked.connect(self.newWindow_trabajador_agregado_exitosamente)
        back_botton.clicked.connect(self.show_ventana1_trabajador)

        self.setCentralWidget(central_widget)
        self.show()

    def newWindow_trabajador_agregado_exitosamente(self):
        self.trabajadores.clear()

        self.leer_txt_trabajadores("Trabajadores.txt")

        ID_ultimo = int(self.trabajadores[len(self.trabajadores)-1].id)

        trabajador_objeto = Trabajador(
            id = ID_ultimo+1,
            nombre = self.linedit_nombre.text(),
            edad = self.linedit_edad.text(),
            puesto = self.linedit_puesto.text(),
            salario_anual = self.linedit_salario_anual.text(),
            contrasena = self.linedit_contrasena_usuario.text()
        )

        self.trabajadores.clear()

        path = Path("Trabajadores.txt")

        self.leer_txt_trabajadores(path)

        for trabajador in self.trabajadores:
            if trabajador.id == trabajador_objeto.id:
                QMessageBox.critical(
                    self, "Error", f"Ese trabajador ya se encuentra en la base de datos"
                )
                self.refresh_agregar_trabajador()
                break
        else:
            QMessageBox.information(self, "Usuario agregado exitosamente", f"El usuario fue agregado correctamente")
            self.trabajadores.append(trabajador_objeto)
            self.agregar_trabajador_txt(path)
            self.refresh_agregar_trabajador()

    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def ventana1_cliente(self):
        self.setWindowTitle("Bienvenido")
        self.setGeometry(100, 100, 500, 500)

        # Widget central
        central_widget = QWidget(self)
        form_layout = QGridLayout(central_widget)

        self.label_ya_nos_habias_visitado = QLabel("Ya nos habías visitado antes?")
        self.pushbotton_si = QPushButton("Si")
        self.pushbotton_no = QPushButton("No")

        form_layout.addWidget(self.label_ya_nos_habias_visitado, 0,0)
        form_layout.addWidget(self.pushbotton_si, 1,0)
        form_layout.addWidget(self.pushbotton_no, 2,0)

        self.pushbotton_si.clicked.connect(self.ventana2_cliente)
        self.pushbotton_no.clicked.connect(self.ventana2_1_cliente)

        self.setCentralWidget(central_widget)
        self.show()
        return central_widget

    def ventana2_cliente(self):
        self.setWindowTitle("Checar correo")
        self.setGeometry(100, 100, 500, 500)

        # Widget central
        central_widget = QWidget(self)
        form_layout = QGridLayout(central_widget)

        self.label_ingrese_su_correo_cliente = QLabel("Ingrese su correo: ")
        self.linedit_ingresar_correo_cliente = QLineEdit()
        botton_continuar = QPushButton("Continuar")
        back_botton = QPushButton("Back")

        form_layout.addWidget(self.label_ingrese_su_correo_cliente, 0,0)
        form_layout.addWidget(self.linedit_ingresar_correo_cliente, 0,1)
        form_layout.addWidget(botton_continuar, 1,0,1,2)
        form_layout.addWidget(back_botton, 2,0,1,2)

        botton_continuar.clicked.connect(self.verificar_cliente)
        back_botton.clicked.connect(self.show_ventana1_cliente)

        self.setCentralWidget(central_widget)
        self.show()
        return central_widget

    def ventana2_1_cliente(self):
        self.setWindowTitle("Agregar Cliente")
        self.setGeometry(100, 100, 500, 500)

        # Widget central
        central_widget = QWidget(self)
        form_layout = QGridLayout(central_widget)

        self.label_ingrese_su_correo_cliente_2_1 = QLabel("Ingrese su correo: ")
        self.label_ingresar_nombre_cliente = QLabel("Ingrese su nombre: ")
        self.label_ingresar_edad_cliente = QLabel("Ingrese su edad: ")
        self.label_ingresar_num_tel = QLabel("Ingrese su número telefónico: ")

        self.linedit_ingrese_su_correo_cliente_2_1 = QLineEdit()
        self.linedit_ingresar_nombre_cliente = QLineEdit()
        self.linedit_ingresar_edad_cliente = QLineEdit()
        self.linedit_ingresar_num_tel = QLineEdit()

        botton_continuar = QPushButton("Continuar")
        back_botton = QPushButton("Back")

        form_layout.addWidget(self.label_ingrese_su_correo_cliente_2_1, 0,0)
        form_layout.addWidget(self.linedit_ingrese_su_correo_cliente_2_1, 0,1)
        form_layout.addWidget(self.label_ingresar_nombre_cliente, 1,0)
        form_layout.addWidget(self.linedit_ingresar_nombre_cliente, 1,1)
        form_layout.addWidget(self.label_ingresar_edad_cliente, 2,0)
        form_layout.addWidget(self.linedit_ingresar_edad_cliente, 2,1)
        form_layout.addWidget(self.label_ingresar_num_tel, 3,0)
        form_layout.addWidget(self.linedit_ingresar_num_tel, 3,1)

        form_layout.addWidget(botton_continuar, 4,0,1,2)
        form_layout.addWidget(back_botton, 5,0,1,2)

        botton_continuar.clicked.connect(self.registrar_cliente)
        back_botton.clicked.connect(self.show_ventana1_cliente)

        self.setCentralWidget(central_widget)
        self.show()
        return central_widget

    def verificar_cliente(self):
        correo = self.linedit_ingresar_correo_cliente.text()
        path = Path("Clientes.txt")
        self.leer_txt_clientes(path)
        for cliente in self.clientes:
            if cliente.correo == correo:
                QMessageBox.information(self, "Bienvenido", f"Bienvenido de nuevo, {cliente.nombre}")
                self.ventana3_cliente()
                return
        QMessageBox.critical(self, "Error", f"Correo no encontrado. Por favor registrese.")
        self.show_ventana1_cliente()

    def registrar_cliente(self):
        cliente_objeto = Cliente(
            correo = self.linedit_ingrese_su_correo_cliente_2_1.text(),
            nombre = self.linedit_ingresar_nombre_cliente.text(),
            edad = self.linedit_ingresar_edad_cliente.text(),
            num_telefonico = self.linedit_ingresar_num_tel.text()
        )

        self.clientes.clear()

        path = Path("Clientes.txt")

        self.leer_txt_clientes(path)

        for cliente in self.clientes:
            if cliente.correo == cliente_objeto.correo:
                QMessageBox.critical(
                    self, "Error", f"Ese cliente ya se encuentra en la base de datos"
                )
                self.refresh_agregar_cliente()
                break
        else:
            QMessageBox.information(self, "Cliente agregado exitosamente", f"El cliente fue agregado correctamente")
            self.clientes.append(cliente_objeto)
            self.agregar_cliente_txt(path)
            self.refresh_agregar_cliente()
            self.ventana3_cliente()

    def leer_txt_clientes(self, ruta_archivo):
        ruta_archivo = Path(ruta_archivo)
        if ruta_archivo.exists():
            with ruta_archivo.open('r', encoding='utf-8') as archivo:
                encabezados = archivo.readline().strip().split('|')
                for linea in archivo:
                    campos = linea.strip().split('|')
                    registro = Cliente(
                        campos[0], campos[1], campos[2], campos[3]
                    )
                    self.clientes.append(registro)
            print("Clientes leídos del archivo correctamente.")

    def agregar_cliente_txt(self, ruta_archivo):
        with open(ruta_archivo, 'w', encoding='utf-8') as archivo:
            archivo.write("Correo|Nombre|Edad|Número Tel\n")
            for cliente in self.clientes:
                linea = f"{cliente.correo}|{cliente.nombre}|{cliente.edad}|{cliente.num_telefonico}\n"
                archivo.write(linea)

    def refresh_agregar_cliente(self):
        self.linedit_ingrese_su_correo_cliente_2_1.clear()
        self.linedit_ingresar_nombre_cliente.clear()
        self.linedit_ingresar_edad_cliente.clear()
        self.linedit_ingresar_num_tel.clear()

    def show_ventana1_cliente(self):
        self.setCentralWidget(self.ventana1_cliente())

    def ventana3_cliente(self):
        self.setWindowTitle("Selección de Acción de Cliente")
        self.setGeometry(100, 100, 500, 500)

        # Widget central
        central_widget = QWidget(self)
        form_layout = QGridLayout(central_widget)

        self.label_ingresar_que_desea_hacer = QLabel("Seleccione que desea hacer hoy:  ")
        self.botton_comprar = QPushButton("Comprar Coche")
        self.botton_vender = QPushButton("Vender Coche ")
        back_botton = QPushButton("Back")

        form_layout.addWidget(self.label_ingresar_que_desea_hacer, 0,0)
        form_layout.addWidget(self.botton_comprar, 1,0)
        form_layout.addWidget(self.botton_vender, 2,0)
        form_layout.addWidget(back_botton, 3,0)

        self.botton_comprar.clicked.connect(self.ventana_comprar_coche)
        self.botton_vender.clicked.connect(self.ventana_vender_coche)
        back_botton.clicked.connect(self.show_ventana1_cliente)

        self.setCentralWidget(central_widget)
        self.show()
        return central_widget

    def ventana_comprar_coche(self):
        self.setWindowTitle("Comprar Coche")
        self.setGeometry(100, 100, 500, 500)

        # Widget central
        central_widget = QWidget(self)
        form_layout = QGridLayout(central_widget)

        self.label_seleccionar_coche = QLabel("Seleccione el coche que desea comprar:")
        self.list_coches_comprar = QListWidget()
        self.linedit_num_serie_comprar = QLineEdit()
        self.label_num_serie_comprar = QLabel("Número de Serie del coche seleccionado:")
        self.botton_comprar_coche = QPushButton("Comprar")
        back_botton = QPushButton("Back")

        form_layout.addWidget(self.label_seleccionar_coche, 0,0)
        form_layout.addWidget(self.list_coches_comprar, 1,0)
        form_layout.addWidget(self.label_num_serie_comprar, 2,0)
        form_layout.addWidget(self.linedit_num_serie_comprar, 2,1)
        form_layout.addWidget(self.botton_comprar_coche, 3,0,1,2)
        form_layout.addWidget(back_botton, 4,0,1,2)

        self.setCentralWidget(central_widget)
        self.show()

        self.imprimir_coches_comprar()

        self.botton_comprar_coche.clicked.connect(self.comprar_coche)
        back_botton.clicked.connect(self.show_ventana1_cliente)

    def imprimir_coches_comprar(self):
        self.coches.clear()

        self.leer_txt_coches("Coches.txt")

        self.list_coches_comprar.clear()

        for coche in self.coches:
            item_coche = QListWidgetItem(f"Marca: {coche.marca}, Modelo: {coche.modelo}, Número de Serie: {coche.num_serie}, Año: {coche.ano}, Fecha Ingreso: {coche.fecha_ingreso}, Condición: {coche.condicion}, Color: {coche.color}, Precio: {coche.precio}")
            self.list_coches_comprar.addItem(item_coche)

    def comprar_coche(self):
        num_serie = self.linedit_num_serie_comprar.text()
        path = Path("Coches.txt")

        self.coches.clear()
        self.leer_txt_coches(path)

        for coche in self.coches:
            if coche.num_serie == num_serie:
                QMessageBox.information(self, "Compra exitosa", f"Ha comprado el coche: {coche.marca} {coche.modelo}")
                self.coches.remove(coche)
                self.agregar_coche_txt(path)
                self.show_ventana1_cliente()
                return

        QMessageBox.critical(self, "Error", "Número de Serie no encontrado.")
        self.show_ventana1_cliente()

    def ventana_vender_coche(self):
        self.setWindowTitle("Vender Coche")
        self.setGeometry(100, 100, 500, 500)

        # Widget central
        central_widget = QWidget(self)
        form_layout = QGridLayout(central_widget)

        self.label_ingrese_datos_coche = QLabel("Ingrese los datos del coche que desea vender:")
        self.label_marca_vender = QLabel("Marca: ")
        self.linedit_marca_vender = QLineEdit()
        self.label_modelo_vender = QLabel("Modelo: ")
        self.linedit_modelo_vender = QLineEdit()
        self.label_num_serie_vender = QLabel("Número de Serie: ")
        self.linedit_num_serie_vender = QLineEdit()
        self.label_ano_vender = QLabel("Año: ")
        self.linedit_ano_vender = QLineEdit()
        self.label_fecha_ingreso_vender = QLabel("Fecha de ingreso del coche en formato dd/mm/aa: ")
        self.linedit_fecha_ingreso_vender = QLineEdit()
        self.label_condicion_vender = QLabel("Condición del coche (Excelente, Buena, Regular, Mala): ")
        self.linedit_condicion_vender = QLineEdit()
        self.label_color_vender = QLabel("Color: ")
        self.linedit_color_vender = QLineEdit()
        self.label_precio_vender = QLabel("Precio en MXN: ")
        self.linedit_precio_vender = QLineEdit()
        back_botton = QPushButton("Back")
        agregar_botton = QPushButton("Vender")

        form_layout.addWidget(self.label_ingrese_datos_coche, 0,0)
        form_layout.addWidget(self.label_marca_vender, 1,0)
        form_layout.addWidget(self.linedit_marca_vender, 1,1)
        form_layout.addWidget(self.label_modelo_vender, 2,0)
        form_layout.addWidget(self.linedit_modelo_vender, 2,1)
        form_layout.addWidget(self.label_num_serie_vender, 3,0)
        form_layout.addWidget(self.linedit_num_serie_vender, 3,1)
        form_layout.addWidget(self.label_ano_vender, 4,0)
        form_layout.addWidget(self.linedit_ano_vender, 4,1)
        form_layout.addWidget(self.label_fecha_ingreso_vender, 5,0)
        form_layout.addWidget(self.linedit_fecha_ingreso_vender, 5,1)
        form_layout.addWidget(self.label_condicion_vender, 6,0)
        form_layout.addWidget(self.linedit_condicion_vender, 6,1)
        form_layout.addWidget(self.label_color_vender, 7,0)
        form_layout.addWidget(self.linedit_color_vender, 7,1)
        form_layout.addWidget(self.label_precio_vender, 8,0)
        form_layout.addWidget(self.linedit_precio_vender, 8,1)
        form_layout.addWidget(back_botton, 10,0,1,2)
        form_layout.addWidget(agregar_botton, 9,0,1,2)

        agregar_botton.clicked.connect(self.vender_coche)
        back_botton.clicked.connect(self.show_ventana1_cliente)

        self.setCentralWidget(central_widget)
        self.show()

    def vender_coche(self):
        coche_objeto = Coche(
            marca = self.linedit_marca_vender.text(),
            modelo = self.linedit_modelo_vender.text(),
            num_serie = self.linedit_num_serie_vender.text(),
            ano = self.linedit_ano_vender.text(),
            fecha_ingreso = self.linedit_fecha_ingreso_vender.text(),
            condicion = self.linedit_condicion_vender.text(),
            color = self.linedit_color_vender.text(),
            precio = self.linedit_precio_vender.text()
        )

        self.coches.clear()

        path = Path("Coches.txt")

        self.leer_txt_coches(path)

        for coche in self.coches:
            if coche.num_serie == coche_objeto.num_serie:
                QMessageBox.critical(
                    self, "Error", f"Ese coche ya fue agregado previamente"
                )
                self.refresh_agregar_coches()
                break
        else:
            QMessageBox.information(self, "Coche vendido exitosamente", f"El coche fue agregado correctamente")
            self.coches.append(coche_objeto)
            self.agregar_coche_txt(path)
            self.refresh_agregar_coches()
            self.show_ventana1_cliente()

app = QApplication(sys.argv)

window = MainWindow()

sys.exit(app.exec())