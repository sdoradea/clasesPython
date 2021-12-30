lista_de_compras = []
input_de_articulo = None

print("\nLista de compras\n\n")

while True:
    input_de_articulo = input("Que desea compar? - Presione [Q] para salir\n")
    if input_de_articulo == "Q":
        break
    elif input_de_articulo in lista_de_compras:
        print("{} ya esta en la lista de compras" .format(input_de_articulo))
    else:
        if input("Seguro que desea agregar {} a la lista S/N\n" .format(input_de_articulo)) == "S":
           lista_de_compras.append(input_de_articulo)

print("La lista de la compra es:\n")
print(lista_de_compras)