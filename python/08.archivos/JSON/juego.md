# Práctica archivo configuración JSON

En este ejemplo veremos como utilizar JSON para almacenar la configuración y los datos de partidas, de forma que queden guardadas en un archivo cuando el programa termine, y podamos cargarlos de nuevo cuando el programa vuelva a abrirse para utilizar estos datos.

Además del archivo Python con el juego, crearemos un archivo de texto ``config.json`` en el cual guardaremos toda la información que necesitemos.

![](img/2025-02-04-18-12-32.png)

El contenido del archivo .json será el siguiente.

```JSON
{
    "usuario": "Dani",
    "dificultad": 10,
    "victorias": 2,
    "derrotas": 0
}
```

El archivo Python quedará tal que así:
```python
import json
import random
import os

# Nombre del archivo JSON donde guardaremos los parámetros
CONFIG_FILE = "config.json"

# Función para guardar los parámetros en un archivo JSON
def guardar_configuracion(data, filename=CONFIG_FILE):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
    print(f"Configuración guardada en {filename}")

# Función para leer los parámetros desde un archivo JSON
def cargar_configuracion(filename=CONFIG_FILE):
    if os.path.exists(filename):  # Verifica si el archivo exist
        with open(filename, "r") as file:
            return json.load(file)
    else:
        print("Veo que es tu primera vez.")
        nombre = input("¿Cómo te llamas?")
        config_data = {}
        config_data["usuario"] = nombre
        config_data["dificultad"] = 10
        config_data["victorias"] = 0
        config_data["derrotas"] = 0
        return config_data  # Retorna valores por defecto si el archivo no existe

config_data = cargar_configuracion()

print("Bienvenido",config_data["usuario"],"Qué deseas hacer")
print("1.Jugar")
print("2.Cambiar dificultad")
accion = int(input())
if accion == 2:
    dificultad = config_data["dificultad"]
    print("La dificultad actual es:",dificultad)
    dificultad = int(input("Elige nueva dificultad (1-5)"))
    print("Has cambiado a dificultad:",dificultad)
    config_data["dificultad"] = dificultad
    # Guardar la configuración inicial
    guardar_configuracion(config_data)
elif accion == 1:
    numero = random.randint(1,10)
    print("🎲 Adivina un número del 1 al 10. Tienes 3 intentos.")
    for intento in range(1, 4):
        numero_elegido = int(input(f"Intento {intento}: "))
        if numero_elegido == numero:
            print(f"🎉 ¡Felicidades! Adivinaste el número {numero} en {intento} intentos.")
            config_data["victorias"] = config_data["victorias"] +1
            break
        elif numero_elegido < numero:
            print("📉 El número es mayor.")
        else:
            print("📈 El número es menor.")

        # Si es el último intento y no acertó, muestra el número correcto
        if intento == 3:
            print(f"❌ Has perdido. El número era {numero}.")
            config_data["derrotas"] = config_data["derrotas"] +1
    guardar_configuracion(config_data)

```