# Listas

Los objetos que almacenan otros objetos se llaman **colecciones**. Las más sencillas son las listas.

Las **listas** son un tipo de dato en Python que le permite almacenar un conjunto de elementos de manera ordenada y acceder a ellos mediante un **índice**. Las listas son una de las estructuras de datos más útiles y versátiles en Python.

## Crear una Lista

Para crear una lista, use corchetes [] para encerrar una lista de elementos separados por comas. Aquí hay un ejemplo de cómo crear una lista en Python:

```python
# Crear una lista
mi_lista = [1, 2, 3, 4]
```

## Agregar elementos a una lista

Puede agregar elementos a una lista existente usando el método `.append()`:

```python
# Agregar un elemento a la lista
mi_lista.append(5)
```

## Acceder a elementos de una lista

Puede acceder a los elementos de una lista mediante su índice, que comienza en 0. Por ejemplo, para obtener el primer elemento de la lista anterior, usaríamos el siguiente código:

```python
# Obtener el primer elemento de la lista
primer_elemento = mi_lista[0]
```

Mostrar los dos primeros elementos:

```python
alumnos[2:]
```

## Iterar sobre una lista

También puedes iterar sobre los elementos de una lista usando un bucle `for`. Aquí hay un ejemplo de cómo imprimir todos los elementos de una lista:

```python
# Imprimir todos los elementos de la lista
for elemento in mi_lista:
    print(elemento)
```

## Longitud de una lista

Puede obtener el número de elementos de una lista usando la función predefinida `len()`:

```python
# Obtener la longitud de la lista
longitud = len(mi_lista)
```

## Eliminar elementos de una lista

Puede eliminar elementos de una lista usando la función predefinida `del`:

```python
# Eliminar el tercer elemento de la lista
del mi_lista[2]
```

Eliminar el último elemento:

```python
del alumnos[-1]
```

## Ordenar

Podemos ordenar a los alumnos por orden alfabético:

```python
alumnos.sort()
```

```python
'''Ejemplo de uso de un método de las listas'''
nombres=['Paco','María','Raquel']
#al definir nombres como una lista, ya puedo llamar a
cualquiera de los métodos que se aplican sobre listas.
#vamos a añadir un elemento al final de la lista
print('Lista previa')
print(nombres)

print('El primer elemento es:')
print(nombres[0])

print('Dame el elemento a añadir')
nuevo = input()
nombres.append(nuevo) #añade elemento al final
print('Lista después de añadir un elemento')
print(nombres)
#fíjate que el método se llama en la lista concreta sobre la
que se quiere usar, NO se pone lista.append, sino
nombres.append
print('Lista previa')
print(nombres)
print('Dame el elemento a insertar')
nuevo = input()
print('Dame la posición de inserción')
posicion = int(input())
nombres.insert(posicion,nuevo) #inserta elemento en la posición dada, ojo a la numeración que empieza por cero
print(nombres)

#de nuevo llamamos al método con el objeto concreto que usamos
```