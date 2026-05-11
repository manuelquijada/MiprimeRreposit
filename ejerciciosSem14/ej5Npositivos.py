# Mostrar números positivos


def positivos(lista):
    nueva_lista = []

    for numero in lista:
        if numero > 0:
            nueva_lista.append(numero)

    return nueva_lista


numeros = []

for i in range(6):
    num = int(input("Ingrese un número: "))
    numeros.append(num)

print("Números positivos:", positivos(numeros))
