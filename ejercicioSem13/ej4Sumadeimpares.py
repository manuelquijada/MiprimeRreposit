# suma de impares

suma = 0
impares = []

while True:
    numero = int(input("Ingrese un número, 0 para terminar: "))

    if numero == 0:
        break

    if numero % 2 != 0:
        suma += numero
        impares.append(numero)

print("Suma de impares:", suma)

for numero in impares:
    print("Número impar ingresado:", numero)
