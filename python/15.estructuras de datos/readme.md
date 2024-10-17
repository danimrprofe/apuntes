# Estructuras de datos en Python

Las estructuras de datos son formas de organizar y almacenar datos en un programa de manera que puedan ser utilizados eficientemente. En Python, las principales estructuras de datos nativas incluyen

- listas
- tuplas
- conjuntos
- diccionarios

Cada una con características específicas que las hacen útiles para diferentes tareas.

## Array

un array es una estructura de datos que almacena elementos de un mismo tipo en una secuencia contigua de memoria.

```python
import array
mi_array = array.array('i', [1, 2, 3, 4, 5])  # 'i' indica que son enteros
print(mi_array[2])  # 3
mi_array.append(6)  # Agregar un elemento
```
