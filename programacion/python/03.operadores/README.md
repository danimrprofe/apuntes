- [Operadores en Python](#operadores-en-python)
  - [Operadores de asignación](#operadores-de-asignación)
- [Operaciones con cadenas de caracteres](#operaciones-con-cadenas-de-caracteres)
  - [Concatenación](#concatenación)
  - [Repetición](#repetición)
  - [Partes de una cadena](#partes-de-una-cadena)
  - [Actividad](#actividad)
- [Operadores aritméticos](#operadores-aritméticos)
  - [Orden de operaciones](#orden-de-operaciones)
- [Operadores lógicos](#operadores-lógicos)
  - [Ejercicios](#ejercicios)

# Operadores en Python

Python ofrece muchas herramientas para realizar operaciones matemáticas y lógicas. Estas herramientas se conocen como **operadores** y permiten realizar **cálculos, comparaciones y manipulaciones** de variables.

En este apartado veremos:

- operadores aritméticos
- operadores de asignación
- operadores lógicos

## Operadores de asignación

Los operadores de asignación permiten asignar un valor a una variable.

**Asignación**

La asignación se puede realizar usando el operador `=`. Por ejemplo:

```python
a = 3
print(a) # imprime 3
```

**Adición**

La adición se puede realizar usando el operador `+=`. Por ejemplo:

```python
a = 3
a += 5
print(a) # imprime 8
```

**Sustracción**

La sustracción se puede realizar usando el operador `-=`. Por ejemplo:

```python
a = 3
a -= 5
print(a) # imprime -2
```

**Multiplicación**

La multiplicación se puede realizar usando el operador `*=`. Por ejemplo:

```python
a = 3
a *= 5
print(a) # imprime 15
```

**División**

La división se puede realizar usando el operador `/=`. Por ejemplo:

```python
a = 15
a /= 5
print(a) # imprime 3
```

# Operaciones con cadenas de caracteres

## Concatenación

El operador + permite concatenar cadenas de caracteres.

```python
cadena1 = "Hola"
cadena2 = "mundo"
cadena3 = cadena1 + " " + cadena2
print(cadena3)
```

## Repetición

Intenta hacer ‘Mamá’*5 a ver qué pasa…

## Partes de una cadena

También podemos obtener partes de un string. Para ello utilizaremos [ ]. Si dentro colocamos un número, nos dará la letra que ocupa esa posición.

```python
cadena1 = "Pikachu"
print(cadena1[0])
```

En informática, comenzamos a contar por el 0. Por lo tanto, la D ocupará la posición 0, y la a la posición 1, etc.

## Actividad

Crea un programa que te pida tu nombre y tus dos apellidos  uno a uno, los guarde en 3 variables y te pida por pantalla las iniciales. En mi caso, saldría por pantalla DMR.

# Operadores aritméticos

Los operadores aritméticos permiten realizar operaciones matemáticas básicas como sumar, restar, multiplicar y dividir.

**Suma**

La suma se puede realizar usando el operador `+`. Por ejemplo:

```python
a = 3
b = 4
c = a + b
print(c) # imprime 7
```

**Resta**

La resta se puede realizar usando el operador `-`. Por ejemplo:

```python
a = 3
b = 4
c = a - b
print(c) # imprime -1
```

**Multiplicación**

La multiplicación se puede realizar usando el operador `*`. Por ejemplo:

```python
a = 3
b = 4
c = a * b
print(c) # imprime 12
```

**División**

La división se puede realizar usando el operador `/`. Por ejemplo:

```python
a = 6
b = 3
c = a / b
print(c) # imprime 2
```

**Módulo**

El módulo se puede realizar usando el operador `%`. Por ejemplo:

```python
a = 7
b = 4
c = a % b
print(c) # imprime 3
```

## Orden de operaciones

Para las operaciones hay un orden de prevalencia, como en las matemáticas comunes, por lo cual debes tener cuidado y usar paréntesis, así como asegurarte de que lo que escribes funciona como deseas.

```python
print (3+4*2)
```
En este ejemplo, la multiplicación se hará en primer lugar, y después la suma.

# Operadores lógicos

Los operadores lógicos permiten realizar comparaciones entre variables y devolver un valor booleano.

**Igual**

La igualdad se puede comprobar usando el operador `==`. Por ejemplo:

```python
a = 3
b = 4
c = (a == b)
print(c) # imprime False
```

**No igual**

La desigualdad se puede comprobar usando el operador `!=`. Por ejemplo:

```
a = 3
b = 4
c = (a != b)
print(c) # imprime True
```

**Mayor que**

La comparación mayor que se puede comprobar usando el operador `>`. Por ejemplo:

```python
a = 3
b = 4
c = (a > b)
print(c) # imprime False
```

**Menor que**

La comparación menor que se puede comprobar usando el operador `<`. Por ejemplo:

```python
a = 3
b = 4
c = (a < b)
print(c) # imprime True
```

**Mayor o igual que**

La comparación mayor o igual que se puede comprobar usando el operador `>=`. Por ejemplo:

```python
a = 3
b = 4
c = (a >= b)
print(c) # imprime False
```

**Menor o igual que**

La comparación menor o igual que se puede comprobar usando el operador `<=`. Por ejemplo:

```python
a = 3
b = 4
c = (a <= b)
print(c) # imprime True
```

## Ejercicios

Crea un programa que te pida una contraseña. A continuación, te debería pedir que la vuelvas a escribir. Si las dos contraseñas escritas no coinciden, mostrar un mensaje informando de que las contraseñas introducidas no son iguales. Si coinciden, mostrar un mensaje informando que se ha cambiado la contraseña.