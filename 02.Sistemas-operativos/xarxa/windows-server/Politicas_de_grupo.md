# Políticas de grupo (GPO)

La política de grupo es un mecanismo para controlar e implementar la configuración del sistema operativo en las computadoras en toda su red.

Consiste en la configuración de usuario y computadora para los diversos sistemas operativos de Microsoft Windows, que los sistemas implementan durante el inicio y apagado de la computadora y el inicio y cierre de sesión del usuario.

## Vinculación

Se pueden configurar uno o más objetos de directiva de grupo (GPO) y luego usar un proceso llamado ``vinculación`` para asociarlos con objetos específicos de servicios de dominio de Active Directory (AD DS).

Cuando se vincula un GPO a un objeto contenedor, todos los objetos en ese contenedor reciben las configuraciones que configuró en el GPO.

Puede vincular varios GPO a un solo contenedor de AD DS o vincular un GPO a múltiples contenedores a lo largo de la jerarquía de AD DS.
