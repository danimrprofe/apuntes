# Comunicación entre procesos

Los procesos pueden comunicarse entre sí a través de variables compartidas o condiciones de carrera. Esto les permite compartir información y coordinar su ejecución.

Las **variables compartidas** son recursos compartidos entre procesos, mientras que las **condiciones de carrera** son mecanismos de sincronización entre procesos para garantizar que se ejecuten de manera ordenada. Estas dos herramientas permiten a los procesos trabajar juntos de manera eficiente y segura.

## Sección crítica

La **sección crítica** es una secuencia de instrucciones que se debe ejecutar de forma indivisible, sin entrelazarse con otras operaciones respecto a la misma variable.

La **exclusión mutua** es una forma de sincronización para proteger esta sección crítica.

Para esto, se utilizan los **semáforos**, que son variables que toman valores enteros no negativos y que tienen dos operaciones (up y down), tomados valores 0 o 1. Cuando un semáforo tiene valor 0 ó 1 se llama mutex.

Si dos procesos esperan una condición o recurso que dependen el uno del otro, se produce un **interbloqueo**.

## Sincronización en Java

- Para aplicar exclusión mútua utilizar palabra synchronized en declaración de atributos, métodos o en un bloque de ódigo
- Todos los métodos definidos con  synchronized se ejecutarán en exclusión mútua
- Cuando se ejecuta un método sincronizado el resto de métodos sincronizados no se puede ejecutar, y tendrán que esperar a que acabe el proceso que se está ejecutando