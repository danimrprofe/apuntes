# Utilidades para el desarrollo y pruebas de programas. Compiladores. Interpretes. Depuradores

- Lenguaje ordenadores formado por instrucciones codificadas en código binario
- Lenguajes de programación formado por símbolos y reglas que permiten escribir programas
- Creados para facilitar la tarea de la programación
- Compuestos por un léxico, sintaxis y semántica
- Necesidad de traducir de un programa escrito en un lenguaje fuente a un lenguaje máquina.

Tipos de traductores:

- Compiladores
- Intérpretes
- Según lenguajes de programación uno u otro
- ``C++`` compilado
- Java compilado e interpretado
- SQL, interpretado

## Compiladores

- Convierte un programa de un lenguaje a otro, informando de posibles errores y generando los resultados a partir de datos de entrada.
- A partir de un lenguaje fuente se crea un programa objeto ejecutable

### Ventajas

- Solo una compilación y el código objeto se puede ejecutar muchas veces sin necesitar de recompilar
- Si se encuentra un error no se genera un programa objeto
- Programas objeto codificados, por lo que son “confidenciales” al no mostrar el código
- Mayor eficiencia que los lenguajes interpretados
- Consumen mayor cantidad de memoria
- Los archivos compilados solo serán ejecutables en el tipo de máquina para el que han sido compilados

### Tipos de compiladores

- De una o varias pasadas
- Compiladores incrementales
- Compiladores cruzados

### Etapas del proceso de traducción

El proceso de traducción consta de dos etapas principales: análisis y síntesis.

La **etapa de análisis** incluye un análisis léxico, un análisis sintáctico mediante parsers, y un análisis semántico.

Por su parte, la **etapa de síntesis** comprende la generación de un código intermedio, la optimización del mismo y la generación de código.

### Elementos importantes en las etapas

- Tabla de símbolos: Estructura de datos que guarda información generada durante el proceso de compilación
- Manejador de errores: decide acciones a realizar al encontrar un error en el proceso de compilación
- Gestión de errores
- Errores léxicos, semánticos o sintácticos
- Errores de compilación
- Errores de ejecución

### Módulos externos al compilador

- Preprocesador: por ejemplo incluir código de librerías
- Ensamblador: traduce a código máquina
- Enlazador: crea ejecutables a partir de código objeto y librerías
