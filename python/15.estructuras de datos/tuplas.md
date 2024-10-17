# Tuplas y secuencias

Las tuplas son colecciones **ordenadas** pero **inmutables**, lo que significa que no se pueden modificar después de su creación. Son útiles cuando se necesita una secuencia constante de elementos.

```python
mi_tupla = (1, 2, 3, 4)
```

Para acceder a un elemento:

```python
valor = mi_tupla[1]  # Devuelve 2
```
Como las tuplas son inmutables, no es posible agregar ni eliminar elementos directamente. Si se necesita modificar una tupla, se debe crear una nueva tupla a partir de la existente.

## Ejemplos

- Coordenadas: (34.0522, -118.2437)  # Latitud y longitud
- Posiciones: punto_2D = (10, 20), punto_3D = (5, -4, 8)
- colores = ('rojo', 'verde', 'azul')
- tamaños = ('S', 'M', 'L')