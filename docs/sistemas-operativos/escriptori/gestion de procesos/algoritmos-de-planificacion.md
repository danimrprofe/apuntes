# Algoritmos de planificación

Gracias a los algoritmos de planificación, especialmente en sistemas operativos multi-proceso o en sistemas operativos en red,
Siempre y cuando se ejecuten varios procesos en el mismo equipo,

La CPU se encarga de asignar tiempos de ejecución a cada proceso según

- El tipo de algoritmo
- La prioridad de cada proceso

## Tipos

- FIFO
- SJF
- Prioridad
- Round Robin
- Colas multinivel

### Algoritmo FIFO (First In First Out) o FCFS (First Come First Serve)

Los ciclos de UCP asignados a cada proceso se asignan en función de una cola FIFO.
Al primer proceso que llega se le asignan tiempos o ciclos de UCP hasta que termina completamente.
A continuación, se ejecuta completo el siguiente proceso que hay en la cola FIFO y así sucesivamente hasta terminar con el último proceso.
Este algoritmo de planificación normalmente se utiliza para la gestión de trabajos en colas de impresión, respecto de los trabajos que van llegando a la impresora.

### Algoritmo Round Robin

Asigna **rotativamente** tiempos de ejecución a los diferentes procesos.

También se llama algoritmo de Round-Robin y en él la asignación de tiempos de ejecución a los procesos es la misma y de forma secuencial.

A cada uno se le asigna el mismo quantum o intervalo de tiempo de ejecución.

Selección de proceso mediante cola FIFO

Es el algoritmo utilizado normalmente en la asignación de tiempos en sistemas operativos multiusuario y multiproceso

En la actualidad se puede decir que es el utilizado en sistemas operativos monousuario y que trabajan en multitarea.

### Colas multinivel

Principales características:

- Determinar cuantas colas tendrá el sistema y el algoritmo de planificación de cada una
- Debe existir un planificador de nivel superior para determinar que cola será atendida
- Cuando llega un proceso se clasifica para determinar en qué cola se introduce
- Definir cuando un proceso puede cambiar de tipo de cola

## Selección del algoritmo optimo

- Evaluación analítica
- Modulación determinista
- Modelos de colas
- Simulación