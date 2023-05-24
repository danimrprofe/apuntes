# tar
```
tar <funciones> archivo_a_crear <archivos a adicionar>
```
Funciones:

c: crea un contenedor
x: extrae archivos en un contenedor
f: tes tea los archivos almacenados en un contenedor
v: modo verbose

¿especifica el nombre del contenedor
- z: comprime o descomprime mediante gzip
- j: comprime o descomprime mediante bzip2

Ejercicios:

1.	Empaqueta un directorio llamado MANUALES y guarda los datos en un fichero llamado MANU ALEA-EMPAQUETADOS.tar:
```
Tar cvf MANUALES-EMPAQUETADOS .tar MANUALES
```
2.	Empaqueta el directorio /etc/CONFIGURACION y guarda los datos en un fichero llamado CONFIGURACION.tar en el directorio:
```
Tar cvf /etc/CONFIGURACION.tar /etc/CONFIGURACION
```
3.	Empaqueta y comprime un directorio llamado ARCHIVOS y guárdalo en un fichero llamado ARCHIVOS_C OMPRIMIDOS. tgz:
```
Tar czvf ARCHTVOS_COMPRIMIDOS.tgz ARCHIVOS
```
Si el archivo que queremos desempaquetar está comprimido, es decir si queremos descomprimir y desempaquetar en un solo paso, tenemos que hacerlo con la opción z del comando tar:

```
Tar xzvf ARCHIVOS_COMPRIMIDOS.tgz
```
Si queremos desempaquetar pero no descomprimir un archivo llamado ARCHIVOS_COMPRIMIDOS.tgz:
```
Tar xvf ARCHTVOS_COMPRIMIDOS.tar
```
El archivo ARCHIVOS_COMPREMEDOS.tgz está en el mismo directorio desde donde lanzamos el comando. Los contenidos se desempaquetarán en el mismo directorio donde estamos situados.

4.	Crear un contenedor sin comprimir y luego verificar su contenido:
```
Tar -cvf /tmp/ejemplo 1 .tar /var/log
Tar -tvf /tmp/ej emplo 1 .tar
```
5.	Crear un contenedor comprimido con gzip y luego verificar su contenido:
```
Tar -czvf /tmp/ejemplo2.tar. gz /var/log
Tar -tzvf/tmp/ej emplo2.tar.gz
```
6.	Crear un contenedor comprimido con bzip2 y luego verificar su contenido:
```
Tar -cjvf /tmp/ejemplo3 .tar.bz2 .-Var/log
Tar -tjvf /tmp/ejemplo 3. tar.bz2
```
