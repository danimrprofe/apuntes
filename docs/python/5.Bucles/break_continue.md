## BREAK Y CONTINUE. Interrumpiendo bucles.

A veces estamos recorriendo un bucle “buscando” algo, de manera que cuando lo encontramos ya no queremos seguir haciendo iteraciones, queremos “interrumpir” la búsqueda de alguna manera.
BREAK te saca del bucle completamente de forma inmediata.
CONTINUE interrumpe abruptamente la iteración en la que estás y pasa a la siguiente.
Vamos a poner unos códigos de prueba sólo para ver cómo funcionan

## Ejemplo continue

Al cumplirse la condición, continúe hace que se interrumpa la iteración y se pase a la siguiente, por eso no imprime la letra “a”, que aparece. El resto si se imprimen.

Como ves al estar CONTINUE nos salimos de la antes de imprimir ese valor .
Ejemplo con break
Al cumplirse la condición, break hace que se interrumpa el bucle entero y por eso no se imprimen letras hasta la a.

## Ejemplo de password

La estructura “while True” es una manera de escribir un bucle infinito. Significa que algo se va a repetir siempre hasta que cerremos el programa.
Sería como decir “mientras que verdadero sea verdadero...” Funcionaría igual que “while 1=1” o cualquier expresión lógica que sepamos que siempre es verdadera.
Si nos aciertan la contraseña, entramos en el condicional y break nos saca del bucle while, de forma que ya empezamos a ejecutar el código que hay después.