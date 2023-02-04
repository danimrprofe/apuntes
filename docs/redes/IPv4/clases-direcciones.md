# Clases de direcciones

- Una red con clase (classful) es una arquitectura de direccionamiento de red utilizada en Internet desde 1981
- A partir de 1993 se introduce el enrutamiento entre dominios sin clase en 1993 (CIDR)

## ¿Cómo se divide el espacio de direcciones?

- En IPv4 se divide en cinco clases de direcciones.
- Clases basadas en los 4 primeros bits de dirección.
- Clases A, B y C proporcionan direcciones de unidifusión para redes de tres tamaños de red diferentes.

 La clase D es utilizada para redes de multidifusión, donde se envía información a un grupo de dispositivos en la red simultáneamente. El rango de direcciones de clase E (240.0.0.0 a 255.255.255.255) está reservado para fines futuros o experimentales y no es asignado para uso general.

## CLASE A

- El primer bit es un 0, así quedarán 7 bits - para definir la red.
- Empiezan por un valor entre 00000000 y - 01111111.
- Es decir 0 y 127
- 0 y el 127 reservados (entre 1 y 126 en realidad).
- La red 127.0.0.1 es para loopback.

![imagen](2019-05-08-08-43-36.png)

## CLASE B

- 2 primeros bits de la red son 10, quedando 6+8=14 bits para definir las redes.
- IP de clase B empezarán por un valor entre 10000000 y 10111111
- Direcciones que comienzan entre 128 y 191.

![imagen](2019-05-08-08-43-44.png)

## CLASE C

- 3 primeros bits de la red son 110, quedando 5+8+8=21 bits para definir las redes.
- Empezarán por un valor entre 11000000 y 11011111
- Entre 192 y 223.