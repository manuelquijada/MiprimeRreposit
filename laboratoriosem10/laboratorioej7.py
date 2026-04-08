# aplicar varios cambios al texto


def transformar(texto, lista):
    for num in lista:
        if num == 1:
            texto = texto.upper()
        elif num == 2:
            texto = texto.lower()
        elif num == 3:
            texto = texto.capitalize()

    return texto


print("Resultado final:")
print(transformar("hola mundo", [1, 2, 3]))
