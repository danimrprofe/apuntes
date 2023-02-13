# 1º bachillerato PDF 22-23

# Crear tablero

tablero = [" "," "," "," "," "," "," "," "," " ]

def pintar_tablero():
    print("|", tablero[0] ,"|", tablero[1] ,"|", tablero[2], "|")
    print("|", tablero[3] ,"|", tablero[4] ,"|", tablero[5], "|")
    print("|", tablero[6] ,"|", tablero[7] ,"|", tablero[8], "|")

pintar_tablero()

seguir_partida = True
turnos = 0

while seguir_partida:
    # pedir jugador 1

    casilla = int(input("elige una casilla: "))

    # Mirar si está ocupada

    if tablero[casilla] == "X" or tablero[casilla] == "O":
        print("esta casilla está ocupada")
    else:
        tablero[casilla] = "X"
        turnos = turnos + 1
        print(turnos)

    pintar_tablero()
    if turnos == 9:
        break

    if  tablero[0] == tablero[1] == tablero[2] != " " or \
        tablero[3] == tablero[4] == tablero[5] != " " or \
        tablero[6] == tablero[7] == tablero[8] != " " or \
        tablero[0] == tablero[3] == tablero[6] != " " or \
        tablero[1] == tablero[4] == tablero[7] != " " or \
        tablero[2] == tablero[5] == tablero[8] != " " or \
        tablero[0] == tablero[4] == tablero[8] != " " or \
        tablero[2] == tablero[4] == tablero[6] != " ":
        print("Ha ganado jugador 1")
        break


    # pedir jugador 2

    casilla = int(input("elige una casilla: "))

    # Mirar si está ocupada

    if tablero[casilla] == "X" or tablero[casilla] == "O":
        print("esta casilla está ocupada")
    else:
        tablero[casilla] = "O"
        turnos = turnos + 1
        print(turnos)

    pintar_tablero()

    if  tablero[0] == tablero[1] == tablero[2] != " " or \
        tablero[3] == tablero[4] == tablero[5] != " " or \
        tablero[6] == tablero[7] == tablero[8] != " " or \
        tablero[0] == tablero[3] == tablero[6] != " " or \
        tablero[1] == tablero[4] == tablero[7] != " " or \
        tablero[2] == tablero[5] == tablero[8] != " " or \
        tablero[0] == tablero[4] == tablero[8] != " " or \
        tablero[2] == tablero[4] == tablero[6] != " ":
        print("Ha ganado jugador 1")
        break

print("fin de la partida")
