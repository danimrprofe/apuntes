programación en python 5
BUCLES
Introducción
La informática nace para tratar automáticamente la información. Si una tarea completa me va a llevar cinco minutos no tiene sentido invertir media hora en ver cómo automatizarla, pero si la tarea me llevaría una semana, bien puedo invertir un día en mirar cómo aligerarla.

# Bucles

Una de las herramientas más útiles para no tener que repetir un mismo código muchas veces son los bucles.

Los bucles nos permiten repetir tareas que son iguales o con pequeñas variaciones, un número de veces determinado o bien hasta que se cumpla alguna condición.

Imagina que queremos pintar los números del 1 al 4. Si quisiéramos repetir una misma operación varias veces sería muy largo y pesado de escribir.

Si lo pensáis bien, todas estas líneas siguen un patrón. Es decir, en cada línea estamos imprimiendo el número anterior incrementado en 1. Esto se repite hasta que el número sea el 4. Imaginad que lo queremos hacer hasta el número 100, sería muy largo. Los bucles nos ayudan en esta situación.









Calculadora de números primos
Un programa que va calculando los números primos. ¿Cómo podemos construir la lista de los números primos?
Explicación del problema
El algoritmo que nos enseñaron en el cole. Un número primo solo se puede dividir por 1 y por él mismo.
Empezamos nuestra lista con el 2. Este es primo.
Cogemos el número siguiente, el 3, y lo dividimos entre los primos que tenemos en nuestra lista (en este caso el 2).
Si sale resto cero con alguno es que no es primo
Si no sale resto cero y el cociente es menor que el divisor, entonces sabemos que ya será primo.
Cómo lo programamos
Ahí veréis que hay dos puntos de ruptura, uno si encontramos que no es primo y otro si después de dividir el cociente es menor que el divisor.
Por ejemplo, imagina que vamos por el llevamos la lista llena hasta el 13, esto quiere decir que será [2,3,5,7,11,13].
Nos toca probar el 14. Hacemos la división 14 entre 2, resto cero. Vaya, no es primo.
Nos toca probar el 15. Hacemos la división 15 entre 2, resto uno, cociente 7, mayor que 2, puede ser primo.
Siguiente primo de la lista, el 3. Hacemos la división 15 entre 3, vaya, resto cero. No es primo.
Con el 16 pasa lo mismo que con el 14, son pares. BREAK.
Nos toca ahora el 17. Hacemos la división 17 entre 2, resto uno, cociente 8, mayor que 2, puede ser primo, siguiente primo de la lista, el 3. 17 entre 3, resto 2, cociente 5, mayor que tres, puede ser primo. Siguiente primo de la lista, el 7, resto 3, ¡cociente 2 MENOR que 7... es primo! Lo añadimos a la lista de primos y BREAK.
Vamos calculando los números primos y metiéndolos en una lista


Te explico línea a línea. Pedimos un límite.
Inicializamos la lista de primos con el número 2. El bucle en i recorrerá todos los números de uno en uno hasta el máximo que nos han indicado.
El bucle en j recorre todos los primos para cada número que vamos eligiendo en el bucle en i Comprueba si el resto de dividir el número i entre el primo j da cero. Si es así, salimos del bucle en j, no hay que comprobar con más primos, ya sabemos que no lo es.
Si no sale cero (elif), comprueba si el cociente es menor que el divisor, en ese caso, sabemos que es primo, lo añadimos a la lista de primos y podemos dejar de comprobar con el resto de primos (bucle en j).
Finalmente, cuando ya hemos terminado con todos los números hasta el que nos dijeron, cuando se termine el bucle en i, podemos imprimir la lista completa de primos.

Programa nombre y contraseña
Programa que te pregunta el nombre y sólo si eres el indicado te pregunta la contraseña. Te pregunta quién eres y sólo si eres la persona indicada te pregunta la contraseña.

Funcionamiento
Como antes tenemos un bucle infinito (while True) (del que sólo podremos salir a las bravas). Nos pregunta quién somos y recoge la respuesta.
Si no digo el nombre correcto, interrumpe ahí el bucle y lo vuelve a empezar, preguntándome de nuevo quién soy.
Si digo el nombre correcto, sigue adelante
Me pregunta la contraseña, que guarda en una variable.
Si la contraseña es correcta sale del bucle infinito y me dirá “Estás dentro”, si no, vuelve a empezar el bucle y me preguntará el nombre de nuevo.

