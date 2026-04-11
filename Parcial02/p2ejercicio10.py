# ejercicio 10
texto = "Python2026"

# verifico si es alfanumerico
validar = texto.isalnum()

print(validar)

if validar:
    # convierto a minusculas
    minus = texto.lower()

    # separo la palabra de los numeros
    palabra = minus.replace("2026", "")

    print(palabra)
