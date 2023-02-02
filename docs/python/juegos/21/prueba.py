from carta import Carta
from baraja import Baraja
from mano import Mano

cartaprueba = Carta("tréboles", 2)

mibaraja = Baraja()
print(mibaraja.contar())

print(mibaraja.quedan_cartas())

mibaraja.barajar()

mano_dani = Mano()

mano_dani.añadir_carta(mibaraja.sacar_carta())
mano_dani.añadir_carta(mibaraja.sacar_carta())
mano_dani.añadir_carta(mibaraja.sacar_carta())

mano_dani.mostrar_mano()
