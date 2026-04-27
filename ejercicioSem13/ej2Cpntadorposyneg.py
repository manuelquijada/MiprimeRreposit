# Contador de positivos y negativos .

positivos = 0
negativos = 0

while True:
    numero = int(input("Ingrese un número, 0 para terminar: "))

    if numero == 0:
        break

    if numero > 0:
        positivos += 1
    else:
        negativos += 1

resumen = ["Positivos: " + str(positivos), "Negativos: " + str(negativos)]

for dato in resumen:
    print(dato)
