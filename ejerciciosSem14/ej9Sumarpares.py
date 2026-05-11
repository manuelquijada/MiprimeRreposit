# Suma de números pares


def suma_pares(lista):
    suma = 0

    for numero in lista:
        if numero % 2 == 0:
            suma += numero

    return suma


numeros = []

for i in range(6):
    num = int(input("Ingrese un número: "))
    numeros.append(num)

print("Suma de números pares:", suma_pares(numeros))
