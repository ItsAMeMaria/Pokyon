import random
import datetime

def getName():
    playerName = input("Type in your name: ")
    return playerName

def generate_random_id():
    places = 0
    random_id = ''
    while places < 7:
        random_id += str(random.randrange(10))
        places += 1
    return random_id 

def getDate():
    date = str(datetime.date.today())
    return date

player_name = getName()
player_id = generate_random_id()
player_startedOn = getDate()

player_data = {
    'player_name': player_name,
    'player_id': player_id,
    'player_startedOn': player_startedOn,
}

name = player_data.get("player_name")
id = player_data.get("player_id")
date = player_data.get("player_startedOn")

    
def playingGame():
    print("_" * 55)
    print("| Name:      {:<40}|".format(player_name))
    print("| ID no.:    {:<40}|".format(player_id))                                    
    print("-" * 55)
    print("| Adventure started on:  {:<30}|".format(date))
    print("_" * 55)
