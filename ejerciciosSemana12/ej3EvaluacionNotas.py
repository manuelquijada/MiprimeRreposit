# Evaluacion de notas.

nota = int(input("Ingresa la nota (0-10): "))

if nota >= 9:
    print("Excelente")
elif nota >= 7:
    print("Bueno")
elif nota == 6:
    print("Aprobado")
else:
    print("Reprobado")
