# Gestión de memoria

## Conceptos generales

### Funciones de gestión de memoria

La gestión de memoria es uno de los principales conceptos en el diseño de sistemas informáticos.

Se trata de la administración de los recursos de memoria del sistema para optimizar el rendimiento y aprovechar al máximo las capacidades de la memoria.

Esto involucra varias funciones, como la asignación y liberación de memoria a los procesos, el control de las zonas utilizadas, la protección de los datos y la creación de zonas compartidas de memoria.

### Jerarquía de memoria

Además, existe una jerarquía de memoria que se encarga de determinar el **orden** en que los datos se almacenan.

Esta jerarquía se compone de **registros**, **caché**, memoria **principal** y memoria **secundaria**. Esto permite aprovechar al máximo los recursos de memoria disponibles.

### Principio de localidad

Junto con la jerarquía de memoria existe un principio de localidad, que se refiere a los patrones de acceso a la memoria.

Estos patrones de acceso pueden ser **temporales**, como los bucles while y for, o **espaciales**, como los arrays y cadenas.

### Protección de memoria

La protección de la memoria también es un elemento importante para garantizar la seguridad de los datos. Esto se logra a través de **registros** de protección, **bits** de protección y **derechos** de acceso. Esto permite proteger los datos de accesos no autorizados.

### Control de memoria

La gestión de memoria también involucra el control de la memoria. Esto se logra a través de **mapas de bits** y **listas enlazadas**, lo que permite determinar qué áreas de la memoria se han asignado y cuáles están disponibles.

## Fragmentación

- Objetivo gestor de memòria: maximitzar utilización de la memòria
- Fragmentación produce desaprovechamiento

## Tipos de fragmentación

- Interna: espacio desaprovechado dentro de un bloque
- Externa: zones libres entre bloques de memòria que no pueden ser
llenados

## Modelos de gestión de memoria

Los modelos de gestión de memoria se refieren al uso de la memoria RAM en una computadora. Estos incluyen la "Máquina desnuda", el "Monitor monolítico".

En la **Máquina desnuda**, el sistema operativo ocupa una pequeña parte de la memoria RAM, que se le asigna de forma fija. Esto deja el resto de la memoria RAM a disposición del usuario. Esto tiene la ventaja de que el sistema operativo puede gestionar la memoria, sin embargo, la desventaja es que la memoria RAM asignada al sistema operativo no está disponible para el usuario. Los programas del usuario nunca pueden invadir la memoria asignada al sistema operativo.

En el **Monitor monolítico**, el sistema operativo se carga en memoria ROM. Esto significa que el sistema operativo no está sujeto a cambios, lo que aumenta la estabilidad de la computadora. El SO puede establecer límites de dirección para cada programa, lo que significa que ningún programa puede acceder a la memoria asignada a otro programa. Esto garantiza la seguridad y la privacidad.

## Asignación contigua

La asignación contigua es un método de asignación de memoria en la cual los bloques de la memoria son asignados a los diferentes procesos. Estos bloques pueden ser de diferentes tamaños. Existen dos tipos principales de multiprogramación:

* multiprogramación con número fijo de tareas (MFT)
* multiprogramación con número variable de tareas (MVT).

### Multiprogramación con número fijo de tareas (MFT)

- Memoria se divide en bloques que son asignados a los diferentes procesos
- Puede haber bloques de diferentes tamaños
- Lista de espera unida (cola única)
- Listas de espera separadas (colas variadas)

### Multiprogramación con número variable de tareas (MVT)

- Ventaja: fragmentación interna se elimina
- Desventaja: más completa de implementar

## Asignación dispersa

La asignación dispersa consiste en asignar memoria a procesos según sus necesidades; cada uno recibe la cantidad de memoria exacta que necesita, sin desperdiciar recursos.

### Segmentación

- Procesos se dividen en segmentos
- Tabla de descriptores de segmentos (TDS)
- Ventajas: No se necesita una partición contigua para todo el proceso

### Paginación

- Tabla de mapa de páginas
- Paginación multinivel
- División de memoria en marcos y del proceso en páginas.
- Asignación de páginas a marcos.
- Algoritmos de asignación y reemplazo

### Segmentación paginada

### Paginación multinivel

- Paginar la propia tabla de páginas
- Se necesitan más accesos a memoria

## Memoria virtual

La memoria virtual es una herramienta usada por los sistemas operativos para **aumentar** la cantidad de **memoria disponible** para los programas. Esto se logra al asignar una porción de la memoria del disco duro, como una extensión de la memoria RAM.

Cuando los programas intentan cargar datos en la memoria virtual, el sistema operativo interviene y carga datos desde la memoria virtual a la memoria RAM. Esto se conoce como **swapping** o intercambio.

 Se usan **algoritmos** para decidir cuándo se realiza el intercambio, como el algoritmo **FIFO** (First-In-First-Out) o el algoritmo **LRU** (Least Recently Used). Estos algoritmos permiten a los sistemas operativos **administrar la memoria** de forma eficiente.
