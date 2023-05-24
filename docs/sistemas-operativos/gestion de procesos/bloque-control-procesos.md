## Bloque de control de procesos

### Control de procesos

Los sistemas operativos disponen de los servicios necesarios para la gestión de los procesos, tales como su creación, terminación, ejecución periódica, cambio de prioridad, etc.

Durante su existencia, los procesos pasan por distintos estados cuyas transiciones están controladas por el SO.

Toda la información de un proceso que el SO necesita para controlarlo se mantiene en una estructura de datos: el bloque de control de procesos o BCP.

En SO multiproceso, el SO mantiene listas de bloques de control de procesos para cada uno de los estados del sistema.

### Estructura del bloque de control de procesos

Esta estructura de datos, que es única para cada proceso, identifica el proceso respecto de los demás y sirve para controlar su correcta ejecución.
Es lo que se llama el bloque de control del proceso

Partes:

- Estado del proceso
- Identificador o PID. Dependiendo del SO, a cada proceso se le asigna un PID.
- Contador de programa
- Prioridad. La asignada por el planificador.
- Ubicación en memoria. Dirección de memoria en la que se carga el proceso
  - Puntero a la zona de memoria
- Recursos utilizados. Recursos hardware y software para poder ejecutarse.
  - Puntero a los recursos asignados
- Zona de almacenamiento de registros en CPU

![imagen](2019-05-13-13-20-59.png)

### En programas multihilo o multihebra:

El BCP puede contener además el PPID, o Process Parent IDentif¡catión.

Este dato referencia el PID del proceso padre dentro del BCP, de tal forma que desde el propio BCP se pueden identificar todos los procesos que son hijos de otro, siempre y cuando tengan el mismo PPID.

En procesos convencionales, este dato en el BCP no existirá.