## Nivel de transporte

### Funciones a nivel de capa de transporte**

#### Segmentación y reensamblado

#### Multiplexado de conexiones

    15. Multiplexación ascendente
        6.  Permite compartir un único circuito virtual para
            varias transmisiones
    16. Multiplexación descendente
    17. Conexiones orientadas a conexión
        7.  Establece un circuito virtual a través de la red
            entre emisor y receptor
        8.  Todos los paquetes son enviados por este circuito
            virtual
        9.  Pasos
            1.  Establecer conexión: solicitud, confirmación
                conexión, ACK confirmació
            2.  Transferencia de datos
            3.  Liberar conexión

#### Entrega fiable

        10. Control de errores
        11. Control de secuencia
        12. Control de pérdidas
        13. Control de duplicidades

#### Reconstrucción ordenada de datos

        1.  Los paquetes se pueden recibir en un orden diferente
        2.  Se tienen que reordenar y recomponer para recuperar
            los datos
#### Control de flujo

- Stop and wait
- Ventana deslizante

### Protocolos de capa de transporte

#### TCP

##### Características

- Orientado a conexión
- Garantiza fiabilidad de transmisión utilizando números de secuencia y checksum
- Proporciona control de flujo para garantizar que un host no se colapsa con más datos que el buffer puede soportar

##### Segmentos TCP

1.  Puerto origen y destino (16 bit)
2.  Número de secuencia y número de acuse de recibo)
3.  Medida de la ventana
4.  Checksum
5.  Bits de control (SYN, ACK, FIN)
6.  Datos

    1.  Establecimiento de conexión
    2.  Acuse de recepción. Ventanas
    3.  Retransmisión
    4.  Control de congestión y flujo

#### UDP

- No orientado a conexión, transmisión rápida, pero sin fiabilidad.
- No ofrece ninguna garantía, ni proporciona métodos de detección de errores

Segmento UDP:

- Puertos origen y destino
- Longitud
- Checksum (opcional)
- Datos

#### Puertos

Según la numeración de los puertos se hace la siguiente
clasificación para los protocolos TCP y UDP:

- Los puertos inferiores a 1.024 están reservados para servicios muy definidos, como telnet, SMTP, P0P3
- Estas asignaciones son fijas y no pueden ser utilizadas por otros servidos.
- A menudo estos puertos son llamados «puertos bien conocidos».

##### Puertos registrados

- Los puertos entre 1024 y 49151 Son puertos registrados.
- IANA intenta ordenar el uso de este rango, pero sin las restricciones que
existen para los puertos bien conocidos.

##### Puertos privados

- Puertos numerados entre 49152 y 65535
- Son puertos privados de los que se puede disponer para cualquier uso.

#### Sockets
