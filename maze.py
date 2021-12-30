import random
import readchar as readchar
import os

POS_X = 0
POS_Y = 1
NOBJECTS_ON_MAP = 10

obstacule_definition = """ ◙◙◙◙◙   ◙◙ ◙      ◙
◙             ◙◙    
       ◙            
◙    ◙◙◙◙◙   ◙    ◙ 
◙            ◙      
◙    ◙       ◙    ◙ 
◙      ◙     ◙    ◙ 
        ◙        ◙  
◙◙     ◙     ◙    ◙ 
      ◙      ◙      
◙    ◙       ◙◙   ◙ 
◙     ◙     ◙     ◙ 
◙      ◙     ◙    ◙  """

my_position = [3, 1]
map_obj = []
tail_length = 0
tail = []

endGame = False
died = False

# create obstacule map

obstacule_definition = [list(row) for row in obstacule_definition.split("\n")]
MAP_WIDHT = len(obstacule_definition[0])
MAP_HEIGHT = len(obstacule_definition)

# main loop
while not endGame:
    os.system("cls")
    # Generate new objects on the map
    while len(map_obj) < NOBJECTS_ON_MAP:
        new_position = [random.randint(0, MAP_WIDHT - 1), random.randint(0, MAP_HEIGHT - 1)]

        if new_position not in map_obj and new_position != my_position and obstacule_definition[new_position[POS_Y]][new_position[POS_X]] != "◙":
            map_obj.append(new_position)

    # Draw map
    print("+" + "-" * (MAP_WIDHT * 2) + "+")

    for coordinate_y in range(MAP_HEIGHT):
        print("|", end="")

        for coordinate_x in range(MAP_WIDHT):

            char_to_draw = "  "
            object_in_cell = None
            tail_in_cell = None

            for map_objs in map_obj:
                if map_objs[POS_X] == coordinate_x and map_objs[POS_Y] == coordinate_y:
                    char_to_draw = " ♦"
                    object_in_cell = map_objs

            for tail_piece in tail:
                if tail_piece[POS_X] == coordinate_x and tail_piece[POS_Y] == coordinate_y:
                    char_to_draw = " Þ"
                    tail_in_cell = tail_piece

            if my_position[POS_X] == coordinate_x and my_position[POS_Y] == coordinate_y:
                char_to_draw = " Þ"

                if object_in_cell:
                    map_obj.remove(object_in_cell)
                    tail_length += 1

                if tail_in_cell:
                    endGame = True
                    died = True

            if obstacule_definition[coordinate_y][coordinate_x] == "◙":
                char_to_draw = " ◙"

            print("{}".format(char_to_draw), end="")

        print("|")

    print("+" + "-" * (MAP_WIDHT * 2) + "+")

    direction = readchar.readchar().decode()
    new_position = None

    if direction == "w":
        new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_WIDHT]
    elif direction == "s":
        new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_WIDHT]
    elif direction == "a":
        new_position = [(my_position[POS_X] - 1) % MAP_WIDHT, my_position[POS_Y]]
    elif direction == "d":
        new_position = [(my_position[POS_X] + 1) % MAP_WIDHT, my_position[POS_Y]]
    elif direction == "o":
        endGame = True
    if new_position:
        if obstacule_definition[new_position[POS_Y]][new_position[POS_X]] != "◙":
            tail.insert(0, my_position.copy())
            tail = tail[:tail_length]
            my_position = new_position

if died:
    print("Haz Muerto!")
    print(""" 
███████████████████████████
███████▀▀▀░░░░░░░▀▀▀███████
████▀░░░░░░░░░░░░░░░░░▀████
███│░░░░░░░░░░░░░░░░░░░│███
██▌│░░░░░░░░░░░░░░░░░░░│▐██
██░└┐░░░░░░░░░░░░░░░░░┌┘░██
██░░└┐░░░░░░░░░░░░░░░┌┘░░██
██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
██▌░│██████▌░░░▐██████│░▐██
███░│▐███▀▀░░▄░░▀▀███▌│░███
██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
████▄─┘██▌░░░░░░░▐██└─▄████
█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
███████▄░░░░░░░░░░░▄███████
██████████▄▄▄▄▄▄▄██████████
███████████████████████████
    """)