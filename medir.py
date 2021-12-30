def medirlargos(iterable, *args):
    if args:
        largos = [len(iterable)]
        for a in args:
            largos.append(len(a))
        return largos
    return len(iterable)


def main():
    print(medirlargos("hola"))
    print(medirlargos("hola", "como", "estas"))


if __name__ == "__main__":
    main()
