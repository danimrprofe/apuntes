# Comando nslookup

```
nslookup www.google.com
Servidor:  server-ies1.iesramonllull.local
Address:  10.216.22.4

Respuesta no autoritativa:
Nombre:  www.google.com
Addresses:  2a00:1450:4003:811::2004
          216.58.209.68
```

## Análisis

El resultado de la consulta nslookup **www.google.com** muestra la siguiente información:

**Servidor DNS utilizado**

El servidor DNS utilizado para la consulta es **server-ies1.iesramonllull.local** con la dirección IP **10.216.22.4**. Esto indica el servidor DNS desde el cual se realizó la consulta.

**Respuesta no autoritativa**

La línea "Respuesta no autoritativa" significa que la respuesta proviene de un servidor DNS que no es la fuente autorizada para el dominio consultado. En este caso, el servidor DNS utilizado no es el servidor autoritativo para el dominio "google.com", sino un servidor local de la red "iesramonllull.local".

**Nombre**

El nombre de dominio consultado es "www.google.com".

**Direcciones**

Se muestran las direcciones IP asociadas al nombre de dominio. En este caso, se obtuvieron dos direcciones IP:

- 2a00:1450:4003:811::2004: Es una dirección IPv6 asociada a "www.google.com".
- 216.58.209.68: Es una dirección IPv4 asociada a "www.google.com".

Estos resultados indican que "www.google.com" tiene tanto una dirección IPv6 como una dirección IPv4, lo que significa que el dominio es accesible tanto a través de IPv6 como de IPv4.

# Powershell

En PowerShell, puedes utilizar el cmdlet Resolve-DnsName como alternativa a nslookup. Resolve-DnsName proporciona funcionalidades similares y te permite realizar consultas de DNS desde PowerShell.

Analicemos una petición:

```
PS Z:\> Resolve-DnsName www.google.com

Name                                           Type   TTL   Section    IPAddress
----                                           ----   ---   -------    ---------
www.google.com                                 AAAA   90    Answer     2a00:1450:4003:80f::2004
www.google.com                                 A      56    Answer     142.250.184.164
```