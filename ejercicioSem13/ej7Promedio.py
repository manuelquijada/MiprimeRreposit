# Promedio de notas

notas_validas = []

while True:
    nota = float(input("Ingrese una nota, -1 para terminar: "))

    if nota == -1:
        break

    if nota < 0 or nota > 10:
        print("Nota inválida")
    else:
        notas_validas.append(nota)

suma = 0

for nota in notas_validas:
    suma += nota

if len(notas_validas) > 0:
    promedio = suma / len(notas_validas)
    print("Promedio:", promedio)
else:
    print("No se ingresaron notas válidas")
