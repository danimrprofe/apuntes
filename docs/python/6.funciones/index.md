# Funciones

Las funciones son una forma de organizar el código y las tareas en Python. Para crear una función, se usa la palabra clave def seguida por el nombre de la función y los parámetros entre paréntesis. A continuación, se escribe el cuerpo de la función, que es el código que se ejecutará cuando se llame a la función. Finalmente, se debe retornar el resultado de la función con la palabra clave return.

Ejemplo:

```python
def saludar (nombre):
  saludo = "Hola " + nombre
  return saludo

print(saludar("Juan")) # Imprime "Hola Juan"
```