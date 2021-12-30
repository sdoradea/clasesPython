numero1 = int(input("ingresa el primer numero: "))
numero2 = int(input("ingrese el segundo numero: "))

if numero1 < numero2:
    for x in range(numero1, (numero2 + 1)):
        if x % 2 == 0:
            print(f"{x} es par")
        else:
            print(f"{x} es impar")
else:
    print("numero 1 debe ser menor al numero 2")