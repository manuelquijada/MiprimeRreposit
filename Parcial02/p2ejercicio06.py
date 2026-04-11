# ejercicio 6
texto = "Manuel"

# preparo el texto para comparar ignorando mayusculas
normal = texto.casefold()

# verifico si solo tiene letras
verificar = normal.replace(" ", "").isalpha()

print(normal)
print(verificar)
