#METODO 1
"""
numerosUsuario = []
numeroIntroducido = int(input("Introduzca un numero en la lista: \n"))
numerosUsuario.append(numeroIntroducido)

while input("Desea introducir otro numero en la lista [S/N]") == "S":
    numeroIntroducido = int(input("Introduzca un numero en la lista: \n"))
    numerosUsuario.append(numeroIntroducido)

for numero in numeroUsuario[1:]:
    if numeroPequenio > numero:
       numeroPequenio = numero
    
    if numeroGrande < numero:
       numeroGrande = numero  

print("El numero mas pequenio es: {} y el numero mas grande es: {}" . format(numeroPequenio, numeroGrande))
"""

#METODO 2
"""
numeroIntroducido = input("Introduzca los numeros separados por coma:\n")
numeroUsuario = numeroIntroducido.split(",")
numeroUsuarioInt = []
for numero in numeroUsuario:
    numeroUsuarioInt.append(int(numero))
for numero in numeroUsuario[1:]:
    if numeroPequenio > numero:
       numeroPequenio = numero
    
    if numeroGrande < numero:
       numeroGrande = numero  

print("El numero mas pequenio es: {} y el numero mas grande es: {}" . format(numeroPequenio, numeroGrande))
"""

# METODO 3 List Comprehesion

numeroIntroducido = input("Introduzca los numeros separados por coma:\n")
numeroUsuario = [int(numero) for numero in numeroIntroducido.split(",")]
numeroPequenio = numeroUsuario[0]
numeroGrande = numeroUsuario[0]

for numero in numeroUsuario[1:]:
    if numeroPequenio > numero:
       numeroPequenio = numero
    
    if numeroGrande < numero:
       numeroGrande = numero 

print("El numero mas pequenio es: {} y el numero mas grande es: {}" .format(numeroPequenio, numeroGrande))