# Autoconfiguración de red sin DHCP

Es posible que las máquinas en la red puedan autoconfigurarse una dirección IP utilizando el direccionamiento IP privado automático APIPA en el modo sin configuración, cuando **no se dispone de un servidor DHCP** y no se han configurado manualmente los **parámetros IP** de los clientes.

## ¿Para qué se utiliza?

El protocolo APIPA (Automatic Private IP Addressing) es una función de Microsoft Windows que permite a los equipos asignarse automáticamente una dirección IP privada cuando no pueden obtener una dirección IP válida de un servidor DHCP.

## ¿Qué rango de direcciones se utilizan?

El rango de direcciones IP privadas automáticas que se utiliza es 169.254.0.1 a 169.254.255.254, con una máscara de subred de 255.255.0.0. Cuando una máquina no puede obtener una dirección IP del servidor DHCP, el sistema operativo intentará asignar una dirección IP en este rango.

## ¿Puede comunicarse el equipo con otros equipos de la red?

Sin embargo, es importante tener en cuenta que el uso de APIPA solo permite la comunicación con otros equipos que también estén utilizando APIPA en la misma red. No permite la conexión a Internet o a redes externas