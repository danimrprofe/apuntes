# Listas

Las listas son colecciones **ordenadas y mutables** que permiten almacenar elementos de cualquier tipo de dato. Son una de las estructuras más flexibles y ampliamente usadas en Python.

```python
mi_lista = [1, 2, 3, 4, 5]

# Adición de elementos:
mi_lista.append(6)  # Agrega un elemento al final
mi_lista.insert(2, 10)  # Inserta el número 10 en la posición 2

# Eliminación de elementos:
mi_lista.remove(3)  # Elimina el primer valor igual a 3
elemento = mi_lista.pop(1)  # Elimina y devuelve el elemento en la posición 1
del mi_lista[0]  # Elimina el primer elemento de la lista

# Ordenación
mi_lista.sort()
```

Ejemplo: crear lista de cuadrados

```python
squares = []
for x in range(10):
     squares.append(x**2)
```

### Usando listas como pilas

Las listas pueden funcionar como **pilas** (estructura **LIFO**: Last In, First Out). El último elemento que se añade es el primero que se retira.

```python
pila = []
pila.append('a')
pila.append('b')
elemento = pila.pop()  # Devuelve y elimina 'b'
```

### Usando listas como colas

Para usar listas como colas (**FIFO**: First In, First Out), donde el primer elemento que entra es el primero que sale, es más eficiente utilizar la colección deque de la librería collections.

```python
from collections import deque
cola = deque([1, 2, 3])
cola.append(4)  # Agrega 4 al final de la cola
primero = cola.popleft()  # Elimina y devuelve el primer elemento (1)
```

###  La instrucción del

La instrucción del se utiliza para eliminar elementos de una estructura de datos o borrar variables.

```python
lista = [1, 2, 3, 4, 5]
del lista[2]  # Elimina el tercer elemento
del lista  # Elimina la variable lista
```