import random

# número secreto
numero_secreto = random.randint(1, 10)

intentos = 0
max_intentos = 10
activo = True

while activo:
    numero = int(input("Adivina el número (1-10): "))
    intentos += 1

    if numero == numero_secreto:
        print("¡Lo lograste!")
        activo = False
    else:
        print("Intenta de nuevo")

    if intentos == max_intentos and numero != numero_secreto:
        print("Se acabaron los intentos. El número era:", numero_secreto)
        activo = False
