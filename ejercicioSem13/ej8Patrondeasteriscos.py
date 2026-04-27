# Patron de asteriscos

while True:
    n = int(input("Ingrese un número, 0 para salir: "))

    if n == 0:
        break

    for i in range(1, n + 1):
        if i % 2 != 0:
            print("*" * i)
