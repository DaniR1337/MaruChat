# Forma para crear ejecutables del programa Maruchat y servidor, para el proyecto de ingeniería de comunicación

## Tabla de contenidos
- [Descripción](#descripción)
- [Uso](#Uso)
- [Licencia](#licencia)
- [QR al repositorio](#QR)
- [Contacto](#contacto)

## Descripción

Forma para crear ejecutables del programa Maruchat y servidor, para con un click hacer posible la comunicación.

## Uso 

Requisitos: 

REQUIERE Instalar pip install Pillow
REQUIERE Instalar pip install pyinstaller

Ejecutar las siguientes lineas para convertir el programa en ejecutable luego de modificar Maruchat.py y server.py con la: Dirección IPv4

pyinstaller --windowed --onefile --icon=./icoserver.ico  server.py
pyinstaller --windowed --onefile --icon=./icologo.ico  Maruchat.py

Los ejecutables se crearán en la carpeta dist (distribución) acá debe pegar las imagenes: 
- logo.png
- type.gif

## Licencia

Creative Commons Legal Code CC0 1.0 Universal, Consulte la licencia para más detalles: https://creativecommons.org/publicdomain/zero/1.0/

## QR al repositorio
[![C-digo-QR.png](https://i.postimg.cc/mgzTq1YP/C-digo-QR.png)](https://postimg.cc/PCHGvxFH)

## Contacto

- Autor: Alex Varela Quirós
- correo: alex.varela@ucr.ac.cr 
- tel: +50685525005

[![iconopeque.jpg](https://i.postimg.cc/hvtdRL0p/iconopeque.jpg)](https://postimg.cc/k6L4xtzb)

