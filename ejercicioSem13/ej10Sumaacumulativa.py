# suma acumulativa con limite

suma = 0
numeros_validos = []

while suma <= 100:
    numero = int(input("Ingrese un número: "))

    if numero < 0:
        print("Número negativo ignorado")
    else:
        suma += numero
        numeros_validos.append(numero)

print("La suma superó 100:", suma)

for numero in numeros_validos:
    print("Número válido ingresado:", numero)
