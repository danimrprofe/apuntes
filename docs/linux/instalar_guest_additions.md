# Guest additions

Las Guest Additions son un conjunto de herramientas y controladores desarrollados para mejorar la funcionalidad y la compatibilidad entre el sistema operativo invitado y la máquina virtual.

Estas herramientas permiten a los usuarios compartir archivos, carpetas y discos entre la máquina virtual y la máquina anfitriona. También permiten a los usuarios mejorar la velocidad del sistema, agregar compatibilidad con dispositivos USB, habilitar el soporte de copiar y pegar entre la máquina anfitriona y la máquina virtual, así como mejorar la experiencia de visualización, entre otras funciones.

## Instalar guest additions

Ir al menu Dispositivos/insertar imagen de CDROM de Guest aditions

```
sudo mkdir /mnt/cdrom
sudo mount /dev/cdrom /mnt/cdrom
cd /mnt/cdrom
ls -lisa
sudo ./VBoxLinuxAdditions.run
sudo reboot now
```
