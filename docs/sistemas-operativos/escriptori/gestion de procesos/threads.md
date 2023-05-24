## Threads o hilos

Un thread es un subproceso de un proceso:

- Consume recursos propios
- Depende del proceso padre que lo ha ejecutado.

Una hebra es un punto de ejecución de un proceso.

Un proceso tendrá siempre una hebra, en la que corre el propio programa, pero puede tener más hebras.

Las hebras representan un método software para mejorar el rendimiento y eficacia de los sistemas operativos.

Las hebras de un mismo proceso compartirán:

- Memoria
- Archivos
- Recursos hardware, etc.

### Ejemplo (Word)

Si ejecutamos el procesador de textos Word, con un solo documento abierto, el programa Word convertido en proceso estará
ejecutándose en un único espacio de memoria, tendrá acceso a determinados archivos (galerías de imágenes, corrector
ortográfico, etc.), tendrá acceso al hardware (impresora, disquetera), etc.

En definitiva, este proceso, de momento, solamente tiene una hebra.

Si en esta situación, sin cerrar Word, abrimos un nuevo documento, Word no se vuelve a cargar como proceso.

Simplemente el programa, convertido en proceso, tendrá a su disposición dos hebras o hilos diferentes, de tal forma que el
proceso sigue siendo el mismo (el original).

Word se está ejecutando una sola vez

El resto de documentos de texto que abramos en esta misma sesión de trabajo no serán procesos propiamente dichos.

Serán hilos o hebras del proceso principal, que es el propio procesador de textos.

Antes de hablar de prioridades, y teniendo muy en cuenta lo comentado anteriormente, vamos a ver los
diferentes estados en los que pueden estar los procesos.

Hoy en día existen gran cantidad de programas diseñados en multihilo o multihebra. De esta forma, si un
programa puede realizar varias cosas, como analizar el registro del equipo, desfragmentar el disco duro y
realizar copias de seguridad, todas ellas se podrán ejecutar a la vez. En programas convencionales,
solamente se podría ejecutar una tras otra, pero no todas a la vez.
