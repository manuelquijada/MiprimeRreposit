# ejercicio 4
# palabra inicial
palabra = "CANTANDO"

# la paso a minusculas
minus = palabra.lower()

# le quito el sufijo ando
nuevo = minus.removesuffix("ando")

# busco la posicion de la letra t
posicion = nuevo.find("t")

print(nuevo)
print("la posicion de la t es:", posicion)
