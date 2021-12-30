a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listadeCompras = ["lecha", "Pan", "Arroz"]
frase = "Hola, estoy aprendiendo python"
vocales = ["a", "e", "i", "o", "u"]
nvocales = 0

for item in a:
    print(item)
for item2 in listadeCompras:
    print(item2)
for letra in frase:
    print("He encotnrado una {}" .format(letra))
    nvocales += 1
print("Numero de vocales encontradas {}" .format(nvocales))

numero_de_repeticiones = int(input("cuantas veces quieres repetir el mensaje?\n"))
for nv in range(numero_de_repeticiones):
    print("Hola")
for nv in range(5):
    print(nv)
for nv in range(5, 9):
    print(nv)
for nv in range(9, nv + 1):
    print(nv)