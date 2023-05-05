# DHCP

## Introducción

DHCP (Dinamic Host Configuration Protocol) es un servicio basado en el modelo cliente/servidor. SE trata de un protocolo de configuración automática de direcciones.

- Forma parte del protocolo TCP/IP.
- Permite a los ordenadores de una red obtener los parámetros de configuración de red automáticamente.

¿Cómo funciona?

Un servidor posee unos rangos de direcciones IP dinámicas y las va asignando a los clientes.
Sabe en todo momento la IP que posee cada interfaz, por asociación a su dirección MAC (Media Access Control)

## Inconvenientes configuración manual

- En cada equipo se ha de asignar la dirección IP de manera manual
- Al ser manual, pueden asignarse IP incorrectas o no válidas
- Si hay errores, surgirán problemas en la red.
- Lleva mucho trabajo cambiar los equipos de sitio

## Ventajas de la configuración automática

- Las direcciones IP son asignadas por el servidor DHCP automáticamente a cada equipo que la solicite.
- Al automatizar la asignación, estará libre de errores.
- No habrá problemas en la red.
- Los cambios de la estructura de la red se reflejan de manera automática al actualizarse cada cliente.

## Concesiones

Cuando un cliente DHCP recibe de un servidor una IP para que la utilice, se dice que recibe una concesión.

La concesión puede asignarse por tiempo limitado o por tiempo ilimitado.

## Ámbito

Intervalo consecutivo completo de las direcciones IP posibles de una red y su máscara de subred.
Normalmente, los ámbitos definen una subred física de la red a la que se ofrecen los servicios DHCP.

Los ámbitos permiten al servidor administrar la distribución y asignación de direcciones IP, así como los parámetros de configuración relacionados a los clientes de la red.

## Intervalo de exclusión

Secuencia limitada de direcciones IP excluidas del ámbito DHCP.
Aseguran que el servidor no ofrecerá las direcciones de estos intervalos a los clientes DHCP de la red.
Ejemplo:
En el ámbito definido en el punto anterior, deseamos excluir las direcciones de la 195.162.230.150 hasta la 195.162.230.160.

## Conjunto de direcciones

Conjunto formado por las direcciones del ámbito quitando el/los intervalos de exclusión.
En cuanto se asignan las direcciones, se eliminan del conjunto.
Si se liberan, se vuelven a agregar al conjunto
El servidor puede elegir las direcciones del grupo para su asignación dinámica a los clientes DHCP de la red.
Conjunto de direcciones

Ejemplo:

- Ámbito: De 192.168.1.10 hasta 192.168.1.20
- Exclusión: De 192.168.1.15 hasta 192.168.1.17
- IPs asignadas a equipos: 192.168.1.10 y 11
- Conjunto de direcciones: 192.168.1.12,13,14,18,19,20

## Reserva

Dirección IP fija
Perteneciente al intervalo de exclusión
Se asignará de forma estática e indefinida a un dispositivo hardware de la subred por parte del servidor DHCP.
Suelen basarse en parámetros como la MAC del cliente
Las reservas
Aseguran que dicho dispositivo hardware siempre podrá utilizar la misma dirección IP.
Reserva

## Concesión

Periodo de tiempo durante el cual un equipo puede utilizar una IP asignada.

Lo especifica el servidor DHCP (en segundos). 600 = 10 minutos.
Cuando se realiza una concesión a un cliente, la concesión está activa.

### Caducidad de la concesión

- Antes de que caduque, el cliente necesitará renovarla en el servidor.
- La duración de una concesión determina cuándo caducará y la frecuencia con la que el cliente necesita renovarla en el servidor
- La concesión queda inactiva cuando caduca o cuando se elimina del servidor.
- Cuando el servidor comprueba una concesión del cliente, comprueba no solo la duración, sino toda la configuración.
