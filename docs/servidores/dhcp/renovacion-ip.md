# Proceso de renovación de IP a un cliente

## Durante el estado de renovación

El cliente, antes de que venza el periodo de cesión – por lo general, cuando haya pasado el 50% del tiempo previsto-
Envía un mensaje DHCPRENEW al servidor
Solicita una ampliación del plazo así como el mantenimiento de los valores asignados.
Se inicia el estado de reenlace
Cuando el cliente se dispone a dejar la IP asignada
Se lo comunica al servidor mediante un mensaje DHCPRELEASE para que conste que desde ese momento queda liberada para cualquier otro dispositivo que la necesite.

## Renovación de IP (Temporizadores)

Lease time (LT) = 86.400 (24 horas)
T1 = 50% de 24 h = 12 h
T2 = 87,5% de 24 h = 21 h
Renewal time (T1)
Al 50% del tiempo (T1) se pedirá renovación se intentará renovar con el servidor DHCP que nos dio la IP
Ocurrirá a las 12 horas (quedando otras 12 horas)
Rebind time (T2)
Si no se obtuvo respuesta a la renovación
Al 87,5% del tiempo (T2) se intentará volver a enlazar con algún servidor enviando un mensaje de broadcast
A las 21 horas (quedando 3 horas)
Autoconfiguración (APIPA)
Autoconfiguración de red sin DHCP