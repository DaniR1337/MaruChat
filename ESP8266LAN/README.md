# Código para la ESP8266, para el proyecto de ingeniería de comunicación

## Tabla de contenidos
- [Descripción](#descripción)
- [Uso](#Uso)
- [Licencia](#licencia)
- [Contacto](#contacto)

## Descripción

Código para configurar el ESP8266 como un punto de acceso WiFi sin conexión a Internet. Los dispositivos podrán conectarse
a la red WiFi con el nombre de red y contraseña especificados.

## Uso 

Requisitos: 

REQUIERE Instalar Plugin del ESP8266 para Arduino.
- ir a archivo>Preferencias y en la casilla  “Gestor de URLs Adicionales de Tarjetas” 
- agregamos: http://arduino.esp8266.com/stable/package_esp8266com_index.json

REQUIERE Instalar controladores del puerto COM virtual (VCP) del puente USB a UART CP210x
necesarios para el funcionamiento del dispositivo como un puerto COM virtual
se puede bajar de: https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers?tab=downloads 
o con el enlace directo: https://github.com/nodemcu/nodemcu-devkit/raw/master/Drivers/CH341SER_WINDOWS.zip 

Compilar y y cargar sobre la placa ESP8266 desde Arduino IDE.

## Licencia

Creative Commons Legal Code CC0 1.0 Universal, Consulte la licencia para más detalles: https://creativecommons.org/publicdomain/zero/1.0/

## Contacto

- Autor: Alex Varela Quirós
- correo: alex.varela@ucr.ac.cr 
- tel: +50685525005

[![iconopeque.jpg](https://i.postimg.cc/hvtdRL0p/iconopeque.jpg)](https://postimg.cc/k6L4xtzb)