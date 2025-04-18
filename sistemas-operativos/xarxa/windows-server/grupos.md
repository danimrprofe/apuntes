# Grupos

## Pertenencia a grupos y grupos anidados

Los usuarios pueden pertenecer a más de un grupo de Active Directory. Estos grupos pueden contener otros objetos, como ordenadores, otros grupos, etc.

El agrupamiento **anidado** describe el proceso de configurar uno o más grupos como miembros de otro grupo, permitiendo así la creación de grupos anidados. Esto se logra mediante la asignación de los grupos existentes como miembros de un grupo, lo que les permite heredar los permisos asignados al padre.

## Ejemplo de agrupamiento anidado

Un ejemplo de agrupamiento anidado es considerar una empresa con **dos grupos**: marketing y diseño gráfico. Los miembros del grupo de diseño gráfico tienen acceso a una **impresora láser color** de alta resolución.

Para que los miembros del grupo de marketing también tengan acceso a la impresora, se agrega el grupo de marketing como miembro del grupo de diseño gráfico. De esta forma, los miembros del grupo de marketing tendrán el mismo permiso para la impresora láser color como los miembros del grupo de diseño gráfico.

## Tipos de grupos

Hay dos clasificaciones de grupo en Windows Server:

- Tipo de grupo
- Ámbito de grupo.

El tipo de grupo define cómo se usa un grupo dentro de Active Directory.

Los dos tipos de grupos de Windows Server 2012 R2 son los siguientes:

- ``Grupos de distribución``: grupos no relacionados con la seguridad creados para la distribución de Información a una o más personas.
- ``Grupos de seguridad``: grupos relacionados con la seguridad creados para otorgar permisos de acceso a recursos a múltiples usuarios

### Grupos de distribución

Las aplicaciones compatibles con Active Directory pueden usar grupos de distribución para funciones no relacionadas con la seguridad.

Por ejemplo, Microsoft Exchange usa grupos de distribución para enviar mensajes a múltiples usuarios.

### Grupos de seguridad

Los grupos que utiliza para asignar permisos a los recursos se denominan grupos de seguridad.

Los administradores hacen que los usuarios que necesitan acceso a los mismos recursos sean miembros de un grupo de seguridad.

Luego otorgan permiso al grupo de seguridad para acceder al recurso.
