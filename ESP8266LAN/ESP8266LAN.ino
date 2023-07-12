#include <ESP8266WiFi.h> // Incluir la biblioteca ESP8266WiFi para utilizar las funciones relacionadas con WiFi

const char *ssid = "ESTACION-IoT";  // Nombre de la red WiFi
const char *password = "998877665"; // Contraseña de la red WiFi

void setup()
{
  WiFi.mode(WIFI_AP);               // Configurar el modo de WiFi como Punto de Acceso (Access Point)
  WiFi.softAP(ssid, password);      // Configurar el ESP8266 como un Punto de Acceso WiFi con el nombre de red y contraseña especificados
  IPAddress myIP = WiFi.softAPIP(); // Obtener la dirección IP asignada al Punto de Acceso
}

void loop()
{
  // Código adicional o lógica para interactuar con clientes o realizar tareas específicas pueden ser colocadas aquí
}
