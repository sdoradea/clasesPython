def anadir_lista_numero(lista_numero, numero):
    lista_numero.append(numero)


def main():
    lista_numero = []
    anadir_lista_numero(lista_numero, 1)
    anadir_lista_numero(lista_numero, 4)
    anadir_lista_numero(lista_numero, 2)
    print(lista_numero)


if __name__ == "__main__":
    main()
