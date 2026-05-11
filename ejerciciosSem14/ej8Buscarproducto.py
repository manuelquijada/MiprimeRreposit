# Buscar producto


def buscar_producto(productos, buscado):
    for producto in productos:
        if producto == buscado:
            return True

    return False


productos = []

for i in range(5):
    producto = input("Ingrese un producto: ")
    productos.append(producto)

buscar = input("Ingrese el producto a buscar: ")

if buscar_producto(productos, buscar):
    print("Producto encontrado")
else:
    print("Producto no encontrado")
