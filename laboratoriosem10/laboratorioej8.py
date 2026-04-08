# menu principal


def menu(texto, num):
    if num == 1:
        return texto.upper()
    elif num == 2:
        return texto.lower()
    elif num == 3:
        return texto.capitalize()
    else:
        return "opcion invalida"


texto = input("Ingrese texto: ")

print("1. Mayusculas")
print("2. Minusculas")
print("3. Primera letra mayuscula")

op = int(input("Seleccione opcion: "))

print("Resultado:")
print(menu(texto, op))
