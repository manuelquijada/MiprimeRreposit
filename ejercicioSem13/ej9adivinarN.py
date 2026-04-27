# Adivinar numero

import random

numero_secreto = random.randint(1, 10)
intentos = []

while True:
    numero = int(input("Adivine el número del 1 al 10: "))
    intentos.append(numero)

    if numero == numero_secreto:
        print("Adivinaste el número")
        break
    elif numero < numero_secreto:
        print("El número secreto es mayor")
    else:
        print("El número secreto es menor")

for intento in intentos:
    print("Intento realizado:", intento)
