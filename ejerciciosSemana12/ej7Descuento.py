# Calculo de descuento en compras.

monto = float(input("Ingresa el monto de la compra: "))

if monto > 100:
    descuento = monto * 0.20
elif monto >= 50:
    descuento = monto * 0.10
else:
    descuento = 0

total = monto - descuento

print("Descuento:", descuento)
print("Total a pagar:", total)
