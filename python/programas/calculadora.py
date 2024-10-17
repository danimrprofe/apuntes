def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: División por cero no permitida"
    return a / b

# Entrada de usuario
print("Selecciona operación:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

eleccion = input("Introduce tu elección (1/2/3/4): ")
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

if eleccion == '1':
    print(f"El resultado es: {sumar(num1, num2)}")
elif eleccion == '2':
    print(f"El resultado es: {restar(num1, num2)}")
elif eleccion == '3':
    print(f"El resultado es: {multiplicar(num1, num2)}")
elif eleccion == '4':
    print(f"El resultado es: {dividir(num1, num2)}")
else:
    print("Elección no válida")