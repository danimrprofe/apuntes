# Gestión de archivos y dispositivos

La gestión de archivos y dispositivos es un proceso fundamental en el funcionamiento de un sistema informático. Esto involucra el almacenamiento, manipulación y acceso de datos. Esto incluye la creación, modificación, eliminación y organización de archivos y dispositivos.

## Estructura

La estructura de gestión de archivos y dispositivos está formada por directorios, archivos y dispositivos.

- Los **directorios** son carpetas para almacenar archivos y directorios de una forma lógica.
- Los **archivos** son docuemntos que contienen datos, como textos, imágenes, etc.
- Los **dispositivos** son elementos de hardware que se conectan al sistema informático para permitir el almacenamiento de archivos. Estos dispositivos permiten al usuario guardar y acceder a los datos en caso de que el sistema de archivos se corrompa o pierda información.

## Funciones

- Crear/modificar/borrar archivos
- Crear/modificar/borrar directorios
- Compartición de archivos
- Permisos
- Hacer procesos transparentes al usuario

## Manejo del espacio

Grabación contigua VS división en bloques

## Control de bloques libres

- Lista enlazada uniendo los bloques libres
- Mapa de bits. 1 bit por bloque determina si está libre o no

## Estructura del directorio

### Un único directorio (CP/M)

En el directorio de CP/M, todos los archivos se almacenan en un único nivel jerárquico, lo que significa que no hay subdirectorios dentro del directorio. El nombre de cada archivo debe ser único dentro del directorio, ya que no se admite la duplicación de nombres de archivos.

El nombre de cada archivo no puede exceder de ocho caracteres, aunque los archivos pueden tener hasta tres letras como extensión. Los archivos se clasifican por orden alfabético con el nombre de archivo completo, incluyendo la extensión.

El directorio se puede navegar utilizando comandos de línea de comandos, y la información de cada archivo, como el tamaño de archivo y la fecha de modificación, se puede ver con el comando DIR.

### Árbol de directorios (DOS)

Los árboles de directorios en DOS son más complejos que los de Unix. La entrada del directorio en DOS contiene el nombre, la extensión, los atributos, la fecha y el puntero al primer bloque, así como el tamaño del archivo.

### Unix (Más sencillo)

 Por otro lado, la entrada del directorio en Unix es mucho más sencilla, solo contiene el nombre del archivo y el número del nodo índice (**inode**).

 Esto hace que Unix sea mucho más fácil de usar al tener una representación más sencilla de la estructura de directorios.

## Almacenamiento de archivos

- Para aprovechar eficientemente el espacio, los archivos se dividen en bloques.
- Estos bloques se guardan en diferentes ubicaciones del disco.
- Necesaria asociación fichero - bloques para poder leer o escribir un archivo.

### Sistemas

- Puntero en la última posición de un bloque al siguiente
- Lista enlazada o tabla (FAT)
- Nodos índices (Linux/unix)
  - Punteros a bloques
  - Punteros indirectos (simples, dobles)

## Problema de fragmentación

### Fragmentación interna

- Se divide el disco en bloques de tamaño fijo
(4KB)
- Cualquier archivo más pequeño ocupa un bloque entero
- Se desperdicia espacio (fragmentación interna).

### Fragmentación externa

- El cambio de tamaño de archivos, así como su creación y eliminación, dejan bloques libres insuficientes para ciertos
archivos (fragmentación externa).
- Una posible solución consiste en desfragmentar.

## Sistemas de archivos

Los sistemas de archivos son la forma en que los sistemas operativos almacenan, organizan y recuperan archivos en una computadora.

Los sistemas de archivos más comunes son **FAT, NTFS y EXT**. Estos sistemas de archivos pueden ser utilizados para compartir archivos en una red de computadoras.

La fiabilidad de un sistema de archivos depende de la capacidad de detectar y recuperarse de los bloques defectuosos, así como de la creación de copias de seguridad adecuadas.

## Técnicas de almacenamiento intermedio

- Spooling (impresión)
- Buffers (entre dispositivos)
- Caché (disminuir accesos a disco)
- Utilización eficiente de bloques en disco

## Seguridad

- Principios de diseño para seguridad
- Ataques de seguridad comunes
- Validación del usuario
  - Autenticación: sabe, tiene, es. Desafío (captcha)
  - Ingeniería social
  - Biometría
