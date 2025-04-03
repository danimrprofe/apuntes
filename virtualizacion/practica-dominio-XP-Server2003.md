2. Crear la máquina virtual de Windows XP
Paso 1: Configurar la máquina virtual
Abre VirtualBox y haz clic en "Nueva"
Nombre: Windows XP
Tipo: Microsoft Windows
Versión: Windows XP (32-bit)
Memoria RAM: 512 MB - 1 GB (según lo que quieras probar).
Disco duro: Crear uno nuevo (VDI, tamaño fijo, 10-20 GB).
Paso 2: Configurar almacenamiento y arranque
En la configuración de la máquina, ve a "Almacenamiento".
Selecciona el Controlador IDE y carga la ISO de Windows XP.
Paso 3: Instalación de Windows XP
Inicia la máquina y arranca desde la ISO.
Sigue los pasos del instalador de Windows XP.
Formatea el disco en NTFS.
Completa la instalación y configura usuario/contraseña.


Windows XP SP3: M8DPF-XT324-YBKK9-3VF8C-M2X78
Paso 4: Instalar VirtualBox Guest Additions (Opcional)
Ve a Dispositivos > Insertar imagen de Guest Additions.
Instala los controladores para mejorar el rendimiento.
3. Crear la máquina virtual de Windows Server 2003
Paso 1: Configurar la máquina virtual
En VirtualBox, haz clic en "Nueva".


Nombre: Windows Server 2003


Tipo: Microsoft Windows


Versión: Windows 2003 (32-bit)


Memoria RAM: 1 GB o más.


Disco duro: 10-30 GB (según uso).


Paso 2: Configurar almacenamiento y red
En "Almacenamiento", carga la ISO de Windows Server 2003 en el Controlador IDE.


En "Red", usa el modo Red Interna si quieres conectar ambas máquinas entre sí.


Paso 3: Instalación de Windows Server 2003
Arranca la máquina e inicia la instalación desde la ISO.
Sigue los pasos del instalador y selecciona NTFS como sistema de archivos.
Configura una contraseña para el administrador.
Configura el Rol de Servidor (si quieres probar DHCP, DNS, Active Directory, etc.).


Windows Server 2003 Standard x64 Edition VWMD9-2Q897-F427R-TV2KY-CRF2B
Datos:
administrator password: 123456
COMPUTER NAME: SERVIDOR
Zona horaria: +1
Tras reiniciar  la máquina virtual del servidor, iniciamos sesión:

Para pulsar Ctrl+alt+supr en la máquina virtual clic derecho en el icono de la flecha y:

Iniciamos sesión como administrador:

1. Configuración de red en VirtualBox
Antes de configurar las direcciones IP dentro de los sistemas operativos, debemos asegurarnos de que ambos usen la misma red interna en VirtualBox.
Paso 1: Configurar adaptadores de red en VirtualBox
En VirtualBox, ve a Configuración > Red en cada máquina virtual.


En el Adaptador 1, selecciona Red Interna y nómbrala (ejemplo: "RedXP2003").


Asegúrate de hacer esto en ambas máquinas.



2. Configurar Windows Server 2003 (Servidor - IP Fija)
Dado que actuará como servidor de red, asignaremos una IP fija.
Paso 2: Asignar IP en Windows Server 2003
Abre el Panel de Control > Conexiones de red.


Haz clic derecho en Conexión de área local > Propiedades.


Selecciona Protocolo de Internet (TCP/IP) > Propiedades.


Configura la siguiente IP:


Dirección IP: 192.168.1.1


Máscara de subred: 255.255.255.0


Puerta de enlace predeterminada: (Vacío o misma IP del servidor si hay NAT)


Servidor DNS preferido: 192.168.1.1 (o una IP de Google como 8.8.8.8)


Guarda los cambios y cierra.



3. Configurar Windows XP (Cliente - IP Manual o Automática)
Windows XP puede recibir una IP por DHCP desde el servidor o configurarse manualmente.
Opción 1: Configurar IP manualmente en XP
Ve a Panel de Control > Conexiones de red.


Clic derecho en Conexión de área local > Propiedades.


Selecciona Protocolo de Internet (TCP/IP) > Propiedades.


Configura:


Dirección IP: 192.168.1.2


Máscara de subred: 255.255.255.0


Puerta de enlace: 192.168.1.1


DNS preferido: 192.168.1.1


Guarda los cambios y prueba la conexión (ver paso 4).



4. Probar la conexión entre ambas máquinas
Después de configurar las IPs, verifica que pueden comunicarse:
Paso 4: Probar conectividad con ping
En Windows XP, abre Símbolo del sistema (cmd).


Escribe:

 bash
CopiarEditar
ping 192.168.1.1
 Si responde, la conexión es correcta.


En Windows Server 2003, prueba:

 bash
CopiarEditar
ping 192.168.1.2
 Si hay respuesta, ambas máquinas están conectadas correctamente.




Tarea: Configuración de Dominio en Windows Server 2003 y Gestión de Usuarios y Recursos
Objetivo: Configurar un dominio en Windows Server 2003, unir un equipo con Windows XP y gestionar usuarios, grupos y recursos compartidos en la red.

Parte 1: Configuración del Controlador de Dominio en Windows Server 2003
Instalar Active Directory:


Abre Ejecutar (Win + R), escribe dcpromo y presiona Enter.
Selecciona "Controlador de dominio para un nuevo dominio".
Elige "Dominio en un nuevo bosque".
Introduce un nombre de dominio (ejemplo: midominio.local).
Configura una contraseña segura para el administrador de Active Directory.
Completa la instalación y reinicia el servidor.


Configurar DNS y DHCP (Opcional, si la red lo necesita).


Parte 2: Unión del Cliente Windows XP al Dominio
En Windows XP, asigna una IP estática en la misma subred del servidor y usa la IP del servidor como DNS principal.


Unir al dominio:


Ve a Mi PC > Propiedades > Nombre de equipo > Cambiar.
Selecciona Dominio, introduce el nombre (midominio.local) y presiona Aceptar.
Introduce las credenciales del administrador del dominio cuando se soliciten.
Reinicia el equipo.


Parte 3: Creación y Gestión de Usuarios y Grupos
Paso 5: Crear un usuario en Active Directory:
En el servidor, abre Usuarios y Equipos de Active Directory (dsa.msc).
Dentro del dominio, haz clic derecho en Usuarios > Nuevo > Usuario.
Crea el usuario Juan Pérez con nombre de usuario jperez.
Asigna una contraseña y marca "El usuario debe cambiar la contraseña en el próximo inicio de sesión".

Contraseña provisional: !1234567a, y marcamos que el usuario debe cambiar la contraseña en el primer inicio de sesión.

Ahora ya tendremos el usuario creado:

Paso 6. Crear un grupo y agregar usuarios:
Dentro de Active Directory, ve a Usuarios > Nuevo > Grupo.
Llama al grupo Profesores.

Abre las propiedades del grupo Alumnos  haciendo doble click en el nombre del grupo y añade el usuario jperez. Vamos a add:

Escribimos parte del nombre de usuario y le damos a check names:

Nos aparecerá el usuario y le damos a OK:

Ahora el grupo Alumnos tiene un miembro, el usuario jperez.

Parte 4: Creación y Configuración de Recursos Compartidos
Crear una unidad de red compartida:


En el servidor, crea una carpeta en C:\Recursos_Alumnos.



Haz clic derecho > Propiedades > Compartir.
Activa la opción "Compartir esta carpeta" y nómbrala Alumnos.

Ve a la pestaña Seguridad y otorga permisos de lectura/escritura sólo al grupo Ventas.









El grupo Users, que es más amplio, tiene permisos para acceder a esta carpeta, por lo que se los vamos a quitar:



Conectar la unidad de red en Windows XP:
En el cliente, abre Mi PC > Herramientas > Conectar a unidad de red.
Escribe la ruta \\Servidor\Ventas y selecciona una letra (ejemplo: Z:).
Introduce las credenciales del dominio si lo solicita.
Asegura que el usuario pueda acceder y escribir en la carpeta.


Parte 5: Pruebas y Verificación
✅ El usuario jperez puede iniciar sesión en el dominio desde Windows XP.
 ✅ El usuario jperez tiene acceso a la unidad de red Ventas.
 ✅ El usuario puede crear y modificar archivos en la carpeta compartida.
 ✅ Los permisos de grupo se aplican correctamente.

Extras (Opcional, si hay más tiempo)
🔹 Configurar una política de grupo (GPO) para asignar automáticamente la unidad de red.
 🔹 Crear más usuarios y probar diferentes niveles de acceso.
Extra: Asignación Automática de Unidad de Red con una GPO
Objetivo: Configurar una Política de Grupo (GPO) en Windows Server 2003 para asignar automáticamente la unidad de red Ventas (Z:) a los usuarios del grupo Ventas.

1. Crear y Configurar la GPO
Abrir el Editor de Políticas de Grupo:


En el servidor, abre Ejecutar (Win + R), escribe gpedit.msc y presiona Enter.
Alternativamente, abre Usuarios y Equipos de Active Directory (dsa.msc), haz clic derecho en el dominio (midominio.local) y selecciona Propiedades > Directiva de Grupo.


Crear una nueva GPO:


En la ventana Directiva de Grupo, haz clic derecho en el dominio y selecciona "Nueva directiva de grupo".
Nómbrala Asignación Unidad Ventas.


Editar la GPO:


Haz clic derecho sobre Asignación Unidad Ventas y selecciona Editar.


Ve a: Configuración de usuario > Preferencias > Configuración de Windows > Asignaciones de unidad
Haz clic derecho en Asignaciones de unidad > Nuevo > Unidad de red.


Configurar la Unidad de Red:


En Ubicación, escribe la ruta del recurso compartido:

 CopiarEditar
\\Servidor\Ventas


En Letra de unidad, selecciona Z:.


Marca la opción "Reconectar" para que la unidad se vuelva a mapear en cada inicio de sesión.


Filtrar la GPO para el grupo "Ventas":


Ve a la pestaña Ámbito.


En Seguridad, haz clic en Agregar > Usuarios o grupos.


Escribe Ventas, selecciona el grupo y presiona Aceptar.


Asegúrate de que Ventas tiene activadas las opciones "Leer" y "Aplicar esta directiva de grupo".



2. Aplicar la GPO y Verificar
Actualizar las Políticas en Windows XP:


En el cliente Windows XP, abre Símbolo del sistema (cmd) y ejecuta:

 bash
CopiarEditar
gpupdate /force


Reinicia el equipo.


Iniciar sesión con un usuario del grupo Ventas y comprobar:


Abre Mi PC y verifica si aparece la unidad Z: conectada automáticamente.


Intenta crear y modificar archivos en la carpeta para verificar permisos.



Resultado Esperado:
✅ Los usuarios del grupo Ventas tendrán la unidad Z: asignada automáticamente al iniciar sesión.
 ✅ La configuración se aplicará sin necesidad de que los usuarios la configuren manualmente.

Extras (Opcionales)
🔹 Aplicar la GPO solo a ciertos equipos dentro del dominio.
 🔹 Configurar una GPO de Inicio de Sesión con un script net use Z: \\Servidor\Ventas.
 🔹 Usar gpresult /R en Windows XP para verificar si la GPO se aplica correctamente.
Este método ayuda a automatizar la administración de recursos en un dominio de Windows Server 2003. 🚀

