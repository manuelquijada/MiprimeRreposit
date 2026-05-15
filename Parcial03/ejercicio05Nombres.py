nombre_completo = input("Ingrese su nombre completo: ")

partes_nombre = nombre_completo.split()

nombre_invertido = partes_nombre[::-1]

for palabra in nombre_invertido:
    letras_formateadas = ""

    for letra in palabra:
        letras_formateadas += letra + "."

    letras_formateadas = letras_formateadas[:-1]

    print(letras_formateadas)
