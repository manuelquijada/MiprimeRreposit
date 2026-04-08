# transformar lista de palabras


def lista_palabras(lista, num):
    nueva = []

    for i in lista:
        if num == 1:
            nueva.append(i.upper())
        elif num == 2:
            nueva.append(i.lower())
        elif num == 3:
            nueva.append(i.capitalize())

    return nueva


print("Lista transformada:")
print(lista_palabras(["hola", "MUNDO", "python"], 2))
