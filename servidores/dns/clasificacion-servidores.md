# Clasificación de servidores

## Servidor primario (maestro)

Obtiene la información de sus zonas  <span style="color:#0070C0">de sus archivos locales</span> \.

Todas las modificaciones sobre una zona\, como añadir dominios\, se llevan a cabo en el servidor primario\.

## Servidor secundario (esclavo)

Contiene una  <span style="color:#0070C0">copia</span>  de solo lectura de los archivos de zona del primario

Las zonas siguen disponibles incluso si el servidor primario no está online

![imagen](img/Teoria%20UD03%20Servicio%20DNS%20%28Serveis%20en%20xarxa%2918.png)

![imagen](img/Teoria%20UD03%20Servicio%20DNS%20%28Serveis%20en%20xarxa%2919.png)

## Servidor caché

Solo atiende consultas de los clientes DNS sobre nombres de dominios\.

No contienen ningún tipo de información acerca de la zona y se utiliza para acelerar las consultas\.

Buscará la respuesta a una consulta DNS y recordará la respuesta para la siguiente consulta

Se reduce el ancho de banda y la latencia

![imagen](img/Teoria%20UD03%20Servicio%20DNS%20%28Serveis%20en%20xarxa%2920.png)