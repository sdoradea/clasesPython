""" 
EL propocito de las funciones es basicamente, tener un unico codigo unificado
bajo un nombre, al cual le podemos pasar variables sin que tengamos que 
repetir el codigo y la funciones no solo pueden recibir parametros
tambien pueden devolverlos.

"""


#funciones
def saludo_secreto():
    print("Hola Mundo")
    a=input("Como estas?")
    b=input("Dos mas Dos")

    if b == "2":
        print("Tu si que sabes.")


saludo_secreto()

#funcion con argumento o parametro

def saludo_sectario(nombre):
    print("Hola {} " .format(nombre[::-1]))

saludo_sectario("Elena")
saludo_sectario("Aaron")
saludo_sectario("Nadja")
saludo_sectario("Stanley")

# devuelve un parametro
def largo_string(my_string):
    largo = 0
    for n in my_string:
        largo += 1
    return largo


largo_de_la_string = largo_string("Hola mundo")

print(largo_de_la_string)