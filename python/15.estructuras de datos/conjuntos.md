## Conjuntos

Los conjuntos son colecciones **no ordenadas** de elementos **únicos**. Permiten realizar operaciones matemáticas como la unión, intersección y diferencia.

```python
mi_conjunto = {1, 2, 3}
# Adición de elementos:
mi_conjunto.add(4)  # Agrega el valor 4

# Eliminación de elementos:
mi_conjunto.remove(2)  # Elimina el valor 2

# Unión, intersección y diferencia:
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
union = conjunto1 | conjunto2  # {1, 2, 3, 4, 5}
interseccion = conjunto1 & conjunto2  # {3}
diferencia = conjunto1 - conjunto2  # {1, 2}
```