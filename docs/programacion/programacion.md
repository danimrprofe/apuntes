# Apuntes de programación

- [Apuntes de programación](#Apuntes-de-programaci%C3%B3n)
- [Conceptos de programa, aplicación y lenguaje de programación](#Conceptos-de-programa-aplicaci%C3%B3n-y-lenguaje-de-programaci%C3%B3n)
  - [Software](#Software)
  - [Aplicaciones](#Aplicaciones)
  - [Algoritmos](#Algoritmos)
    - [Formas de representación de un algoritmo](#Formas-de-representaci%C3%B3n-de-un-algoritmo)
  - [Lenguajes de programación](#Lenguajes-de-programaci%C3%B3n)
- [Tipos de lenguaje de programación](#Tipos-de-lenguaje-de-programaci%C3%B3n)
  - [Nivel de abstracción](#Nivel-de-abstracci%C3%B3n)
    - [Lenguajes de bajo nivel](#Lenguajes-de-bajo-nivel)
    - [Lenguajes de nivel medio](#Lenguajes-de-nivel-medio)
  - [Propósito](#Prop%C3%B3sito)
  - [Evolución histórica](#Evoluci%C3%B3n-hist%C3%B3rica)
  - [Forma de ejecutarse](#Forma-de-ejecutarse)
  - [MANERA DE ABORDAR LA TAREA A REALIZAR](#MANERA-DE-ABORDAR-LA-TAREA-A-REALIZAR)
  - [Paradigma de programación](#Paradigma-de-programaci%C3%B3n)
  - [Lugar de ejecución](#Lugar-de-ejecuci%C3%B3n)
  - [CARACTERÍSTICAS DE LOS LENGUAJES MÁS DIFUNDIDOS](#CARACTER%C3%8DSTICAS-DE-LOS-LENGUAJES-M%C3%81S-DIFUNDIDOS)
    - [C](#C)
    - [C++](#C)
    - [`Java`,](#Java)
    - [`PHP`,](#PHP)
    - [Python](#Python)
- [Tipos de código](#Tipos-de-c%C3%B3digo)
  - [Código fuente](#C%C3%B3digo-fuente)
  - [Código objeto](#C%C3%B3digo-objeto)
  - [Código ejecutable](#C%C3%B3digo-ejecutable)
  - [TRADUCTORES DE UN LENGUAJE DE PROGRAMACIÓN](#TRADUCTORES-DE-UN-LENGUAJE-DE-PROGRAMACI%C3%93N)
- [Obtención de código ejecutable](#Obtenci%C3%B3n-de-c%C3%B3digo-ejecutable)
  - [Compilador](#Compilador)
  - [Intérprete](#Int%C3%A9rprete)
  - [COMPILADOR + INTÉRPRETE](#COMPILADOR--INT%C3%89RPRETE)
  - [DIFERENCIA ENTRE COMPILADOR E INTÉRPRETE](#DIFERENCIA-ENTRE-COMPILADOR-E-INT%C3%89RPRETE)
  - [DEPURADORES](#DEPURADORES)
- [Paradigmas de programación](#Paradigmas-de-programaci%C3%B3n)
  - [Lenguajes](#Lenguajes)
    - [Lenguajes que soportan un paradigma](#Lenguajes-que-soportan-un-paradigma)
    - [Lenguajes que soporten múltiples paradigmas de programación](#Lenguajes-que-soporten-m%C3%BAltiples-paradigmas-de-programaci%C3%B3n)
    - [Lenguajes que soportan muchos paradigmas de programación](#Lenguajes-que-soportan-muchos-paradigmas-de-programaci%C3%B3n)
  - [Programación Imperativa](#Programaci%C3%B3n-Imperativa)
  - [Programación declarativa](#Programaci%C3%B3n-declarativa)
  - [Diferencias principales](#Diferencias-principales)
  - [¿Y qué hay de la programación orientada a objetos?](#%C2%BFY-qu%C3%A9-hay-de-la-programaci%C3%B3n-orientada-a-objetos)
  - [Conclusión](#Conclusi%C3%B3n)

# Conceptos de programa, aplicación y lenguaje de programación

## Software

La definición de software o programa informático es la siguiente: el software es un
conjunto de programas elaborados por el hombre, que controlan la actuación de la
computadora, haciendo que ésta siga en sus acciones una serie de pasos lógicos
predeterminados.

El software es el nexo entre el hardware (computadora) y el hombre (usuario). La
computadora, por sí sola, no puede comunicarse con el usuario y viceversa, ya que los
separa la barrera del lenguaje. El software trata de eliminar esa barrera,
estableciendo procedimientos de comunicación entre el hombre y la máquina; es decir,
el software obra como un intermediario entre el hardware y el hombre.

Existen diferentes tipos de software: software de sistema y software de aplicación

## Aplicaciones

Una **aplicación** es un tipo de programa informático diseñado para facilitar al usuario la realización de un determinado tipo de trabajo. Esto lo diferencia principalmente de otros tipos de programas (sistema) que realizan tareas más avanzadas y no pertinentes al usuario común, como los sistemas operativos (que hacen funcionar al ordenador, como Windows, Mac o Linux), las utilidades (que realizan tareas de mantenimiento o de uso general), y los lenguajes de programación (con el cual se crean los programas informáticos).

Las aplicaciones suelen diseñarse para la **automatización** de ciertas **tareas** complicadas
o tediosas como pueden ser la contabilidad, la redacción de documentos, o la gestión de un almacén. Algunos ejemplos de programas de aplicación son los procesadores de textos, hojas de cálculo, y base de datos.

De modo que una aplicación informática es un programa o consta de varios programas relacionados entre sí. Pero un programa no siempre es una aplicación, porque hay diferentes tipos de programas y los programas de aplicación son solo uno de ellos.

## Algoritmos

Cuando queremos resolver un problema a través de la creación de un programa informático habremos de diseñar previamente lo que se denomina un algoritmo. Un **algoritmo** es la forma de resolver un problema, los pasos a seguir para resolver un problema estándar.

Se llama algoritmo a la secuencia de pasos organizados a seguir para resolver un problema. Cualquier algoritmo debe tener las siguientes características:

- La descripción de cada paso no debe llevar a ambigüedades, los pasos son absolutamente explícitos y no inducen a error.
- El número de pasos debe ser finito, de forma que el algoritmo se pueda ejecutar en un tiempo finito.

Los algoritmos son independientes de la sintaxis de cada lenguaje de programación en particular, siendo evidente que el algoritmo que lleve a la solución de un determinado problema puede ser expresado utilizando distintos lenguajes de programación.

### Formas de representación de un algoritmo

Hay distintas formas de escribir un algoritmo, bien usando un lenguaje específico de descripción de algoritmos (**pseudocódigo**), bien mediante representaciones gráficas (organigramas o **diagramas de flujo**).

- En los **diagramas de flujo** existen símbolos estandarizados que permiten reflejar distintos tipos de pasos en un algoritmo.
- El **pseudocódigo** es una forma de escribir los pasos, pero de la forma más cercana al lenguaje de programación que vamos a utilizar, es como un falso lenguaje muy cercano al lenguaje humano.

Independiente del lenguaje de programación que vaya a usarse, un algoritmo que esté escrito en pseudocódigo o con un diagrama de flujo es fácilmente traducible a muchos lenguajes de programación.

## Lenguajes de programación

Un **lenguaje de programación** es un lenguaje diseñado para describir el conjunto de acciones consecutivas que un equipo debe ejecutar. Por lo tanto, un lenguaje de programación es un modo práctico para que los seres humanos puedan dar instrucciones a un equipo. Hay muchísimos, de toda clase de tipos y características, inventados para facilitar el abordaje de distintos problemas, el mantenimiento del software, su reutilización, mejorar la productividad, etc.



## Evolución histórica

Con el paso del tiempo, se va incrementando el nivel de abstracción, pero en la práctica, los de una generación no terminan de sustituir a los de la anterior:

- Lenguajes de **primera generación** (1GL): Código máquina.
- Lenguajes de **segunda generación** (2GL): Lenguajes ensamblador.
- Lenguajes de **tercera generación** (3GL): La mayoría de los lenguajes modernos, diseñados para facilitar la programación a los humanos. Ejemplos: C, `Java`.
- Lenguajes de **cuarta generación** (4GL): Diseñados con un propósito concreto, o sea, para abordar un tipo concreto de problemas. Ejemplos: SQL, matlab, Mathematica.
- Lenguajes de **quinta generación** (5GL): La intención es que el programador establezca el problema qué ha de ser resuelto y las condiciones a reunir, y la máquina lo resuelve. Se usan en inteligencia artificial. Ejemplo: Prolog.

## Forma de ejecutarse

Según la manera de ejecutarse:

- Lenguajes compilados
- Lenguajes interpretados
- También los hay mixtos

## MANERA DE ABORDAR LA TAREA A REALIZAR

Según la manera de abordar la tarea a realizar, pueden ser:

- Lenguajes **imperativos**: Indican cómo hay que hacer la tarea, es decir, expresan los pasos a realizar. Ejemplo: C.
- Lenguajes **declarativos**: Indican qué hay que hacer. Ejemplos: Lisp, Prolog. Otros ejemplos de lenguajes declarativos, pero que no son lenguajes de programación, son HTML (para describir páginas web) o SQL (para consultar bases de datos).



## Lugar de ejecución

En sistemas distribuidos, según dónde se ejecute:

- Lenguajes de **servidor**: Se ejecutan en el servidor. Ejemplo: `PHP` es el más utilizado en servidores web.
- Lenguajes de **cliente**: Se ejecutan en el cliente. Ejemplo: `JavaScript` en navegadores web.

## CARACTERÍSTICAS DE LOS LENGUAJES MÁS DIFUNDIDOS

Algunos de los lenguajes más difundidos son:

- BASIC, que durante mucho tiempo se ha considerado un buen lenguaje para comenzar a
aprender, por su sencillez, aunque se podía tender a crear programas poco legibles. A
pesar de esta "sencillez" hay versiones muy potentes, incluso para programar en
entornos gráficos como Windows.

- COBOL, que fue muy utilizado para negocios (para crear software de gestión, que
tuviese que manipular grandes cantidades de datos), aunque últimamente está bastante
en desuso.

- FORTRAN, concebido para ingeniería, operaciones matemáticas, etc. También va
quedando desplazado.

- Ensamblador, muy cercano al código máquina (es un lenguaje de "bajo nivel"), pero
sustituye las secuencias de ceros y unos (bits) por palabras más fáciles de recordar,
como MOV, ADD, CALL o JMP.

### C

- Uno de los mejor considerados actualmente (junto con C++ y `Java`, que
mencionaremos a continuación), porque no es demasiado difícil de aprender y
- Permite un grado de control del ordenador muy alto, combinando características de lenguajes de
alto y bajo nivel.
- Es muy transportable: existe un estándar, el ANSI
- Asegura que se pueden convertir programas en C de un ordenador a otro o de un sistema
operativo a otro con bastante menos esfuerzo que en otros lenguajes.

### C++

- Un lenguaje desarrollado a partir de C, que
- permite Programación Orientada a Objetos, por lo que resulta más adecuado para proyectos de una cierta envergadura.
- Creado por Bjarne Stroustrup.

### `Java`,

- Desarrollado a su vez a partir de C++
- Elimina algunos de sus inconvenientes
- Ha alcanzado una gran difusión gracias a su empleo en Internet.

### `PHP`,

- Es un lenguaje de programación interpretado, diseñado originalmente para la
creación de páginas web dinámicas.
- Se usa principalmente para la interpretación del lado del servidor (server-side scripting)
- Actualmente puede ser utilizado desde una interfaz de línea de comandos o en la creación de otros tipos de programas.

### Python

- Es un lenguaje de programación de alto nivel
- Filosofía hace hincapié en una sintaxis muy limpia y que favorezca un código legible.
- Se trata de un lenguaje de programación multiparadigma ya que soporta orientación a objetos, programación imperativa y, en menor medida, programación funcional

# Tipos de código

## Código fuente

Se le da el nombre de **código fuente** a los programas escritos en un determinado lenguaje de programación y que está compuesto por instrucciones escritas por un programador.

## Código objeto

Se llama **código objeto** al código que resulta de la compilación del código fuente. Consiste en lenguaje máquina o bytecode y se distribuye en varios archivos que corresponden a cada código fuente compilado.

## Código ejecutable

Para obtener un **código ejecutable** se han de enlazar todos los archivos de código objeto con un programa llamado enlazador.



## DEPURADORES

El **depurador** (debugger) es un programa independiente del editor, el compilador y el enlazador. Suele estar integrado con los otros tres, de modo que desde el entorno de programación se puede lanzar cualquiera de los programas, pero también se puede usar por separado.

El depurador es una herramienta fundamental para localizar y corregir los errores en tiempo de ejecución.

# Paradigmas de programación

Existen muchos paradigmas de programación diferentes, cada uno de ellos tiene sus propias características y tratan de solucionar los problemas clásicos del desarrollo de software desde diferentes perspectivas y filosofías. Hoy vamos a ver algunas diferencias entre paradigmas de programación populares.

Los paradigmas de programación solo son propuestas tecnológicas adoptadas por la Comunidad de desarrolladores que se enfocan a resolver uno o varios problemas definidos y delimitados. Existen muchos paradigmas de programación diferentes, posiblemente el más ampliamente utilizado hoy en día sea el de la programación orientada a objetos.

## Lenguajes



## ¿Y qué hay de la programación orientada a objetos?

La programación orientada a objetos es una forma de programación imperativa

Al programar orientando a objetos se describe la secuencia que debe seguir el programa para resolver un problema dado.

La diferencia con otras formas de programación imperativas como la programación estructurada es que en la orientación a objetos se hace uso de estructuras de datos llamadas objetos.

Estos objetos son estructuras que aglutinan propiedades y métodos conjuntamente.

## Conclusión

Aunque la diferencia entre la programación estructurada y la programación orientada a
objetos es grande, realmente la mayor diferencia se encuentra en las ramas superiores.

Las diferencias entre programación imperativa y programación declarativa es mucho más
severa y compleja que las diferencias entre diferentes sub-paradigmas dentro de la
programación imperativa.

Sobre lo que nos depara el futuro, no estoy seguro, ni siquiera tengo una opinión
propia bien formada al respecto, pero es aconsejable no perder la pista de lenguajes
como `Haskell` e intentar comprender el paradigma de la programación declarativa para
crecer como profesionales del desarrollo de software y sobre todo mantener una postura
abierta y alejar los talibanismos y la polémica estéril.

