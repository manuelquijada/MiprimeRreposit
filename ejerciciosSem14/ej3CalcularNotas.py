# Calcular promedio de notas


def calcular_promedio(notas):
    suma = 0

    for nota in notas:
        suma += nota

    promedio = suma / len(notas)
    return promedio


notas = []

for i in range(5):
    nota = float(input("Ingrese una nota: "))
    notas.append(nota)

promedio = calcular_promedio(notas)

print("Promedio:", promedio)

if promedio >= 6:
    print("El grupo aprueba")
else:
    print("El grupo reprueba")
