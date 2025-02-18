# Manual Básico de Python

## ¿Qué es Python?

Python es un lenguaje de programación fácil de aprender y muy utilizado en diferentes áreas como desarrollo web, ciencia de datos y automatización. Su sintaxis simple lo hace ideal para principiantes.

## Estructura de un programa en Python

Un programa en Python es un conjunto de instrucciones que se ejecutan en orden de arriba hacia abajo. Estas instrucciones pueden ser:

- Declaraciones de variables
- Condicionales (`if`, `elif`, `else`)
- Bucles (`while`, `for`)
- Funciones (`def`)

Ejemplo de un programa básico en Python:

```python
nombre = input("¿Cómo te llamas? ")
print("Hola, " + nombre)

edad = int(input("¿Cuántos años tienes? "))
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
```

## 1. Mostrar mensajes con print()

La función `print()` nos permite mostrar información en la pantalla.

```python
print("Hola, bienvenido a Python!")
```

## 2. Variables

Las variables almacenan datos en memoria. No necesitan declaración de tipo.

```python
nombre = "Juan"  # Variable de tipo cadena
edad = 25  # Variable de tipo entero
altura = 1.75  # Variable de tipo flotante
es_estudiante = True  # Variable booleana
```

Las variables se pueden llamar desde cualquier punto del programa.

Podemos hacer diferentes operaciones con las variables:

```python
x = 10
y = 5
suma = x + y  # Resultado: 15
resta = x - y  # Resultado: 5
multiplicacion = x * y  # Resultado: 50
division = x / y  # Resultado: 2.0
print(suma, resta, multiplicacion, division)
```

## 3. Entrada de datos con input()

Podemos pedir información al usuario con `input()`. El valor ingresado siempre será una cadena, por lo que si necesitamos un número, debemos convertirlo con `int()` o `float()`.

```python
nombre = input("¿Cómo te llamas? ")
print("Hola, " + nombre)

edad = int(input("¿Cuántos años tienes? "))
print("Tendrás", edad + 1, "el próximo año.")
```

## 4. Condicionales (if, elif, else)

Permiten ejecutar diferentes bloques de código según condiciones.

```python
edad = 18
if edad >= 18:
    print("Eres mayor de edad")
elif edad >= 13:
    print("Eres adolescente")
else:
    print("Eres niño")
```

### Uso de AND en condicionales

```python
edad = 25
ingresos = 3000
if edad > 18 and ingresos > 2000:
    print("Eres adulto y tienes buenos ingresos")
```

### Uso de OR en condicionales

```python
es_estudiante = False
tiene_descuento = True
if es_estudiante or tiene_descuento:
    print("Puedes acceder al descuento")
```

## 5. Bucles

### **while**: Se ejecuta mientras una condición sea verdadera.

```python
contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1
```

### **for**: Itera sobre una secuencia (lista, rango, cadena, etc.).

```python
for i in range(5):
    print("Valor:", i)
```

### **Listas y cómo recorrerlas**

Las listas almacenan varios valores en una sola variable y podemos recorrerlas con un bucle `for`.

```python
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print("Me gusta la", fruta)
```

## 6. Funciones

Permiten reutilizar código agrupando instrucciones.

```python
def saludar(nombre):
    return "Hola, " + nombre

print(saludar("Ana"))
```

Las funciones pueden tener múltiples parámetros y valores de retorno:

```python
def operar(a, b):
    suma = a + b
    resta = a - b
    return suma, resta

resultado_suma, resultado_resta = operar(10, 5)
print(resultado_suma, resultado_resta)  # Imprime: 15 5
```

## 7. Comentarios

Sirven para documentar el código y no se ejecutan.

```python
# Esto es un comentario de una línea
"""
Esto es un comentario
multilínea
"""
```

Este manual cubre lo esencial para empezar con Python. ¡Practica y sigue aprendiendo!
