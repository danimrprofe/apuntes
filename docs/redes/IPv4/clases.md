# Sistema con clases (direccionamiento classful)

## Problemática

Al comienzo de Internet, una dirección IP constaba de 8 bits para identificar una red particular a la que estaba conectado un host y 24 bits restantes para identificar el host dentro de esa red. Esto fue suficiente en ese momento debido a la escasa cantidad de redes grandes. Sin embargo, con la amplia proliferación de redes locales (LAN), el formato de dirección IP se vio limitado, ya que solo admite un máximo de 254 redes independientes.

## Sistema de clases

Surgió la necesidad de un formato más flexible, por lo que se introdujo el sistema de clases de direcciones IP.
En el sistema con clases, las direcciones IP se dividen en tres clases: Clase A, Clase B y Clase C.

Cada clase se define por el rango de valores del primer octeto de la dirección IP.

La clase A se identifica por un primer octeto entre 1 y 126, la clase B entre 128 y 191 y la clase C entre 192 y 223.

Cada clase define una cantidad diferente de bits para la identificación de la red y para la identificación del host.

## Evolución hacia CIDR

El sistema con clases se ha superado con el sistema de direccionamiento CIDR (Classless Inter-Domain Routing), que permite una mayor flexibilidad en la asignación de direcciones IP.
