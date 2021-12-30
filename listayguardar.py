SALIDA = "salir"

itens_del_supermercado = ["pollo", "carne", "maiz", "lechuga", "pan"]

def producto_usuario():
    return input("introduce un articulo o escribe [salir]:  ")

def guardar_lista_a_disco(lista_compra):
    nombredefichero = input("como quieres que se llame el archivo?:    ")
    with open(nombredefichero + ".txr", "w") as mi_archivo:
        mi_archivo.write("\n".join(lista_compra))

def guardar_lista_de_la_compra(lista_compra, iten_a_guardar):
        if iten_a_guardar.lower() in [a.lower() for a in lista_compra]:
            print("el articulo ya existe")
        else:
            lista_compra.append(iten_a_guardar)
       

def main():
    lista_compra = []
    input_usuario = producto_usuario()
    while input_usuario != SALIDA:
        guardar_lista_de_la_compra(lista_compra, input_usuario)
        print("\n".join(lista_compra))
        input_usuario = producto_usuario()
    
    guardar_lista_a_disco(lista_compra)


if __name__ == "__main__":
    main()
