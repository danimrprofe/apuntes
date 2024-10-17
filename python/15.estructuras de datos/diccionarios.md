## Diccionarios

Los diccionarios son colecciones de pares clave-valor. Son útiles para mapear una clave única a un valor.

```python
#Creación
mi_diccionario = {'nombre': 'Juan', 'edad': 30}

# Adición y modificación de elementos:

mi_diccionario['ciudad'] = 'Madrid'  # Agrega una nueva clave-valor
mi_diccionario['edad'] = 31  # Modifica el valor asociado a la clave 'edad'

# Eliminación de elementos:
del mi_diccionario['ciudad']  # Elimina la clave 'ciudad'
valor = mi_diccionario.pop('edad')  # Elimina y devuelve el valor as
```