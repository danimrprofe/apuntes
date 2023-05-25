# Loopback en IPv6

El dispositivo loopback es una interfaz de red virtual que hace referencia a nuestra propia máquina. El nombre reservado es el de localhost.

## IPv4

En el caso de IPv4, para el dispositivo loopback suele utilizar la dirección 127.0.0.1 , aunque realmante se pueden utilizar cualquier 127.X.X.X con idéntico resultado.

## IPv6

En el caso de IPv6 la dirección loopback es ::1 (se pueden comprimir las direcciones en IPv6). Podemos por ejemplo hacer un ping a la interfaz loopback:

```ps
C:\Users\XXXX>ping ::1

Pinging ::1 with 32 bytes of data:
Reply from ::1: time<1ms
Reply from ::1: time<1ms
Reply from ::1: time<1ms
Reply from ::1: time<1ms

Ping statistics for ::1:
Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
Minimum = 0ms, Maximum = 0ms, Average = 0ms
```

Si en lugar de especificar la dirección IP, hacemos ping al nombre loopback, se buscará en primer lugar la IP que le corresponde. Podemos en ping especificar qué protocolo vamos a usar, mediante los argumentos -4 (para IPv4) y -6 (para IPv6).

```ps
C:\Users\XXXX>ping -4 localhost

Pinging DESKTOP-2XXXXXU [127.0.0.1] with 32 bytes of data:
Reply from 127.0.0.1: bytes=32 time<1ms TTL=128
Reply from 127.0.0.1: bytes=32 time<1ms TTL=128
Reply from 127.0.0.1: bytes=32 time<1ms TTL=128
Reply from 127.0.0.1: bytes=32 time<1ms TTL=128

Ping statistics for 127.0.0.1:
 Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
 Minimum = 0ms, Maximum = 0ms, Average = 0ms
```

Para hacer ping con IPv6:

```ps
C:\Users\XXXX>ping -6 localhost

Pinging DESKTOP-2XXXXXU [::1] with 32 bytes of data:
Reply from ::1: time<1ms
Reply from ::1: time<1ms
Reply from ::1: time<1ms
Reply from ::1: time<1ms

Ping statistics for ::1:
 Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
Approximate round trip times in milli-seconds:
 Minimum = 0ms, Maximum = 0ms, Average = 0ms
```


Para acceder en el navegador al servidor http local, en el caso de IPv6 tendremos que escribir la dirección IP ente brackets:

http://[::1]