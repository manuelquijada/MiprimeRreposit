# Validacion de usuario y contraseña.

usuario_correcto = "admin"
password_correcto = "1234"

usuario = input("Usuario: ")
password = input("Contraseña: ")

if usuario == usuario_correcto and password == password_correcto:
    print("Acceso permitido")
else:
    print("Acceso denegado")
