# Mostrar nombres con más de 5 caracteres


def nombres_largos(lista):
    print("Nombres con más de 5 caracteres:")

    for nombre in lista:
        if len(nombre) > 5:
            print(nombre)


nombres = []

for i in range(10):
    nombre = input("Ingrese un nombre: ")
    nombres.append(nombre)

nombres_largos(nombres)
