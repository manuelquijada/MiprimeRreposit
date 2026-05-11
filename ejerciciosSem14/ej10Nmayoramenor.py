# Ordenar números de menor a mayor


def ordenar(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux

    return lista


numeros = []

for i in range(6):
    num = int(input("Ingrese un número: "))
    numeros.append(num)

print("Lista ordenada:", ordenar(numeros))
