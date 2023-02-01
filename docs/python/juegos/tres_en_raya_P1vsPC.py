import random

def juego_3_en_raya():
    tablero = [" " for x in range(9)]
    turno = "X"
    contador = 0
    libres = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    def imprimir_tablero():
        print()
        print("| {} | {} | {} |".format(tablero[0], tablero[1], tablero[2]))
        print("| {} | {} | {} |".format(tablero[3], tablero[4], tablero[5]))
        print("| {} | {} | {} |".format(tablero[6], tablero[7], tablero[8]))
        print()

    while True:
        imprimir_tablero()

        # Turno del jugador

        eleccion = int(input("Elige una casilla (1-9): ".format(turno)))
        if eleccion not in libres:
            print("casilla no válida")
            continue

        if tablero[eleccion - 1] == " ":
            tablero[eleccion - 1] = turno
            libres.remove(eleccion)
            contador += 1
        else:
            print("Casilla ocupada, elige otra.")
            continue

        # No puede haber un ganador antes del quinto turno

        if contador >= 5:
            if (tablero[0] == tablero[1] == tablero[2] != " ") or \
               (tablero[3] == tablero[4] == tablero[5] != " ") or \
               (tablero[6] == tablero[7] == tablero[8] != " ") or \
               (tablero[0] == tablero[3] == tablero[6] != " ") or \
               (tablero[1] == tablero[4] == tablero[7] != " ") or \
               (tablero[2] == tablero[5] == tablero[8] != " ") or \
               (tablero[0] == tablero[4] == tablero[8] != " ") or \
               (tablero[2] == tablero[4] == tablero[6] != " "):
                imprimir_tablero()
                print("¡Jugador {} gana!".format(turno))
                break

        # Turno del ordenador

        eleccion = random.choice(libres)
        print("Ordenador elige casilla ", eleccion)
        tablero[eleccion - 1] = "O"
        libres.remove(eleccion)
        contador += 1

    if input("¿Quieres jugar de nuevo? (s/n)").lower() == "s":
        juego_3_en_raya()

juego_3_en_raya()
