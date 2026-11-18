# Escritura en un archivo
with open("archivo.txt", "w") as archivo:
    archivo.write("Este es un archivo de ejemplo.\n¡Hola, Mundo!")

# Lectura del archivo
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()

print("Contenido del archivo:")
print(contenido)