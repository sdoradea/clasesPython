def incrementar(num):
    num += 1
    return num


def main():
    numero = 8
    numero = incrementar(numero)
    numero = incrementar(numero)
    numero = incrementar(numero)
    print(numero)


if __name__ == "__main__":
    main()
