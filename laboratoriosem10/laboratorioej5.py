# validar opcion


def cambiar(texto, num):
    if num == 1:
        return texto.upper()
    elif num == 2:
        return texto.lower()
    elif num == 3:
        return texto.capitalize()
    else:
        return "opcion invalida"


print(cambiar("hola", 5))
