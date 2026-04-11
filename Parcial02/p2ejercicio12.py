# ejercicio 12
archivo = "Manuel.txt"

# primero quito la extension del archivo
nuevo = archivo.removesuffix(".txt")

# este prefijo no existe en el texto, pero uso el metodo porque lo pide el ejercicio
nuevo = nuevo.removeprefix("ING. ")

# convierto todo a minusculas
nuevo = nuevo.lower()

print(nuevo)
