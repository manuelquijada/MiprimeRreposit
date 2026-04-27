# Numeros primos Rango

while True:
    n = int(input("Ingrese un número, 0 para salir: "))

    if n == 0:
        break

    for numero in range(1, n + 1):
        divisores = 0

        for i in range(1, numero + 1):
            if numero % i == 0:
                divisores += 1

        if divisores == 2:
            print(numero, "es primo")
