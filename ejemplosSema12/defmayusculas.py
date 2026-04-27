def validar_mayusculas(nombre):
    # "Esta función verifica si el nombre está en mayúsculas"

    if nombre.isupper():
        return True
    else:
        return False


# Ejemplo de uso
nombre = input("Ingresa un nombre: ")

resultado = validar_mayusculas(nombre)

print(resultado)
