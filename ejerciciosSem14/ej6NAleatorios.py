# Números aleatorios mayores a 50

import random


def mayores_50(lista):
    contador = 0

    for numero in lista:
        if numero > 50:
            contador += 1

    return contador


numeros = []

for i in range(10):
    numeros.append(random.randint(1, 100))

print("Números generados:", numeros)

print("Cantidad mayores a 50:", mayores_50(numeros))
