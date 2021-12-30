eSpacios = 0
pUntos = 0
cOmas = 0
txt_Usuario = input("Ingrese una frace\n")

for letra in txt_Usuario:
    if letra == " ":
        eSpacios += 1
    elif letra == ".":
        pUntos += 1
    elif letra == ",":
        cOmas += 1
print("Espacios: {} Puntos: {} Comas: {}" .format(eSpacios, pUntos, cOmas))

import string

letra_Mayucula = 0
txt_Usuario2 = input("Introdusca un texto\n")

for letra in txt_Usuario2:
    if letra in string.ascii_uppercase:
        letra_Mayucula += 1

print("Las Mayusculas son: {}" .format(letra_Mayucula))