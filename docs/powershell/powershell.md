# Powershell

PowerShell es un **lenguaje de scripting** de Microsoft que se ejecuta en la línea de comandos. Fue inventado por Jeffrey Snover en 2006 con el fin de ofrecer una herramienta de línea de comandos de alto nivel que sea fácil de usar y tenga una sintaxis intuitiva.

El objetivo principal de PowerShell es proporcionar un entorno de scripting con el que los usuarios puedan automatizar tareas administrativas y mejorar la productividad. Esto se logra mediante la creación de comandos específicos para realizar tareas específicas, así como la creación de **scripts** más largos para realizar una variedad de tareas

## Conexión remota

El servicio de administración remota de Windows WinRM está
habilitada por defecto.

Para crear una sesión remota de powershell:

    new-pssession -computername rtmsvrd

Una vez creada la sesión, para conectar a ella se utiliza:

    Enter-PsSession 3 (identificador de sesión)

## Configuración de red

Para conocer los adaptadores de red

```poweshell
Get-netadapter
```

Configurar una interfaz

new-netipaddress -interfaceindex 6 -ipaddress 192.168.0.200
-prefixlength 24 -defaultgateway 192.168.0.1

Configurar direcciones DNS

Set-dnsclientserveraddress -interfaceindex 6 –serveraddresses
("192.168.0.1","192.168.0.2")

