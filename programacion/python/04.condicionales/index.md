# Condicionales

Los condicionales son una parte importante de la programación, ya que nos permiten controlar el flujo de nuestro programa. Estos nos permiten ejecutar un código si una condición es verdadera o ejecutar un código diferente si la condición es falsa.

En Python, hay tres tipos principales de condicionales: if, elif y else.

## Partes de un condicional

Un condicional tiene tres “partes”.

1. La condición que queremos comprobar (en este caso edad>18)
2. Las acciones que tomamos si se cumple la condición (nos dirá que somos viejos)
3. Las acciones que tomamos si NO se cumple la condición (dirá que somos jóvenes)

## If

El condicional if es el más básico de los condicionales. Si una condición es verdadera, se ejecutará el código que sigue al condicional.

```python
if condicion:
    codigo
```

Por ejemplo, si queremos comprobar si un número es mayor que 10, podemos usar el siguiente código:

```python
numero = 5
if numero > 10:
    print("El número es mayor que 10")
```

En este caso, la condición es falsa, por lo que el código no se ejecutará.

## Elif

Elif es una palabra clave que significa "si la condición anterior fue falsa, entonces prueba esta condición". Esto nos permite comprobar múltiples condiciones y ejecutar diferentes códigos dependiendo de la condición.

```python
numero = 5
if numero > 10:
    print("El número es mayor que 10")
elif numero == 5:
    print("El número es 5")
```

En este caso, la primera condición es falsa, por lo que el código no se ejecutará. Sin embargo, la segunda condición es verdadera, por lo que el código después del elif se ejecutará.

## Else

Else es una palabra clave que significa "si ninguna de las condiciones anteriores fue verdadera, entonces ejecuta este código". Esto es útil si queremos ejecutar un código si ninguna de nuestras condiciones fue verdadera.

```python
numero = 5
if numero > 10:
    print("El número es mayor que 10")
elif numero == 5:
    print("El número es 5")
else:
    print("El número es menor que 10")
```

En este caso, ninguna de las condiciones anteriores fue verdadera, por lo que el código después del else se ejecutará.

# Actividad

1. Completa la actividad del supermercado para que revise si la cantidad que damos para pagar es suficiente o no y nos avise en tal caso.
2. Al comienzo del programa deberá pedirnos una contraseña para acceder a la tienda, y solo podremos acceder a ella si escribimos la contraseña correcta.