import random


def jugar_partida():
    print("Vamos a jugar piedra, papel o tijeras!")
    opciones = ["piedra", "papel", "tijeras"]
    eleccion_jugador = input("Elige piedra, papel o tijeras: ").lower()
    eleccion_computadora = random.choice(opciones)
    print(f"La computadora eligió {eleccion_computadora}.")
    if eleccion_jugador == eleccion_computadora:
        print("Empate!")
    elif eleccion_jugador == "piedra" and eleccion_computadora == "tijeras":
        print("Ganaste!")
    elif eleccion_jugador == "papel" and eleccion_computadora == "piedra":
        print("Ganaste!")
    elif eleccion_jugador == "tijeras" and eleccion_computadora == "papel":
        print("Ganaste!")
    else:
        print("Perdiste!")
    play_again = input("¿Quieres jugar de nuevo? (s/n) ").lower()
    if play_again == 's':
        jugar_partida()
    else:
        print("Gracias por jugar!")


if __name__ == '__main__':
    jugar_partida()
