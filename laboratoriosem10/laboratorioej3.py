# pedir datos al usuario


def cambiar(texto, num):
    if num == 1:
        return texto.upper()
    elif num == 2:
        return texto.lower()
    elif num == 3:
        return texto.capitalize()


t = input("Ingrese texto: ")
n = int(input("Ingrese numero: "))

print("El resultado es:")
print(cambiar(t, n))
