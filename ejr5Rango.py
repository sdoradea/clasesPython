numero1 = int(input("ingrese el primer numero: "))
numero2 = int(input("ingrese el segundo numero: "))

if numero1 < numero2:
    for i in range(numero1, (numero2 + 1)):
        print(i)
else:
    print("El primer numero debe ser menor al segundo numero.")