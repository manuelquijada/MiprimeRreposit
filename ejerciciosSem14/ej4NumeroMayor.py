# Encontrar el número mayor


def numero_mayor(lista):
    mayor = lista[0]

    for numero in lista:
        if numero > mayor:
            mayor = numero

    return mayor


numeros = []

for i in range(8):
    num = int(input("Ingrese un número: "))
    numeros.append(num)

print("El número mayor es:", numero_mayor(numeros))
