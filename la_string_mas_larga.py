frase = []
listadePalabras = ""
separador = " "

cadena = input("ingrese una frase\n") + (" ")
for caracter in cadena:
    if caracter == separador:
        if listadePalabras:
            frase.append(listadePalabras)
            listadePalabras = ""
    else:
        listadePalabras += caracter

palabraMax = max(frase, key=len)
palabraMin = min(frase, key=len)

print("La palabras las larga es: {} y la mas corta es: {}" .format(palabraMax, palabraMin))