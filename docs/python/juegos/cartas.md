# Juegos de cartas

Vamos a introducir el concepto de programación orientada a objetos utilizando un juego de cartas.

Para ello, vamos a crear los siguientes objetos:

- Carta
- Baraja (conjunto de 52 cartas diferentes)
- Mano (conjunto de cartas de un jugador en una partida)

## Clase Carta

Comenzaremos creando la clase ``Carta``. Cada carta tendrá dos propiedades, el ``palo`` (tréboles, corazones) y el ``valor`` (7,8, as, etc.).

- También tendremos 2 métodos: el primero de ellos es el ``constructor``, que será el encargado de crear el objeto
- El segundo es el método que nos ofrecerá una representación del objeto en formato de texto al hacer ``print()`` sobre el objeto.

```python
class Carta:
    def __init__(self, palo, valor):
        self.palo = palo
        self.valor = valor

    def __repr__(self):
        return f"{self.valor} de {self.palo}"
```

Si utilizamos la clase en el mismo archivo, podemos crear objetos del tipo ``Carta`` de la siguiente forma:

- La primera línea llamará al método ``__init__`` (constructor)de la clase.
- La segunda línea llamará al método ``__repr__`` para imprimir información sobre la carta.

```python
cartaprueba = Carta("tréboles", 2)
print(cartaprueba)
```

Guardaremos la clase ``Carta`` en un archivo ``carta.py``. Si queremos utilizar esta clase dentro de otro archivo, tendremos que importarla en primer lugar.

```python
from carta import Carta
cartaprueba = Carta("tréboles", 2)
print(cartaprueba)
```

## Clase baraja

La baraja de póker se compone de 52 cartas. Para ello crearemos la clase ``Baraja`` lo tanto, contendrá 52 objetos ``Carta``.

- El método constructor nos creará una lista de cartas con todas las combinaciones posibles. ``Baraja.cartas`` contendrá una lista de objetos ``Carta``.
- ``Baraja.barajar()`` mezclará las cartas de la baraja
- ``Baraja.contar()`` nos dirá cuantas cartas quedan en la baraja
- ``Baraja.sacar_carta()`` nos devolverá un objeto ``Carta`` de ``Baraja.cartas``.
- ``Baraja.contar()`` nos dirá cuantas cartas quedan en la baraja
- ``Baraja.quedan_cartas()`` devolverá ``True`` en caso de que queden cartas en la lista ``Baraja.cartas``. En caso contrario, ``False``.

```python
import random
from carta import Carta

class Baraja:
    def __init__(self):
        self.cartas = []
        palos = ["♥", "♦", "♣", "♠"]
        valores = ["As", "2", "3", "4", "5", "6", "7",
                   "8", "9", "10", "Jota", "Reina", "Rey"]
        for palo in palos:
            for valor in valores:
                self.cartas.append(Carta(palo, valor))

    def barajar(self):
        random.shuffle(self.cartas)

    def __repr__(self):
        return f"Baraja de {self.contar()} cartas"

    def contar(self):
        return len(self.cartas)

    def sacar_carta(self):
        if len(self.cartas) > 0:
            return self.cartas.pop()
        else:
            return None

    def quedan_cartas(self):
        """Devuelve True si quedan cartas en la baraja, False si no."""
        return len(self.cartas) != 0

    def mostrar_cartas(self):
        for carta in self.cartas:
            print(carta)
```

Para probar este nuevo objeto podemos hacer lo siguiente:

```python
mibaraja = Baraja()
print("La baraja tiene", mibaraja.contar(), " cartas")
print(mibaraja.quedan_cartas())
# Sacar todas las cartas de la baraja

while mibaraja.quedan_cartas():
    print(mibaraja.sacar_carta(),  " La baraja tiene",
          mibaraja.contar(), " cartas")

mibaraja.barajar()
```

## Clase Mano

En la clase ``Mano`` guardaremos las cartas que tiene cada jugador durante una partida concreta.

- Agregaremos objetos ``Carta`` a la lista ``Mano.cartas`` mediante el método ``añadir_carta()``.
- Con el método ``mostrar_mano`` mostraremos todos los objetos ``Carta`` de ``Mano.cartas``.
- ``calcular_valor`` nos dirá el valor que suman todas las cartas de nuestra mano.

```python
# Esta clase define el objeto Mano, el cual representa un conjunto de cartas.
class Mano:

    # El método __init__ establece la lista de cartas como una lista vacía y el valor como 0.
    def __init__(self):
        self.cartas = []
        self.valor = 0

    # El método añadir_carta añade una carta a la lista de cartas.
    def añadir_carta(self, carta):
        self.cartas.append(carta)

    def calcular_valor(self):
        self.valor = 0

        for carta in self.cartas:
            if carta.valor in ["Jota", "Reina", "Rey"]:
                self.valor += 10
            elif carta.valor == "As":

                self.valor += 11
            else:
                self.valor += int(carta.valor)

        return self.valor

    def mostrar_mano(self):
        for carta in self.cartas:
            print(carta)
```

Pruebas:

```python
from baraja import Baraja
from mano import Mano

mibaraja = Baraja()
mibaraja.barajar()

mano_J1 = Mano()

if mibaraja.quedan_cartas():
    mano_J1.añadir_carta(mibaraja.sacar_carta())
    mano_J1.añadir_carta(mibaraja.sacar_carta())
    mano_J1.añadir_carta(mibaraja.sacar_carta())

mano_J1.mostrar_mano()

print("En la baraja quedan", mibaraja.contar(), "cartas")
```
