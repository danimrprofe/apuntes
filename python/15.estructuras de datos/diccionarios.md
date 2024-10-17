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

persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
    "profesión": "Ingeniero"
}

print(persona["nombre"])  # Output: Juan
print(persona["profesión"])  # Output: Ingeniero

Diccionario con tuplas:

distancias_entre_ciudades = {
    ("Madrid", "Barcelona"): 620,
    ("Paris", "Londres"): 344
}

print(distancias_entre_ciudades[("Madrid", "Barcelona")])

palabras = ["hola", "mundo", "hola", "python", "mundo", "mundo"]

contador = {}
for palabra in palabras:
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1

print(contador)  # Output: {'hola': 2, 'mundo': 3, 'python': 1}