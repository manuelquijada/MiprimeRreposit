# Contar mayores de edad


def mayores_edad(edades):
    contador = 0

    for edad in edades:
        if edad >= 18:
            contador += 1

    return contador


edades = []

for i in range(5):
    edad = int(input("Ingrese una edad: "))
    edades.append(edad)

print("Mayores de edad:", mayores_edad(edades))
