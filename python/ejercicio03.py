# Pido una frase
frase = input("Escribe una frase: ")

# Quito los espacios
sin_espacios = frase.replace(" ", "")

# Cuento las letras sin espacios
print("Cantidad de letras sin espacios:", len(sin_espacios))
