etiqueta = input("Ingrese la etiqueta de rastreo: ")

if etiqueta == "" or etiqueta is None:
    print("Error: la etiqueta no puede estar vacía.")
else:
    categoria = etiqueta[5:-3]

    print(f"Categoría del paquete: {categoria}")

    ruta = "Ruta Local" if etiqueta.endswith("SV") else "Ruta Internacional"
    print(ruta)
