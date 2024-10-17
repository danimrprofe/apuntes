# Input y print

La función **input()** es una función incorporada en Python 3 que permite al usuario ingresar datos desde el teclado. Esta función se utiliza para obtener la entrada del usuario para que el programa pueda realizar alguna tarea específica.

```python
input()
```

Al llegar a esta instrucción, el programa se quedará esperando a que se pulse la tecla **intro**. Antes de ello, escribiremos lo que queramos enviar al ordenador.

Si queremos que muestre un mensaje antes, podemos incluirlo entre los paréntesis, usando comillas.

```python
input("Dime cómo te llamas")
```

Ahora, primero aparecerá la frase y a continuación, el programa quedará a la espera de que escribamos algo y escribamos **intro** al terminar.

Podemos utilizar variables para guardar la información que devuelve la función input:

```python
valor = input("Introduce un valor: ")
print("El valor ingresado es", valor)
```

En este ejemplo, el usuario primero verá el mensaje "Introduce un valor:". Después de escribir el valor, el programa imprimirá "El valor ingresado es" seguido del valor ingresado por el usuario.

Ejemplo 2:

```python
nombre = input("¿Cuál es tu nombre? ")
print("Hola " + nombre + ", ¡bienvenido!")
```

En este ejemplo, el usuario primero verá el mensaje "¿Cuál es tu nombre?". Después de escribir su nombre, el programa lo saludará con el mensaje "Hola [nombre], ¡bienvenido!".
