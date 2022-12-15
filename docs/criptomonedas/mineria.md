# Minería

- El minado es una validación de las transacciones.
- Por este esfuerzo, los mineros obtienen dinero como recompensa.
- Esta recompensa disminuye las tarifas, creando un incentivo complementario para contribuir al poder de procesamiento de la red.

## Progreso de la minería

- Creación máquinas especializadas como FPGAs y ASICs.
- Carrera por construir máquinas más baratas y eficientes
- Incremento en el número de mineros aumenta complejidad de la generación de hashes
- Mineros invierten grandes cantidades de dinero en máquinas especializadas.

![](img/2022-11-06-22-55-30.png)

## Recompensas

- El sistema se sostiene gracias a recompensas. Las transacciones y los bloques dan recompensas.
- Los mineros dedican potencia de ordenadores a crear bloques a cambio de la posibilidad de ganar dinero
- Para este minado se necesita cada vez más potencia de computación

La primera recompensa fue de 50 bitcoin y fue a parar a la dirección:

```
1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa
```

![](img/2022-11-06-22-55-36.png)

## El reto

El sistema de Bitcoin intenta crear bloques de forma regular cada diez minutos aproximadamente. Para ello, se establece un reto de dificultad que debe ser resuelto mediante criptografía. Esta criptografía consiste en generar un código **hash** específico mediante información del bloque actual y del bloque anterior.

El código hash del bloque génesis fue:
```
000000000019d6689c085ae165831e934ff763ae46a2a6c172b3f1b60a8ce26f
```

Esta tarea es relativamente fácil en sí misma, y para **aumentar la dificultad** se requiere que el hash cumpla con una condición previamente establecida. Esto se consigue aumentando el número de pruebas necesarias hasta encontrar un hash válido. Para adaptar la dificultad según el aumento de la potencia de los ordenadores, se ajusta la condición del hash a una más exigente. El parámetro que hay que variar para conseguir el hash válido se conoce como nonce.

## Crear el hash

Los **hashes** se generan para cada bloque de una cadena de bloques a partir de la información del bloque actual y el anterior. Esta información se usa para encontrar un código hash específico que identifique el bloque. Generar este código hash requiere una cantidad de tiempo relativamente pequeña, sin embargo hay que cumplir una condición para que el hash sea válido. Esto requiere un proceso de prueba-error con el parámetro **nonce** para lograrlo. Al igual que la potencia computacional, la dificultad para encontrar un hash válido aumenta incrementando la condición necesaria para hallarlo.

Videos interesantes

- http://www.youtube.com/watch?v=44D9nVxqGIE
- http://www.youtube.com/watch?v=YBNr69vrscw