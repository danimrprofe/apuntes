# Interfaces loopback

## ¿Qué es el loopback?

Se trata de una interfaz de red `virtual`, con las siguientes características:

- Siempre está activa.
- No está asociada a ningún componente hardware real (tarjeta de red).
- No conectada a ninguna red real.
- Implementada mediante software dentro del sistema operativo.

## Utilización

- Usada para emular tráfico de red entre 2 procesos del mismo host.
- Se suele utilizar para hacer pruebas.
- Tráfico enviado a la IP de `loopback` se pasa como si fuera recibida desde otro dispositivo.
- Dirección habitual: `127.0.0.1` (IPv4) o `::1` (IPv6).
- Nombre de host `localhost`
