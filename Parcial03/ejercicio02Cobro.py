from decimal import Decimal

total = Decimal("0.00")

while True:
    entrada = input("Ingrese el precio del producto o 0 para salir: ")

    try:
        precio = float(entrada)

        if precio == 0:
            break

        total += Decimal(str(precio))

    except ValueError:
        print("Error: debe ingresar un número válido.")

print(f"Total acumulado: ${total}")
