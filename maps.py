import keyboard
import os
import start

def map():
    print("Hau'oli Outskirts East   { E }")
    print("Hau'oli Outskirts South  { S }")
    menu = input("What do you want to do?: ").upper()
    if(menu == "E"):
        map_hauoliOutskirtsEast()
    elif(menu == "S"):
        map_hauoliOutskirtsSouth()
    

def map_hauoliOutskirtsEast():
    os.system('cls')
    print("Hau'oli Outskirts east")
    print("""
    ___________         _________________________________
    |#########|    X   |                                |   X  |#|
    |#/---\\ ##|        |                                |      |#|
    |#| PS | #|        |                                |      |#|
    |#\\---/ ##|        |                                |      |#|
    |_________|        |________________________________|      |#|
     X                                                         |#|
     __________        ________________________________________|#|
    |##########|       |#########################################|
    |__________|    3  |_________________________________________|
    """)
    print("{ X } => Route 1")
    print("{ X } => School")
    print("{ 3 } => Kukui's house")
    print("{ X } => Pokéstop (PS)")
    print("to return press { esc } ")
    def on_key_press(event):
        if event.name == 'esc':
            start.pokemon_stats()

    keyboard.on_press(on_key_press)
    way = input("Where do you want to go?")
    if way == 3:
        map_hauoliOutskirtsSouth()


def map_hauoliOutskirtsSouth():
    os.system('cls')
    print("Hau'oli Outskirts south")
    print("""
    ___________         _________________________________________
    |#########|        |                                       |#|
    |#########|        |                                       |#|
    |#########\\________/         ____________                 |#|
    |#########                   |          |                  |#|
    |##############              |   Kukui  |                  |#|
    |##############              |__________|                  |#|
    |__________________________________________________________|#|
    ~~~~~~         ~~~~~~          ~~~~~~              ~~~~~~  
       ~~~~~~              ~~~~~~ ~~~~~~    ~~~~~~          ~~~~~~ 
    """)
    print("{ X } => Route 1")
    print("{ X } => Schule")
    print("{ 3 } => Kukui's Haus")
    print("{ X } => Pokéstop (PS)")
    print("to return press { esc } ")
    def on_key_press(event):
        if event.name == 'esc':
            start.pokemon_stats()

    keyboard.on_press(on_key_press)
    way = input("Where do you want to go?")
