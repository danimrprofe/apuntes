# Import

En Python, el uso de import permite incluir módulos o archivos en tu programa. A continuación, te muestro un ejemplo simple utilizando dos archivos.

Estructura de archivos
Imagina que tienes la siguiente estructura de archivos:

```
Copiar código
proyecto/
│
├── main.py
└── funciones.py
```

Este archivo contiene algunas funciones simples.

```python
# funciones.py
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b
```

Contenido de main.py
En este archivo, importamos las funciones definidas en funciones.py y las utilizamos.

## main.py

```python
# Importar las funciones del archivo funciones.py
from funciones import sumar, restar

# Usar las funciones importadas
resultado_suma = sumar(5, 3)
resultado_resta = restar(5, 3)

print(f"La suma de 5 y 3 es: {resultado_suma}")
print(f"La resta de 5 y 3 es: {resultado_resta}")
```
