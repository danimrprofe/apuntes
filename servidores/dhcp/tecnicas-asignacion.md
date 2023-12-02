# Técnicas de asignación de IP

## Tipos de asignaciones

Tipo de asignación DHCP es el mecanismo por el cual un servidor DHCP decide:

- La IP que tiene que entregar a un cliente
- Durante cuánto tiempo concede una licencia o autorización al cliente para que use esa IP.
La IP que asigna el servidor al cliente
- Puede ser elegida dentro de un conjunto posible de direcciones IP
- Puede ser obligatoriamente una IP concreta.

El protocolo DHCP establece la posibilidad de utilizar en los servidores DHCP tres técnicas de asignación DHCP.

## Asignación automática

Se cede una IP libre con los demás valores a un cliente la primera vez que lo solicita
Se mantendrá hasta que el cliente la libere.
Suele utilizarse este procedimiento cuando el número de clientes no varía demasiado.

## Asignación dinámica

Se cede una dirección IP libre de manera temporal
El plazo de cesión varía según la frecuencia de altas y bajas de clientes, así como de la cantidad de direcciones disponibles.
Es el sistema habitual entre los ISP

## Asignación estática con reserva

La asignación estática con reserva es un modo de configuración que se asemeja al manual, en el que se asigna una dirección IP específica a un ordenador en particular. Esta configuración se utiliza para evitar la conexión de clientes no autorizados, controlando de forma estricta la asignación de direcciones IP.
