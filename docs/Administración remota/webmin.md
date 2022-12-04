## Webmim

Webmin es una herramienta de administración de servidor basada en web. Es una de las herramientas más populares para la administración de servidores Linux. Este tutorial cubrirá los conceptos básicos de Webmin y le mostrará cómo puede configurar y administrar un servidor Linux con Webmin.

1. Instalación de Webmin: la primera etapa para usar Webmin es instalarlo en el servidor. Para ello, descargue el paquete Webmin desde el sitio oficial. Luego, ejecute el instalador y siga las instrucciones para completar la instalación.

2. Acceso a Webmin: Webmin se ejecuta en el puerto 10000 por defecto. Para acceder a la interfaz de administración de Webmin, abra un navegador web y vaya a la dirección 
```
https://<servidor-ip>:10000.
```
1. Configuración de usuarios y grupos: una vez dentro de Webmin, se le pedirá que inicie sesión con un nombre de usuario y una contraseña. Esto le permitirá acceder a la sección de configuración de usuarios y grupos. Aquí, podrás agregar, editar y eliminar usuarios del sistema.

2. Configuración de los servicios: en la sección de servicios, puedes configurar los servicios que se están ejecutando en el servidor. Por ejemplo, puedes configurar un servidor web, un servidor de correo electrónico, un servidor DNS, etc.

3. Configuración de los paquetes: la sección de paquetes le permite instalar y desinstalar paquetes de software en el servidor. Esta es una excelente manera de mantener el servidor actualizado y libre de vulnerabilidades.

4. Configuración de Firewall: la sección de firewall le permite configurar reglas de firewall para el servidor. Esto le ayudará a mantener su servidor seguro.


## Acceso
-----
Es necesario acceder desde un host autorizado y HTTPS


Permitir y prohibir accesos
---------------------------
Editar fichero /etc/webmin/stop
Lineas allow y deny

Parar servicio: sudo /etc/webmin/stop
Arrancar servicio: sudo /etc/webmin/start