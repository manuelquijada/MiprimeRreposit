temperaturas = []

for i in range(5):
    lectura = int(input(f"Ingrese la temperatura {i + 1}: "))
    temperaturas.append(lectura)

for temperatura in temperaturas:
    match temperatura:
        case 0:
            print("Alerta: Punto de Congelación")
        case 100:
            print("Alerta: Punto de Ebullición")
        case _:
            estado = (
                "Estado: Estable"
                if temperatura >= 10 and temperatura <= 30
                else "Estado: Crítico"
            )
            print(estado)
