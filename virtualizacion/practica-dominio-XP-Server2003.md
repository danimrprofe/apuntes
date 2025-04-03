- [Configuración de un dominio de Windows con Virtualbox](#configuración-de-un-dominio-de-windows-con-virtualbox)
  - [1. Crear la máquina virtual de Windows XP](#1-crear-la-máquina-virtual-de-windows-xp)
    - [1.1. Configurar la máquina virtual](#11-configurar-la-máquina-virtual)
    - [1.2: Configurar almacenamiento y arranque](#12-configurar-almacenamiento-y-arranque)
    - [1.3. Instalación de Windows XP](#13-instalación-de-windows-xp)
    - [1.4. Instalar VirtualBox Guest Additions (Opcional)](#14-instalar-virtualbox-guest-additions-opcional)
  - [2. Crear la máquina virtual de Windows Server 2003](#2-crear-la-máquina-virtual-de-windows-server-2003)
    - [2.1. Configurar la máquina virtual](#21-configurar-la-máquina-virtual)
    - [2.2. Configurar almacenamiento y red](#22-configurar-almacenamiento-y-red)
    - [2.3. Instalación de Windows Server 2003](#23-instalación-de-windows-server-2003)
  - [3. Configuración de red en VirtualBox](#3-configuración-de-red-en-virtualbox)
    - [3.1. Configurar adaptadores de red en VirtualBox](#31-configurar-adaptadores-de-red-en-virtualbox)
  - [4. Configurar Windows Server 2003 (Servidor - IP Fija)](#4-configurar-windows-server-2003-servidor---ip-fija)
    - [4.1. Asignar IP en Windows Server 2003](#41-asignar-ip-en-windows-server-2003)
  - [5. Configurar Windows XP (Cliente - IP Manual o Automática)](#5-configurar-windows-xp-cliente---ip-manual-o-automática)
  - [6. Probar la conexión entre ambas máquinas](#6-probar-la-conexión-entre-ambas-máquinas)
    - [6.1. Probar conectividad con ping](#61-probar-conectividad-con-ping)
  - [7 Configuración del Controlador de Dominio en Windows Server 2003](#7-configuración-del-controlador-de-dominio-en-windows-server-2003)
  - [7.1. Instalar Active Directory:](#71-instalar-active-directory)
  - [7.2 Unión del Cliente Windows XP al Dominio](#72-unión-del-cliente-windows-xp-al-dominio)
  - [8. Creación y Gestión de Usuarios y Grupos](#8-creación-y-gestión-de-usuarios-y-grupos)
    - [8.1. Crear un usuario en Active Directory:](#81-crear-un-usuario-en-active-directory)
    - [8.2. Crear un grupo y agregar usuarios](#82-crear-un-grupo-y-agregar-usuarios)
  - [9: Creación y Configuración de Recursos Compartidos](#9-creación-y-configuración-de-recursos-compartidos)
    - [9.1. Crear una unidad de red compartida](#91-crear-una-unidad-de-red-compartida)
    - [9.2 Conectar la unidad de red en Windows XP](#92-conectar-la-unidad-de-red-en-windows-xp)
    - [9.1. Pruebas y Verificación](#91-pruebas-y-verificación)
  - [10.Asignación Automática de Unidad de Red con una GPO](#10asignación-automática-de-unidad-de-red-con-una-gpo)
    - [10.1. Crear y Configurar la GPO](#101-crear-y-configurar-la-gpo)
      - [Crear una nueva GPO](#crear-una-nueva-gpo)
      - [Editar la GPO](#editar-la-gpo)
      - [Configurar la Unidad de Red](#configurar-la-unidad-de-red)
      - [2. Aplicar la GPO y Verificar](#2-aplicar-la-gpo-y-verificar)

# Configuración de un dominio de Windows con Virtualbox

## 1. Crear la máquina virtual de Windows XP

### 1.1. Configurar la máquina virtual

Abre VirtualBox y haz clic en "Nueva"

- Nombre: Windows XP
- Tipo: Microsoft Windows
- Versión: Windows XP (32-bit)
- Memoria RAM: 512 MB - 1 GB (según lo que quieras probar).
- Disco duro: Crear uno nuevo (VDI, tamaño fijo, 10-20 GB).

### 1.2: Configurar almacenamiento y arranque

- En la configuración de la máquina, ve a "Almacenamiento".
- Selecciona el Controlador IDE y carga la ISO de Windows XP.

### 1.3. Instalación de Windows XP

- Inicia la máquina y arranca desde la ISO.
- Sigue los pasos del instalador de Windows XP.
- Formatea el disco en NTFS.
- Completa la instalación y configura usuario/contraseña.

Windows XP SP3: M8DPF-XT324-YBKK9-3VF8C-M2X78

### 1.4. Instalar VirtualBox Guest Additions (Opcional)

- Ve a Dispositivos > Insertar imagen de Guest Additions.
- Instala los controladores para mejorar el rendimiento.

## 2. Crear la máquina virtual de Windows Server 2003

### 2.1. Configurar la máquina virtual

En VirtualBox, haz clic en "Nueva".

- Nombre: Windows Server 2003
- Tipo: Microsoft Windows
- Versión: Windows 2003 (32-bit)
- Memoria RAM: 1 GB o más.
- Disco duro: 10-30 GB (según uso).

### 2.2. Configurar almacenamiento y red

- En "Almacenamiento", carga la ISO de Windows Server 2003 en el Controlador IDE.
- En "Red", usa el modo Red Interna si quieres conectar ambas máquinas entre sí.

### 2.3. Instalación de Windows Server 2003

- Arranca la máquina e inicia la instalación desde la ISO.
- Sigue los pasos del instalador y selecciona NTFS como sistema de archivos.
- Configura una contraseña para el administrador.
- Configura el Rol de Servidor (si quieres probar DHCP, DNS, Active Directory, etc.).

Windows Server 2003 Standard x64 Edition
- Clave: VWMD9-2Q897-F427R-TV2KY-CRF2B
- administrator password: 123456
- COMPUTER NAME: SERVIDOR
- Zona horaria: +1 GMT

Tras reiniciar  la máquina virtual del servidor, iniciamos sesión:

Para pulsar Ctrl+alt+supr en la máquina virtual clic derecho en el icono de la flecha y:

Iniciamos sesión como administrador:

## 3. Configuración de red en VirtualBox

Antes de configurar las direcciones IP dentro de los sistemas operativos, debemos asegurarnos de que ambos usen la misma red interna en VirtualBox.

### 3.1. Configurar adaptadores de red en VirtualBox

- En VirtualBox, ve a Configuración > Red en cada máquina virtual.
- En el Adaptador 1, selecciona Red Interna y nómbrala (ejemplo: "RedXP2003").
- Asegúrate de hacer esto en ambas máquinas.

## 4. Configurar Windows Server 2003 (Servidor - IP Fija)

Dado que actuará como servidor de red, asignaremos una IP fija.

### 4.1. Asignar IP en Windows Server 2003

- Abre el Panel de Control > Conexiones de red.
- Haz clic derecho en Conexión de área local > Propiedades.
- Selecciona Protocolo de Internet (TCP/IP) > Propiedades.

Configura la siguiente IP:

- Dirección IP: 192.168.1.1
- Máscara de subred: 255.255.255.0
- Puerta de enlace predeterminada: (Vacío o misma IP del servidor si hay NAT)
- Servidor DNS preferido: 192.168.1.1 (o una IP de Google como 8.8.8.8)
- Guarda los cambios y cierra.

## 5. Configurar Windows XP (Cliente - IP Manual o Automática)

Windows XP puede recibir una IP por DHCP desde el servidor o configurarse manualmente.

**Configurar IP manualmente en XP**

- Ve a Panel de Control > Conexiones de red.
- Clic derecho en Conexión de área local > Propiedades.
- Selecciona Protocolo de Internet (TCP/IP) > Propiedades.

Configura:

 - Dirección IP: 192.168.1.2
 - Máscara de subred: 255.255.255.0
 - Puerta de enlace: 192.168.1.1
 - DNS preferido: 192.168.1.1

Guarda los cambios y prueba la conexión

## 6. Probar la conexión entre ambas máquinas

Después de configurar las IPs, verifica que pueden comunicarse:

### 6.1. Probar conectividad con ping

En Windows XP, abre Símbolo del sistema (cmd).

Escribe:

```bash
ping 192.168.1.1
```
Si responde, la conexión es correcta.
En Windows Server 2003, prueba:

```bash
ping 192.168.1.2
```

Si hay respuesta, ambas máquinas están conectadas correctamente.

## 7 Configuración del Controlador de Dominio en Windows Server 2003

Objetivo: Configurar un dominio en Windows Server 2003, unir un equipo con Windows XP y gestionar usuarios, grupos y recursos compartidos en la red.

## 7.1. Instalar Active Directory:

- Abre Ejecutar (Win + R), escribe ``dcpromo`` y presiona Enter.
- Selecciona "Controlador de dominio para un nuevo dominio".
- Elige "Dominio en un nuevo bosque".
- Introduce un nombre de dominio: ``aulainformatica.local``
- Configura una contraseña segura para el administrador de Active Directory.
- Completa la instalación y reinicia el servidor.

## 7.2 Unión del Cliente Windows XP al Dominio

En Windows XP, asigna una IP estática en la misma subred del servidor y usa la IP del servidor como DNS principal.

Unir al dominio:

- Ve a **Mi PC > Propiedades > Nombre de equipo > Cambiar**.
- Selecciona **Dominio**, introduce el nombre (aulainformatica.local) y presiona Aceptar.
- Introduce las credenciales del administrador del dominio cuando se soliciten.
- Reinicia el equipo.

## 8. Creación y Gestión de Usuarios y Grupos

### 8.1. Crear un usuario en Active Directory:

En el servidor, abre Usuarios y Equipos de Active Directory (``dsa.msc``).

- Dentro del dominio, haz clic derecho en **Usuarios > Nuevo > Usuario**.
- Crea el usuario **Juan Pérez** con nombre de usuario **jperez**.
- Asigna una contraseña y marca "El usuario debe cambiar la contraseña en el próximo inicio de sesión".

Contraseña provisional: **!1234567a**, y marcamos que el usuario debe cambiar la contraseña en el primer inicio de sesión.

Ahora ya tendremos el usuario creado:

### 8.2. Crear un grupo y agregar usuarios

- Dentro de Active Directory, ve a **Usuarios > Nuevo > Grupo**.
- Llama al grupo **Alumnos**.
- Abre las propiedades del grupo **Alumnos**  haciendo doble click en el nombre del grupo y añade el usuario **jperez**. Vamos a add:

Escribimos parte del nombre de usuario y le damos a check names:

Nos aparecerá el usuario y le damos a OK:

Ahora el grupo **Alumnos** tiene un **miembro**, el usuario **jperez**.

## 9: Creación y Configuración de Recursos Compartidos

### 9.1. Crear una unidad de red compartida

- En el servidor, crea una carpeta en ``C:\Recursos_Alumnos``.
- Haz **clic derecho > Propiedades > Compartir**.
- Activa la opción "Compartir esta carpeta" y nómbrala **Alumnos**.
- Ve a la pestaña **Seguridad** y otorga permisos de **lectura/escritura** sólo al grupo **Ventas**.

El grupo Users, que es más amplio, tiene permisos para acceder a esta carpeta, por lo que se los vamos a quitar:

### 9.2 Conectar la unidad de red en Windows XP

- En el cliente, abre Mi PC > Herramientas > Conectar a unidad de red.
- Escribe la ruta ``\\Servidor\Ventas`` y selecciona una letra (ejemplo: ``Z:``).
- Introduce las credenciales del dominio si lo solicita.
- Asegura que el usuario pueda acceder y escribir en la carpeta.

### 9.1. Pruebas y Verificación

- ✅ El usuario jperez puede iniciar sesión en el dominio desde Windows XP.
- ✅ El usuario jperez tiene acceso a la unidad de red Ventas.
- ✅ El usuario puede crear y modificar archivos en la carpeta compartida.
- ✅ Los permisos de grupo se aplican correctamente.

## 10.Asignación Automática de Unidad de Red con una GPO

Vamos a configurar una **Política de Grupo (GPO)** en Windows Server 2003 para asignar automáticamente la **unidad de red Alumnos (Z:)** a los usuarios del grupo Ventas.

### 10.1. Crear y Configurar la GPO

Abrir el **Editor de Políticas de Grupo**:

En el servidor, abre **Ejecutar** (Win + R), escribe ``gpedit.msc`` y presiona Enter.

Alternativamente, abre Usuarios y Equipos de Active Directory (``dsa.msc``), haz clic derecho en el dominio (aulainformatica.local) y selecciona **Propiedades > Directiva de Grupo**.

#### Crear una nueva GPO

En la ventana Directiva de Grupo, haz clic derecho en el dominio y selecciona **"Nueva directiva de grupo"**.
Nómbrala ``Asignación Unidad Alumnos``.

#### Editar la GPO

Haz clic derecho sobre Asignación Unidad Ventas y selecciona Editar.

Ve a: Configuración de usuario > Preferencias > Configuración de Windows > Asignaciones de unidad
Haz clic derecho en Asignaciones de unidad > Nuevo > Unidad de red.

#### Configurar la Unidad de Red

En Ubicación, escribe la ruta del recurso compartido:

```bash
\\Servidor\Ventas
```

En Letra de unidad, selecciona Z:.

Marca la opción "Reconectar" para que la unidad se vuelva a mapear en cada inicio de sesión.

Filtrar la GPO para el grupo "Alumnos":

- Ve a la pestaña Ámbito.
- En Seguridad, haz clic en Agregar > Usuarios o grupos.
- Escribe **Alumnos**, selecciona el grupo y presiona Aceptar.

Asegúrate de que Ventas tiene activadas las opciones "Leer" y "Aplicar esta directiva de grupo".

#### 2. Aplicar la GPO y Verificar

Actualizar las Políticas en Windows XP:

En el cliente Windows XP, abre Símbolo del sistema (cmd) y ejecuta:

```
gpupdate /force
```

Reinicia el equipo.

Iniciar sesión con un **usuario** del grupo **Alumnos** y comprobar:

Abre **Mi PC** y verifica si aparece la **unidad Z:** conectada automáticamente.

Intenta crear y modificar archivos en la carpeta para verificar permisos.

Resultado Esperado:

- ✅ Los usuarios del grupo Ventas tendrán la unidad : asignada automáticamente al iniciar sesión.
- ✅ La configuración se aplicará sin necesidad de que los usuarios la configuren manualmente.

Extras (Opcionales)
🔹 Aplicar la GPO solo a ciertos equipos dentro del dominio.
 🔹 Configurar una GPO de Inicio de Sesión con un script net use Z: \\Servidor\Ventas.
 🔹 Usar gpresult /R en Windows XP para verificar si la GPO se aplica correctamente.
Este método ayuda a automatizar la administración de recursos en un dominio de Windows Server 2003. 🚀
