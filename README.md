# Concesionaria

¡Bienvenido al proyecto de Concesionaria! Este es un sistema de gestión de inventario de coches desarrollado en Python, diseñado para ser utilizado tanto por clientes como por el personal de ventas de la concesionaria.

## Descripción del Proyecto

Este proyecto tiene como objetivo facilitar la administración de coches dentro de una concesionaria, permitiendo a los clientes ver los coches disponibles para la compra y al personal de ventas dar de alta nuevos coches y revisar el inventario existente.

## Funcionalidades

- *Clientes:*
  - Ver coches disponibles para la compra.
  - Indicar interés en comprar un coche.

- *Personal de Ventas:*
  - Dar de alta nuevos coches en el inventario.
  - Revisar el inventario de coches.

## Cómo Empezar

Para empezar a utilizar este proyecto, sigue los pasos a continuación:

### Prerrequisitos
 
Asegúrate de tener Python instalado en tu máquina. Puedes descargarlo desde [python.org](https://www.python.org/).

### Instalación

1. Clona el repositorio en tu máquina local:

   sh
   git clone https://github.com/Emiliox11/Concesionaria.git
   cd Concesionaria
   

2. Ejecuta el script principal:

   sh
   python concesionaria.py
   

### Uso

Cuando ejecutes el script, se te presentarán opciones para interactuar como cliente o como personal de ventas.

- Si seleccionas la opción de *Cliente*, podrás ver los coches disponibles para la compra y decidir si quieres adquirir uno.
- Si seleccionas la opción de *Personal de Ventas*, podrás agregar nuevos coches al inventario y revisar los coches actualmente disponibles.

## Ejemplo de Uso

Aquí tienes un ejemplo de cómo interactuar con el sistema:

plaintext
Hola, bienvenido, porfavor seleccione 1 si es cliente o 2 si es personal de ventas de la concesionaria:

1. Cliente
2. Personal de ventas de la concesionaria
3. Salir

Elija la opción deseada: 2

Hola, usted ingresó al menú de trabajadores, por favor elija la tarea a realizar:

1. Dar de alta un coche
2. Checar los coches en el inventario
3. Salir

Elija la opción deseada: 1

Ingrese la marca del coche: Toyota
Ingrese el modelo del coche: Corolla
Ingrese el número de serie del coche: ABC123
Ingrese el año del coche: 2022
Ingrese la fecha de ingreso del coche en formato dd/mm/aa: 01/05/23
Ingrese la condición del coche (Excelente, Buena, Regular, Mala): Excelente
Ingrese el color del coche: Blanco
Ingrese el precio del coche en pesos Mexicanos: 250000

Coche agregado exitosamente.


## Contribución

Si deseas contribuir a este proyecto, por favor sigue los pasos a continuación:

1. Haz un fork del proyecto.
2. Crea una rama para tu feature (git checkout -b feature/nueva-feature).
3. Realiza tus cambios y haz commit (git commit -am 'Agrega nueva feature').
4. Empuja tus cambios a la rama (git push origin feature/nueva-feature).
5. Abre un Pull Request.
