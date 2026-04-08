# aqui cambia una palabra segun el numero


def palabra(palabra, num):
    if num == 1:
        print(palabra.upper())
    elif num == 2:
        print(palabra.lower())
    elif num == 3:
        print(palabra.capitalize())


palabra("manuel", 3)
