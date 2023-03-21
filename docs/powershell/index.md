[🔙 Enrere](../) | [🏠 Pàgina principal](http://danimrprofe.github.io/apuntes/)

# Powershell

PowerShell es un **lenguaje de scripting** de Microsoft que se ejecuta en la línea de comandos. Fue inventado por Jeffrey Snover en 2006 con el fin de ofrecer una herramienta de línea de comandos de alto nivel que sea fácil de usar y tenga una sintaxis intuitiva.

El objetivo principal de PowerShell es proporcionar un entorno de scripting con el que los usuarios puedan automatizar tareas administrativas y mejorar la productividad. Esto se logra mediante la creación de comandos específicos para realizar tareas específicas, así como la creación de **scripts** más largos para realizar una variedad de tareas

## Conexión remota

El servicio de administración remota de Windows WinRM está
habilitada por defecto.

Para crear una sesión remota de powershell:

```ps
new-pssession -computername rtmsvrd
```

Una vez creada la sesión, para conectar a ella se utiliza:

```ps
Enter-PsSession 3 (identificador de sesión)
```

## Configuración de red

Para conocer los adaptadores de red

```ps
Get-netadapter
```

```
Name                      InterfaceDescription                    ifIndex Status       MacAddress             LinkSpeed
----                      --------------------                    ------- ------       ----------             ---------
VirtualBox Host-Only N... VirtualBox Host-Only Ethernet Adapter        12 Up           0A-00-27-00-00-0C         1 Gbps
Ethernet                  Intel(R) Ethernet Connection (12) I2...       4 Up           2C-F0-5D-E5-5F-B3         1 Gbps
```

## Configurar una interfaz

Este código es un comando de PowerShell que se usa para crear una nueva dirección IP, asignar una máscara de subred, y establecer una puerta de enlace predeterminada.

```ps
new-netipaddress -interfaceindex 6 -ipaddress 192.168.0.200
-prefixlength 24 -defaultgateway 192.168.0.1
```

## Configurar direcciones DNS

Este código establece la dirección del servidor DNS para la interfaz de red con índice 6. Establece las direcciones del servidor DNS en "192.168.0.1" y "192.168.0.2". Esto le permite al dispositivo enviar solicitudes DNS a estos servidores específicos.

```ps
Set-dnsclientserveraddress -interfaceindex 6 –serveraddresses
("192.168.0.1","192.168.0.2")
```

## Quitar espacios en nombres de carpetas y archivos

Este código usa los cmdlets de PowerShell para buscar dentro de todos los directorios y subdirectorios de la ubicación actual (-Recurse) y busca cualquier nombre de archivo que contenga un espacio.

Estos archivos se guardan en una variable y luego se renombran con el comando Rename-Item. El espacio se reemplazará con un guión bajo (-replace).

```ps
Get-ChildItem . -Recurse | Where-Object { $_.Name.Contains(' ') } | Rename-Item -NewName { $_.Name -replace ' ', '_' }
```