# Juego de numeros

seguir = "si"

while seguir == "si":
    print("\n--- JUEGO DE NUMEROS ---")
    print("1. Ver numeros pares")
    print("2. Ver numeros impares")
    print("3. Ver todos (par o impar)")
    print("4. Salir")

    opcion = int(input("Ingrese una opcion: "))

    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    if opcion == 1:
        print("\nNumeros pares:")
        for n in lista:
            if n % 2 == 0:
                print(n)

    elif opcion == 2:
        print("\nNumeros impares:")
        for n in lista:
            if n % 2 != 0:
                print(n)

    elif opcion == 3:
        print("\nTodos los numeros:")
        for n in lista:
            if n % 2 == 0:
                print(n, "es par")
            else:
                print(n, "es impar")

    elif opcion == 4:
        print("Fin del programa")
        break

    else:
        print("Opcion no valida")

    seguir = input("Desea continuar? (si/no): ")

print("Programa terminado")
