# Formatear disco desde Clonezilla

## ¿Qué es Clonezilla y qué puedo hacer con él?

Clonezilla es una herramienta que, al igual que otras como Norton Ghost, nos permite crear una imagen (como si fuese una foto de lo que hay dentro ,de un disco duro, guardado todo como un solo archivo) a partir de un disco para posteriormente:

- Guardarla como copia de seguridad
- Restaurarla (volverla a copiar a ese disco) en caso de problemas
- Aprovechar la imagen creada para clonar el disco original, copiando la imagen en un disco nuevo.

## ¿Cómo hago para utilizar Clonezilla?

1. Cargaremos una imagen ISO de Clonezilla que abremos descargado previamente en el «lector de discos» de nuestra máquina virtual (por ejemplo en VirtualBox)
2. Grabaremos en un CD la imagen ISO y la introduciremos en el lector de cd, si es una máquina virtual:
3. Formatear el disco desde la shell de Clonezilla

Para ello, entrar en el shell (consola de comandos) desde el menú de Clonezilla y así poder ejecutar los diferentes comandos:

## 1) Comprobando el disco con Fdisk

Al crear el disco, no está ni formateado, ni tiene tabla de particiones, ni sistema de archivos, por lo que Clonezilla no lo reconoce.

```bash
Command (m for help): F
Unpartitioned space /dev/sdb: 10 GiB, 10736369664 bytes, 20969472 sectors
 Units: sectors of 1 >k 512 = 512 bytes
 Sector size (logical/physical): 512 bytes / 512 bytes
 Start   End   Sectors    Size
 2048   20971519    20969472 10G
```

## 2) Crear tabla de particiones GPT desde Clonezilla

En este caso la crearé del tipo GPT

```bash
Command (m for help): g
Created a new GPT disklabel (GUID: 76AAA8AE-BD36-BE42-AE5D-A44852D884E0).
```

## 3) Creando una partición que ocupe todo el disco en Clonezilla

Tengo para crear hasta 128 particiones, nada más y nada menos. Elijo los parámetros por defecto porque pretendo ocupar todo el disco

```bash
Command (m for help): n
Partition number (1-128, default 1): 1
First sector (2048-20971486, default 2048):
Last sector, +sectors or +size£K,M,G,T,P} (2048-20971486, default 20971486) Created a new partition 1 of type 'Linux filesystem' and of size 10 GiB.
```

## 4) Mostrar la tabla de particiones con Clonezilla

Vamos a comprobar que ha quedado todo bien. Me ha quedado estupenda. Ojo que de momento hasta que no lo grabe no quedará escrita la tabla de particiones, por lo que aún no es definitivo.

```bash
Command (m for help): p
Disk /dev/sdb: 10 GiB, 10737418240 bytes, 20971520 sectors Units: sectors of 1 >k 512 = 512 bytes Sector size (logical/physical): 512 bytes / 512 bytes I/O size (minimum/optimal): 512 bytes / 512 bytes Disklabel type: gpt
Disk identifier: 76AAA8AE-BD36-BE42-AE5D-A44852D884E0
Device Start End Sectors Size Type
Ddev/sdbl 2048 20971486 20969439 10G Linux filesystem
```

## 5. Grabo la tabla de particiones

Ahora sí, vamos a grabar la tabla de particiones.

```bash
Command (m for help): w
The partition table has been altered.
Calling ioctlO to re-read partition table.
Syncing disks.
```

## 6) Última comprobación

Con **lsblk** podemos comprobar que todo es correcto. Tengo 2 particiones porque en esta máquina virtual tenía dos discos diferentes, de 10 GiB cada uno:

- La partición sda1 corresponde al disco SATA a (el primero)
- La partición sda2 corresponde al disco SATA b (el segundo)

```bash
user@debian:~$ lsblk
 NAME MAJrMIN RM SIZE RO TYPE MOUNTPOINT
 loopO 7:0 0 192.8M 1 loop /lib/live/mount/rootfs/filesystem.squashfs
 sda 8:0 0 10G 0 disk
 *—sdal 8:1 0 10G 0 part
 sdb 8:16 0 10G 0 disk
 *—sdbl 8:17 0 10G 0 part
 srO 11:0 1 230M 0 rom /lib/live/mount/medium
 ```