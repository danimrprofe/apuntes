import random

# Generar un número aleatorio entre 1 y 10
numero_aleatorio = random.randint(1, 10)

# Inicializar la adivinanza del usuario
adivinanza = 0

print("Adivina el número entre 1 y 10.")

# Bucle hasta que adivinen el número
while adivinanza != numero_aleatorio:
    adivinanza = int(input("Introduce tu adivinanza: "))

    if adivinanza < numero_aleatorio:
        print("Demasiado bajo.")
    elif adivinanza > numero_aleatorio:
        print("Demasiado alto.")
    else:
        print("¡Felicidades! Has adivinado el número.")