# Proceso de asignación de IP a un cliente

## Funcionamiento general

El protocolo DHCP define un conjunto de mensajes que se intercambian el cliente y el servidor DHCP para que el primero consiga una configuración de red sin intervención humana.
El servidor DHCP escucha en el puerto 67 (UDP). El cliente DHCP, a través del puerto 68 (UDP), envía mensajes para que algún servidor DHCP activo le conteste
Cada red debe tener un servidor DHCP configurado y activo, que almacena tablas con las direcciones IP.
El cliente recibe ofertas, elige una, y lo comunica a todos los servidores (difusión). El servidor elegido le contesta con un mensaje que incluye:

## En el estado inicial

El cliente envía una trama de difusión con el mensaje **DHCPDISCOVER** a la red para detectar los servidores DHCP activos. Esta trama lleva incluida la **MAC** física de origen de la interfaz de red.

## En el estado de inicialización

Los servidores activos responden al cliente con un mensaje **DHCPOFFER**
Incluye una oferta de configuración.
Cliente puede recibir más de un mensaje DHCPOFFER (diferentes servidores disponibles)
Durante el estado de selección
Se analizan las diferentes ofertas recibidas
Se elige la primera que se haya recibido y que resulte válida.

## En el estado de solicitud

El cliente envía otra trama de difusión con un mensaje DHCPREQUEST que notifica la identidad del servidor seleccionado.
De este modo, se descartan los demás ofrecimientos recibidos.

El servidor DHCP implicado recibe el **DHCPREQUEST** del cliente
Registra la asignación
Envía un mensaje DHCPACK al cliente que incluye los parámetros de la configuración asignada junto con la dirección IP.

### En el estado de enlace:

El cliente recibe el mensaje **DHCPACK**
Ejecuta la orden ARP con la IP asignada para comprobar que no está duplicada.
A partir de este momento, el cliente está configurado.
