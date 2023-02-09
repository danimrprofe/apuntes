from pokemon import Pokemon

pikachu = Pokemon("Pikachu", 5, "Eléctrico", 20, 20, 10, 5)
charmander = Pokemon("Charmander", 5, "Fuego", 20, 20, 8, 7)

print(pikachu)
print(charmander)


def pintar_stats(pokemon1, pokemon2):
    print(pokemon1.salud_actual, "/", pokemon1.salud_maxima,
          "------------------", pokemon2.salud_actual, "/", pokemon2.salud_maxima, )


while not (pikachu.está_derrotado() or charmander.está_derrotado()):
    pikachu.atacar_oponente(charmander)
    print(pikachu)
    print(charmander)
    if charmander.está_derrotado():
        break
    charmander.atacar_oponente(pikachu)
    print(pikachu)
    print(charmander)

if pikachu.está_derrotado():
    print("Pikachu ha sido derrotado.")
else:
    print("Charmander ha sido derrotado.")
