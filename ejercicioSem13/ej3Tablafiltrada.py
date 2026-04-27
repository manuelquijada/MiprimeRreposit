# Tabla filtrada

while True:
    numero = int(input("Ingrese un número, -1 para salir: "))

    if numero == -1:
        break

    for i in range(1, 11):
        resultado = numero * i

        if resultado > 20:
            print(numero, "x", i, "=", resultado)
