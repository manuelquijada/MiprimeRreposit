# Validar contraseña

contrasena_correcta = "1234"
intentos_fallidos = 0

while True:
    contrasena = input("Ingrese la contraseña: ")

    if contrasena == contrasena_correcta:
        print("Contraseña correcta")
        break
    else:
        print("Contraseña incorrecta")
        intentos_fallidos += 1

for i in range(intentos_fallidos):
    print("Intento fallido número", i + 1)
