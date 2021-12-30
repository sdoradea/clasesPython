from random import randint
import os
import msvcrt
vida_actual_pikachu = 100
vida_actual_squirtle = 100
vida_inicial_pikachu = vida_actual_pikachu
vida_inicial_squirtle = vida_actual_squirtle

print("""
                                         ,'
    _.----.        ____         ,'  _\   ___    ___     ____
_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.
\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |
 \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |
   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |
    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |
     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |
      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |
       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |
        \_.-'       |__|    `-._ |              '-.|     '-.| |   |
                                `'                            '-._|""")

t_2 = "Pikachu VS Squirtle?"
print("\n" + "__" + len(t_2) * "_" + "\n" + "|" + t_2 + "|" +"\n" + "¯¯" + len(t_2) * "¯")
print("Precione Enter para continuar")
msvcrt.getch()
os.system("cls")

barra_vidaPikachu = int(vida_actual_pikachu *10 / vida_inicial_pikachu)
print("Pikachu:    [{}{}] ({}/{})" .format("*" * barra_vidaPikachu, " " * (10 - barra_vidaPikachu), 
vida_actual_pikachu, vida_inicial_pikachu))
barra_vidaSquirtle = int(vida_actual_squirtle *10 / vida_inicial_squirtle)
print("Squirtle:    [{}{}] ({}/{})" .format("*" * barra_vidaSquirtle, " " * (10 - barra_vidaSquirtle), 
vida_actual_squirtle, vida_inicial_squirtle))

while vida_actual_pikachu > 0 and vida_actual_squirtle > 0:
    # Reinicia los turnos
    #Turno Pikachu
    print("Turno Pikachu\n")
    atk_pikachu = randint(1, 2)
    if atk_pikachu == 1:
        print("Pikachu usa Impactrueno\n")
        vida_actual_squirtle -= randint(5, 10)
    else:
        print("Pikachu usa Rayo\n")
        vida_actual_squirtle -= randint(10, 15)
    if vida_actual_pikachu < 0:
       vida_actual_pikachu = 0
        
    if vida_actual_squirtle < 0:
       vida_actual_squirtle = 0

    print("Presione Enter para continuar\n")
    msvcrt.getch()
    os.system("cls")

    #Turno Squirtle
    
    print("Turno de Squirtle\n")

    barra_vidaPikachu = int(vida_actual_pikachu *10 / vida_inicial_pikachu)
    print("Pikachu:    [{}{}] ({}/{})" .format("*" * barra_vidaPikachu, " " * (10 - barra_vidaPikachu), 
    vida_actual_pikachu, vida_inicial_pikachu))
    barra_vidaSquirtle = int(vida_actual_squirtle *10 / vida_inicial_squirtle)
    print("Squirtle:    [{}{}] ({}/{})" .format("*" * barra_vidaSquirtle, " " * (10 - barra_vidaSquirtle), 
    vida_actual_squirtle, vida_inicial_squirtle))

    atk_squirtle = None
    while atk_squirtle != "A" and atk_squirtle != "B" and atk_squirtle != "C" and atk_squirtle != "D":
        print("Turno Squirtle\n")
        atk_squirtle = input("Que Ataque quieres realizar\n"
                             "[A] Embestida    [B]Burbuja\n"
                             "[C] Rayo Hielo   [D] Hidrobomba\n")
        if atk_squirtle == "A":
            print("Squirtle ha usado Embestida\n")
            vida_actual_pikachu -= randint(5, 10)
        elif atk_squirtle == "B":
            print("Squirtle ha usado Burbuja\n")
            vida_actual_pikachu -= randint(5, 10)
        elif atk_squirtle == "C":
            print("Squirtle ha usado Rayo Hielo\n")
            vida_actual_pikachu -= randint(5, 10)
        elif atk_squirtle == "D":
            print("Squirtle ha usado Hidrobomba\n")
            vida_actual_pikachu -= randint(10, 15)
        
        if vida_actual_pikachu < 0:
            vida_actual_pikachu = 0
        
        if vida_actual_squirtle < 0:
            vida_actual_squirtle = 0

            barra_vidaPikachu = int(vida_actual_pikachu *10 / vida_inicial_pikachu)
            print("Pikachu:    [{}{}] ({}/{})" .format("*" * barra_vidaPikachu, " " * (10 - barra_vidaPikachu), 
            vida_actual_pikachu, vida_inicial_pikachu))
            barra_vidaSquirtle = int(vida_actual_squirtle *10 / vida_inicial_squirtle)
            print("Squirtle:    [{}{}] ({}/{})" .format("*" * barra_vidaSquirtle, " " * (10 - barra_vidaSquirtle), 
            vida_actual_squirtle, vida_inicial_squirtle))
            msvcrt.getch()
            os.system("cls")
            
    if vida_actual_pikachu == 0:
        print("Squirtle Gana")
        barra_vidaPikachu = int(vida_actual_pikachu *10 / vida_inicial_pikachu)
        print("Pikachu:    [{}{}] ({}/{})" .format("*" * barra_vidaPikachu, " " * (10 - barra_vidaPikachu), 
        vida_actual_pikachu, vida_inicial_pikachu))
        print("\n\n Gracias por jugar\n\n")
    elif vida_actual_squirtle == 0:
        print("Pikachu Gana")
        barra_vidaPikachu = int(vida_actual_pikachu *10 / vida_inicial_pikachu)
        print("Pikachu:    [{}{}] ({}/{})" .format("*" * barra_vidaPikachu, " " * (10 - barra_vidaPikachu), 
        vida_actual_pikachu, vida_inicial_pikachu))
        print("\n\n Gracias por jugar\n\n")