# ejercicio para cambiar texto


def texto(texto, num):
    if num == 1:
        return texto.upper()
    elif num == 2:
        return texto.lower()
    elif num == 3:
        return texto.capitalize()


print(texto("hola mundo", 1))
