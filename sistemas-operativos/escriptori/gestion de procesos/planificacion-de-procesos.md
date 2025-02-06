# Planificación de procesos

## Fases de la planificación

Una vez cargado el proceso, el SO asigna a través del planificador la prioridad
del nuevo proceso respecto de los que hay en ejecución.

De esta forma, cada proceso atraviesa varias fases. En un momento dado, el
proceso se estará ejecutando; posteriormente estará en espera, mientras la UCP
ejecuta otro; otros procesos estarán preparados para ser lanzados; otros podrán
estar bloqueados, etc.

En estos cambios de proceso, el SO tiene que saber qué ficheros están abiertos
en cada proceso, qué periféricos se están utilizando, etc.

Cuando se están ejecutando varias tareas a la vez (procesos)

Es necesario compartir el tiempo de trabajo de la CPU.

El tiempo compartido consiste en dividir el tiempo de ejecución del procesador en minúsculos intervalos de tiempo (quantum) e ir asignando cada uno de esos intervalos de ejecución a cada proceso que está en ejecución.

## Planificación

Con esta técnica conseguimos indicar al ordenador los procesos que deben ejecutarse y los estados que estos deben adoptar. Gracias a los algoritmos de planificación podemos decidir qué proceso ha de ejecutarse en cada momento y por qué.

Algunas características de estos algoritmos son la imparcialidad, la equidad, la eficiencia, el tiempo de respuesta y el rendimiento

## Planificador

Se denomina planificador a aquella parte del SO encargada de asignar los recursos del sistema, de manera que se consigan unos objetivos de comportamiento especificados.

## Prioridades

- Los diferentes estados tienen una relación directa con lo que vamos a denominar prioridades
- Son aquellas que el administrador del sistema, o el propio sistema, asignan a cada proceso.
- De ello dependerá que un proceso se ejecute en más o menos tiempo.
- Se pueden establecer prioridades en función de la necesidad de ejecución de - algunos programas.
- Los programas que más se ejecutan, es decir, los más necesarios, tendrán prioridad de ejecución sobre aquellos que se ejecutan muy de cuando en cuando.
Es ahora cuando hemos de hablar de la planificación

## Aspectos a comparar

- Tiempos de respuesta
- Cambios de contexto
- Dificultad de implementación
