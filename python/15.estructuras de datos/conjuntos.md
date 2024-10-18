# Conjuntos

Los conjuntos son colecciones **no ordenadas** de elementos **únicos**. Se definen entre llaves, ``{}``, separando sus elementos por comas.

```python
mi_conjunto = {1, 2, 3}
# Adición de elementos:
mi_conjunto.add(4)  # Agrega el valor 4

# Eliminación de elementos:
mi_conjunto.remove(2)  # Elimina el valor 2
```

Los elementos de los conjuntos no quedan ordenados según se agregan. Permiten realizar operaciones matemáticas como la unión, intersección y diferencia.

## Unión, intersección y diferencia

Los conceptos de unión, intersección y diferencia son fundamentales en la teoría de conjuntos y en muchas otras áreas como bases de datos y programación

### Unión (∪)

Dados estos dos conjuntos de números:

![](img/2024-10-18-08-03-04.png)

La unión de dos conjuntos 𝐴 y 𝐵 B es un conjunto que contiene todos los elementos de  𝐴
A, de 𝐵 B, o de ambos. No se repiten los elementos.

![](img/2024-10-18-08-05-54.png)

### Intersección (∩)

La intersección de dos conjuntos 𝐴 y 𝐵 es un conjunto que contiene solo los elementos que están tanto en  𝐴 como en 𝐵.

![](img/2024-10-18-08-03-38.png)

### Diferencia (−)

La diferencia entre dos conjuntos  𝐴 y  𝐵 es un conjunto que contiene los elementos que están en  𝐴
A, pero no en 𝐵.

La diferencia 𝐴 − 𝐵 sería:

![](img/2024-10-18-08-04-23.png)

Y la diferencia 𝐵 − 𝐴 sería:

![](img/2024-10-18-08-04-33.png)

Ejemplos:

```python
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}
union = conjunto1 | conjunto2  # {1, 2, 3, 4, 5}
interseccion = conjunto1 & conjunto2  # {3}
diferencia = conjunto1 - conjunto2  # {1, 2}
```
