from baraja import Baraja
from mano import Mano

# 1. Creamos una baraja

mibaraja = Baraja()

# 2. Crear una mano

mano1 = Mano()

# 3. Mezclar baraja

mibaraja.mezclar()
mibaraja.mostrar()

# 4. Coger una carta de la baraja y ponerla en la mano

cartacogida = mibaraja.coger_carta()
mano1.añadir_carta(cartacogida)
mano1.mostrar_mano()

# 5. Mirar valor de la mano.

# Si valor > 21

# Sino seguir jugando o plantarse