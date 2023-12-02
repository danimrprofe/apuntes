# Nivel de red

## Funciones

### Encaminamiento

    1.  Para pasar datos entre hosts hay que definir un
        mecanismo de encaminamiento
    2.  Seleccionar el encaminador siguiente óptimo
    3.  Encaminadores mueven paquetes entre las redes a las que
        están conectados

### Direccionamiento

    1.  Se necesita identificar de manera única los ordenadores
    2.  Definir un sistema de agrupación para facilitar la tarea
        de encamiento
    3.  En IP se utilizan las direcciones IP (jerarquizadas,
        clases, subredes, máscaras, etc.) facilita la gestión
        del encaminamiento

#### Orientación a conexión

##### Sin conexión (conmutación de paquetes)

- No se establece ningún camino concreto
- Cada vez que se envía un paquete se decide el camino que seguirá

##### Circuito virtual (conmutación de circuitos)

- Se establece inicialmente un camino entre dos equipos
- Se reservan recursos
- Equivalente a pasar un cable dedicado extremo a extremo

### Protocolos

#### IP

            1.  IPv4 y IPv6

#### ICMP

- Control y notificación de errores. Complementario al protocol IP
- Utilizado en aplicaciones como ping o traceroute (diagnóstico de red)

#### ARP y RARP

            1.  Protocolo de resolución de dirección de capa de enlace

#### Asignación de direcciones

- Estática
- Dinámica (DHCP)
