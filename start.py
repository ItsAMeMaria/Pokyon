from time import sleep
import os
from playerGameData import playingGame
import pokemonList
import playerGameData
import keyboard
import maps

def main():
    os.system('cls')
    print("▄▄▄·      ▄ •▄  ▄· ▄▌       ▐ ▄ ")
    print("▐█ ▄█▪     █▌▄▌▪▐█▪██▌▪     •█▌▐█")
    print("██▀· ▄█▀▄ ▐▀▀▄·▐█▌▐█▪ ▄█▀▄ ▐█▐▐▌")
    print("▐█▪·•▐█▌.▐▌▐█.█▌ ▐█▀·.▐█▌.▐▌██▐█▌")
    print(".▀    ▀█▄▀▪·▀  ▀  ▀ •  ▀█▄▀▪▀▀ █▪")
    print("------------------------------------------------------")
    print("Welcome to Pokyon. A Pokémon game made with Python")
    print("------------------------------------------------------")
    print("         start new game  { s }")
    print("         load game       { l }")
    print("         quit game       { q }")
    game = input("Type in the letter: ")
    if(game == "s"):
        startGame()
    elif(game == "q"):
        exit()

def getPlayerName():
    playerName = playerGameData.getName()
    return playerName

def startGame():     
    loadingAnimation()
    print("???  | Just a second...")
    sleep(2)
    print("???  | okey, good afternoon, it's me Professor Kukui ")
    sleep(2)
    print("Kukui| Before you start your journey on this island")
    print("       you should first type in your name for your Trainer Passport!")
    playerName = getPlayerName()
    print("Kukui| Alright, " + playerName + ". We'll see eachother soon!")
    sleep(2)
    loadingAnimation()
    print("You are now in your house " + playerName)
    print("To get a starter Pokémon, go to Professor Kukui's house.")
    print("To see where his house is press { m } to open the map")
    def on_key_press(event):
        try:
            if event.name == 'm':
                maps.map()
            elif event.name == 'p':
                playerGameData.playingGame()
        except:
            print("please press a letter from above")
            

    keyboard.on_press(on_key_press)
    keyboard.wait()

    
def chooseAStarter():
    loadingAnimation()
    print("Now you have to choose a starter Pokémon!")
    print("Here are the available starter Pokémons for you.")
    print("Rowlet  { 1 }")
    print("Popplio { 2 }")
    print("Litten  { 3 }")
    pokemon_number = int(input("Choose a Pokémon and type in the number: "))
    if pokemon_number == 1:
        chosen_pokemon = pokemonList.pokemonlist.get("Rowlet")
    elif pokemon_number == 2:
        chosen_pokemon = pokemonList.pokemonlist.get("Popplio")
    elif pokemon_number == 3:
        chosen_pokemon = pokemonList.pokemonlist.get("Litten")
    print("You have chosen: " + chosen_pokemon["name"])
    return chosen_pokemon


def pokemon_stats():
    loadingAnimation()
    chosen_pokemon = chooseAStarter()
    pokemon_name = chosen_pokemon["name"]
    pokemon_type = chosen_pokemon["type"]
    print("/----------------------------------------\\")
    print("|Pokémon: " + pokemon_name + "| type: " + pokemon_type + "|")
    print("\----------------------------------------/")
    print("")
    playingGame()


def loadingAnimation():
    print("loading")
    loading = '...'
    for i in range(3):
        print(loading[i], flush=True)
        sleep(1)
    os.system('cls')


if __name__ == "__main__":
    main()
