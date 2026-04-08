# contar caracteres del resultado


def cantidad(texto, num):
    if num == 1:
        texto = texto.upper()
    elif num == 2:
        texto = texto.lower()
    elif num == 3:
        texto = texto.capitalize()

    return len(texto)


print("Cantidad de letras:")
print(cantidad("hola mundo", 1))
