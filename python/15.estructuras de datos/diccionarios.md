# Diccionarios

Los diccionarios son colecciones de pares clave-valor. Son útiles para mapear una clave única a un valor.

```python
#Creación
mi_diccionario = {'nombre': 'Juan', 'edad': 30}
```

El diccionario está delimitado por llaves ``{}``. Dentro de estas llaves se definen los pares de **clave-valor**.

- ``'nombre'`` es la clave, y ``'Juan'`` es el valor asociado a esa clave.
- ``'edad'``es la clave, y ``30`` es el valor asociado a esa clave.

No puede haber claves duplicadas en un diccionario.

## Adición y modificación de elemento

```python
mi_diccionario['ciudad'] = 'Madrid'  # Agrega una nueva clave-valor
mi_diccionario['edad'] = 31  # Modifica el valor asociado a la clave 'edad'
```

## Eliminación de elementos

```python
del mi_diccionario['ciudad']  # Elimina la clave 'ciudad'
valor = mi_diccionario.pop('edad')  # Elimina y devuelve el valor as
```

## Ejemplo datos de una persona

```python
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
    "profesión": "Ingeniero"
}
print(persona["nombre"])  # Output: Juan
print(persona["profesión"])  # Output: Ingeniero
```

## Diccionario con tuplas

En este ejemplo, las claves son tuplas:

```python
distancias_entre_ciudades = {
    ("Madrid", "Barcelona"): 620,
    ("Paris", "Londres"): 344
}

print(distancias_entre_ciudades[("Madrid", "Barcelona")])
```
