SALIDA = "salir"
ARCHIVO_COMPRA = "lista de compras.txt"

def producto_usuario():
    return input("introduce un articulo o escribe [salir]:  ")

def guardar_lista_a_disco(lista_compra):
    with open(ARCHIVO_COMPRA, "w") as mi_archivo:
        mi_archivo.write("\n".join(lista_compra))

def guardar_lista_de_la_compra(lista_compra, iten_a_guardar):
        if iten_a_guardar.lower() in [a.lower() for a in lista_compra]:
            print("el articulo ya existe")
        else:
            lista_compra.append(iten_a_guardar)

def cargar_o_crear_lista():
    lista_compra = []
    if input("Desea cargar la ultima lista de compras [S/N]") == "S":
        try:
            with open(ARCHIVO_COMPRA, "r") as a:
                lista_compra = a.read().split("\n")
        except FileNotFoundError:
            print("El archivo no existe")
        return lista_compra

def mostrar_lista(lista_compra):
    print("\n".join(lista_compra))
       

def main():
    lista_compra = cargar_o_crear_lista()
    mostrar_lista(lista_compra)
    input_usuario = producto_usuario()
    while input_usuario != SALIDA:
        guardar_lista_de_la_compra(lista_compra, input_usuario)
        input_usuario = producto_usuario()
    mostrar_lista(lista_compra)
    guardar_lista_a_disco(lista_compra)


if __name__ == "__main__":
    main()
