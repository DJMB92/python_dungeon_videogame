from pygame import mixer
from pygame.locals import *
import os
import time
print_counter = 0


# Vanessa - First Room
couch = {
    "name": "poster movie",
    "type": "furniture",
}
door_a = {
    "name": "Blockbuster portal",
    "type": "door",
}
key_a = {
    "name": "a movie",
    "type": "key",
    "target": door_a,
}
piano = {
    "name": "movie shelf",
    "type": "furniture",
}
game_room = {
    "name": "Blockbuster",
    "type": "room",
}
outside = {
    "name": "outside"
}
# END Vanessa - First Room


# Alicia items/characters

bedroom_1 = {
    "name": "Wonderland",
    "type": "room",
}

door_b = {
    "name": "Castle Portal",
    "type": "door",
}

key_b = {
    "name": "Sugar cookie",
    "type": "key",
    "target": door_b,
}

queen_bed = {
    "name": "Mad Hatter",
    "type": "furniture",
}

desk = {
    "name": "Cheshire Cat",
    "type": "furniture",
}
# End Alicia items/characters


# Vanessa items/characters
bedroom_2 = {
    "name": "Hogwarts",
    "type": "room",
}

door_c = {
    "name": "Time turner portal",
    "type": "door",
}

key_c = {
    "name": "travel cordinates",
    "type": "key",
    "target": door_c,
}

little_girl = {
    "name": "Dobby",
    "type": "person",
}

Voldemort = {
    "name": "Voldemort",
    "type": "person",
}

old_person = {
    "name": "Dumbledore",
    "type": "person",
}
# END Vanessa items/characters

# Amelie items/characters

groot = {
    "name": "groot",
    "type": "person",
}

black_hole = {
    "name": "black hole",
    "type": "door",
}

root_key = {
    "name": "key for black hole",
    "type": "key",
    "target": black_hole,
}

rocket = {
    "name": "rocket",
    "type": "person",
}

starlord = {
    "name": "starlord",
    "type": "person",
}

galaxy = {
    "name": "Unknown Galaxy",
    "type": "room",
}

gamora = {
    "name": "gamora",
    "type": "person",
}
# END Amelie items/characters

# Daniel items/characters

weapon = False

bedroom_4 = {
    "name": "Mordor",
    "type": "room",
}
gollum = {
    "name": "Gollum",
    "type": "person",
}
sword = {
    "name": "Narsil",
    "type": "furniture",
}
door_end = {
    "name": "Entrance to Mt Doom",
    "type": "door",
}
sword = {
    "name": "Narsil",
    "type": "key",
    "target": gollum,
}
key_end = {
    "name": "Key to Mount Doom",
    "type": "key",
    "target": door_end,
}
# End Daniel items/characters


all_rooms = [game_room, bedroom_1, bedroom_2, galaxy, bedroom_4, outside]
all_doors = [door_a, door_b, door_c, black_hole, door_end]

# define which items/rooms are related
object_relations = {
    # Vanessa Relations 1
    "Blockbuster":        [couch, piano, door_a],
    "movie shelf":        [key_a],
    "Blockbuster portal":   [game_room, bedroom_1],
    # END Vanessa Relations

    # Alicia relations
    "Wonderland":    [queen_bed, desk, door_a, door_b],
    "Mad Hatter":    [key_b],
    "Cheshire Cat":  [key_b],
    "Castle Portal":   [bedroom_1, bedroom_2],
    # End Alicia relations

    # Vanessa Relations 2
    "Hogwarts":    [door_b, door_c, old_person, little_girl, Voldemort],
    "Voldemort":   [key_c],
    "Dobby":       [key_c],
    "Time turner portal":      [bedroom_2, galaxy],
    # END Vanessa Relations 2

    # Amelie relations:
    "Unknown Galaxy":        [door_c, black_hole, groot, rocket, starlord, gamora],
    "groot":         [root_key],
    "black hole":    [galaxy, bedroom_4],
    # END Amelie relations:

    # Daniel relations
    "Mordor":                 [black_hole, door_end, gollum, sword],
    "Narsil":                 [sword],
    "Gollum":                 [key_end],
    "Entrance to Mt Doom":    [outside],
    # End Daniel relations
}

# define game state. Do not directly change this dict.
# Instead, when a new game starts, make a copy of this
# dict and use the copy to store gameplay state. This
# way you can replay the game multiple times.

INIT_GAME_STATE = {
    "current_room": game_room,
    "keys_collected": [],
    "target_room": outside
}


def linebreak():
    """
    Print a line break
    """
    print("\n\n")


def start_game():
    """
    Start the game
    """
    os.system('cls')
    print("You are now in the blockbuster multiverse, find your movie to enter into your first adventure!")
    play_room(game_state["current_room"])


def play_room(room):
    """
    Play a room. First check if the room being played is the target room.
    If it is, the game will end with success. Otherwise, let player either
    explore (list all items in this room) or examine an item found here.
    """
    global print_counter
    game_state["current_room"] = room
    if (game_state["current_room"] == game_state["target_room"]):
        os.system('cls')
        mixer.init()
        mixer.music.load('lotr.mp3')
        mixer.music.play()
        mixer.music.set_volume(0.2)
        game_ring()
        print("Congrats! You forged your story and beat the game!\n")
        input("Press any key to close the game...")
        time.sleep(3)
    else:
        # os.system('cls')
        if room["name"] == 'Blockbuster' and print_counter < 1:
            print_shelf()
            print_counter = 1
        if room["name"] == 'Wonderland' and print_counter < 1:
            print_wonderland()
            print_counter = 1
        if room["name"] == 'Hogwarts' and print_counter < 1:                
            print_hogwarts()
            print_counter = 1
        if room["name"] == 'Mordor' and print_counter < 1:
            print_lotr()
            print_counter = 1
        if room["name"] == 'Unknown Galaxy' and print_counter < 1:
            print_galaxy()
            print_counter = 1
        print("Multiverse Geo-Locator :-> " + room["name"] + '\n')
        intended_action = input(
            "What would you like to do? Type 'explore' or 'examine'?\n").strip()
        if intended_action == "explore":
            explore_room(room)
            play_room(room)
        elif intended_action == "examine":
            examine_item(input("What would you like to examine?\n").strip())
        else:
            print("Not sure what you mean. Type 'explore' or 'examine'.\n")
            play_room(room)
        linebreak()


def explore_room(room):
    """
    Explore a room. List all items belonging to this room.
    """
    items = [i["name"] for i in object_relations[room["name"]]]
    print("You explore the room; you see a " + ", ".join(items))


def get_next_room_of_door(door, current_room):
    """
    From object_relations, find the two rooms connected to the given door.
    Return the room that is not the current_room.
    """
    connected_rooms = object_relations[door["name"]]
    for room in connected_rooms:
        if (not current_room == room):
            return room


def examine_item(item_name):
    """
    Examine an item which can be a door or furniture.
    First make sure the intended item belongs to the current room.
    Then check if the item is a door. Tell player if key hasn't been
    collected yet. Otherwise ask player if they want to go to the next
    room. If the item is not a door, then check if it contains keys.
    Collect the key if found and update the game state. At the end,
    play either the current or the next room depending on the game state
    to keep playing.
    """
    current_room = game_state["current_room"]
    next_room = ""
    output = None
    for item in object_relations[current_room["name"]]:
        if (item["name"] == item_name):
            output = "You examine the " + item_name + ". "
            if (item["type"] == "door"):
                have_key = False
                for key in game_state["keys_collected"]:
                    if (key["target"] == item):
                        have_key = True
                if (have_key == True and weapon == True):
                    print(
                        "You manage to unlock it, you can feel the fire roaring within the Volcano.\n")
                    input("Press Enter to continue...")
                    next_room = get_next_room_of_door(item, current_room)
                if (have_key == True and weapon == False):
                    print(
                        "You manage to unlock it, you can see the next universe through the portal.\n")
                    next_room = get_next_room_of_door(item, current_room)
                if (have_key == False and weapon == True):
                    print("It is blocked, you need to find a way to unlock it.\n")
                elif (have_key == False and weapon == False):
                    print("It is blocked, you need to find a way to unlock it.\n")

# START room Alicia
# Mad Hatter
            else:
                if (item["name"] in object_relations and len(object_relations[item["name"]]) > 0 and item["name"] == "Mad Hatter"):
                    result_game_key_b = game_key_b()
                    if result_game_key_b == 1:
                        item_found = object_relations[item["name"]].pop()
                        game_state["keys_collected"].append(item_found)
                        os.system('cls')
                        print_mad_hatter()
                        output += "Oh! I saw that rabbit running towards the Castle Portal. \nBut you will need to eat this magic cookie to have the right size and get through that portal.\n"
                        os.system('cls')
                        print_mad_hatter()
                    elif result_game_key_b == 2:
                        output += "A very merry unbirthday to you dear girl!. Try again later"
                    elif result_game_key_b == 3:
                        output += "But you have to enter yes/no. Try again later"
                    else:
                        output += "I haven’t seen that rabbit, ask the Cheshire Cat about it."
# Cheshire Cat
                elif (item["name"] in object_relations and len(object_relations[item["name"]]) > 0 and item["name"] == "Cheshire Cat"):
                    have_key = False
                    for key in game_state["keys_collected"]:
                        if key["target"] == door_b:
                            have_key = True
                    if have_key == True:
                        os.system('cls')
                        print_cat()
                        output += 'We have already spoken, everyone is mad here.\n'
                    else:
                        os.system('cls')
                        print_cat()
                        output += 'If I was looking for a white rabbit...\nI’d ask the Mad Hatter for A BLUE RABBIT.\nThat way we make sure he will help you!\n'


# END room Alicia

# Here starts the room of Vanessa
# Voldemort
                elif (item["name"] in object_relations and len(object_relations[item["name"]]) > 0 and item["name"] == "Voldemort"):
                    result_game_key_c = game_key_c()
                    if result_game_key_c == 1:
                        item_found = object_relations[item["name"]].pop()
                        game_state["keys_collected"].append(item_found)
                        output += "Urrgh! You won this round muggle..\nHere are the coordinates for the Time turner portal.."
                    elif result_game_key_c == 2:
                        output += "You still weak muggle, try again later"
                    elif result_game_key_c == 3:
                        output += "But you have to enter yes/no. Try again later"
                    else:
                        output += "You are weak, when you're able to challenge me come back this way!"
# Dobby

                elif (item["name"] in object_relations and len(object_relations[item["name"]]) > 0 and item["name"] == "Dobby"):
                    have_key = False
                    for key in game_state["keys_collected"]:
                        if key["target"] == door_c:
                            have_key = True
                    if have_key == True:
                        os.system('cls')
                        print_dobby()
                        output += 'I think you already know the Spell. Dobby wants to be free! \n'
                    else:
                        os.system('cls')
                        print_dobby()
                        output += 'You need to be wise..\nIf you want to defeat the one that cannot be named!\nWhat is the most mortiferous spell? It can kill you in a puff!! \n'

# Here finished room of Vanessa

# Amelies groot and key challenge code
                elif (item["name"] in object_relations and len(object_relations[item["name"]]) > 0 and item["name"] == "groot"):
                    result_game_root_key = game_root_key()
                    if result_game_root_key == 1:
                        item_found = object_relations[item["name"]].pop()
                        game_state["keys_collected"].append(item_found)
                        output += "Congratulations! You win! You got the " + \
                            item_found["name"] + "."
                    elif result_game_root_key == 2:
                        output += "But you don't want to play. Try again later"
                    elif result_game_root_key == 3:
                        output += "But you have to enter yes/no. Try again later"
                    else:
                        output += "But your answer is wrong. Try again later"

# Here finished room of Amelie

# Here start Daniel room
# Sword Riddle
                elif (item["name"] in object_relations and len(object_relations[item["name"]]) > 0 and item["name"] == "Narsil"):
                    result_game_sword = game_sword()
                    if result_game_sword == 1:
                        item_found = object_relations[item["name"]].pop()
                        game_state["keys_collected"].append(item_found)
                        os.system('cls')
                        print_sword()
                        output += "Got it, you now yield " + \
                            item_found["name"] + ", the King's Sword."
                    elif result_game_sword == 2:
                        output += "But you don't want to play. Try again later"
                    elif result_game_sword == 3:
                        output += "But you have to enter yes/no. Try again later"
                    else:
                        output += "Your answer is wrong. Try again!"
 # Boss Gollum
                elif (item["name"] in object_relations and len(object_relations[item["name"]]) > 0 and item["name"] == "Gollum"):
                    result_game_boss = boss_battle()
                    if result_game_boss == 1:
                        item_found = object_relations[item["name"]].pop()
                        game_state["keys_collected"].append(item_found)
                        output += "You find the " + item_found["name"] + "."
                    elif result_game_boss == 2:
                        output += "But you don't want to play. Try again later"
                    elif result_game_boss == 3:
                        output += "But you have to enter yes/no. Try again later"
                    elif result_game_boss == 5:
                        output += "Find a weapon, you need to beat the creature!"
                    else:
                        output += "But your answer is wrong. Try again later"
# Here finished room of Daniel

# Changes for the latest version with the name of items
                elif (item["name"] in object_relations and len(object_relations[item["name"]]) > 0 and item["name"] != "Mad Hatter" and item["name"] != "Cheshire Cat" and item["name"] != "Voldemort" and item["name"] != "Dobby" and item["name"] != "groot"):  # Here you need to add your objets
                    item_found = object_relations[item["name"]].pop()
                    game_state["keys_collected"].append(item_found)
                    output += "You find the " + item_found["name"] + "."
                else:
                    output += "There isn't anything interesting about it. \n"
                print(output)
                break
    if (output is None):
        print("The item you requested is not found in the current room.\n")
    if (next_room and weapon == False and input("Do you want to go to the universe? Enter 'yes' or 'no' \n").strip() == 'yes'):
        global print_counter
        print_counter = 0
        os.system('cls')
        play_room(next_room)
    elif (next_room and weapon == True):
        os.system('cls')
        play_room(next_room)
    else:
        play_room(current_room)

# Here is the challege of Daniel


def boss_battle():
    actions = ["fight", "run"]
    global weapon
    os.system('cls')
    print_gollum()
    print("A strange dark-creature lies ahead.\nStanding between you and the entrance to the volcano.\nYou can either run or fight it. What would you like to do? \n")
    userInput = ""
    while userInput not in actions:
        print("Options: run/fight")
        userInput = input()
        if userInput == "fight":
            if weapon:
                os.system('cls')
                print_gollum()
                print("You kill Gollum with Nazril, the sword.\nAfter moving forward, you are able to see the Entrance to Mt Doom.\nKeep going, you are almost there. \n")
                return 1
            elif weapon == False:
                print("\nYou have no way to defend yourself, is too dangerous!\n")
                return 5
        elif userInput == "run":
            print("\nWise decision, but you need to keep going...\n")
            return 5
        else:
            print("Please enter a valid option.")


def game_sword():
    global weapon
    os.system('cls')
    print_sword_grab()
    answer = input(
        '''You reach for the sword.\nBut is hanging in the wall and you hear a voice...\nYou want to grab it? (yes/no): \n''')
    if answer.lower() == 'yes':
        answer = input(
            '''Eerie Voice: a riddle lies ahead..\nIf an elvish sword glows blue, what creature might be close to you? \n''')
        if answer.lower() == 'orcs' or 'goblins' or 'goblin' or 'orc':
            weapon = True
            return 1
        else:
            return 4
    if answer.lower() == 'no':
        return 2
    else:
        return 3


def game_ring():
    os.system('cls')
    print_ending()
    print('''You reached the volcano of Mt Doom!\nThere's something shiny and round in the rock at your feet...\nYou reach for it without hesitation!\n''')
    input("Press Enter to continue...")
    os.system('cls')
    print_ending()
    print('''Sauron: One Ring to rule them all.\nOne Ring to bring them all...\nAnd in the Darkness bind them!\n''')
    input("Press Enter to continue...")
    os.system('cls')
    print_ending()
    answer = input(
        '''The One ring, and the destiny of Middle Earth lies in your hands!\nWill you destroy the ring in the volcano? (yes/no): \n''')
    if answer.lower() == 'yes':
        os.system('cls')
        print_gandalf()
        print('''Gandalf: You have saved Middle Earth... My dear friend!\n''')
        input("Press Enter to continue...")
        os.system('cls')
        print_gandalf()
        print('''A wizard is never late, master traveler. Nor is he early.\nHe arrives precisely when he means to!\n''')
        input("Press Enter to continue...")
    if answer.lower() == 'no':
        os.system('cls')
        print_ending()
        print('''Then... Darkness shall consume us all!!\n''')
        time.sleep(3)

# Here is the end of Daniel


# START FUNCTIONS ALICIA
def game_key_b():  # Here is the challege of Alicia
    os.system('cls')
    mixer.init()
    mixer.music.load('madhatter.mp3')
    mixer.music.play()
    mixer.music.set_volume(0.2)
    print_mad_hatter()
    answer = input(
        'No room in this party! It’s very rude to sit down without being invited.\nDo you want to ask me something? ? (yes/no): \n')
    if answer.lower() == 'yes':
        answer = input('What are you looking for?\n')
        if answer.lower() == 'a blue rabbit':
            return 1
        else:
            return 4
    if answer.lower() == 'no':
        return 2
    else:
        return 3

# END FUNCTIONS ALICIA

# Vanessa Functions


def game_key_c():  # Here is the challege of Vanessa
    os.system('cls')  # Clears the terminal
    print_voldemort()  # Prints Old person Art
    answer = input(
        'Are you sure you want to fight against me muggle? (yes/no):\n')
    if answer.lower() == 'yes':
        os.system('cls')
        print_voldemort()
        answer = input('What is the most mortiferous spell?\n')
        if answer.lower() == 'avada kedavra':
            return 1
        else:
            return 4
    if answer.lower() == 'no':
        return 2
    else:
        return 3
# END Vanessa Functions

# Amelie Functions


def game_root_key():  # Here is the challege of Amelie
    os.system('cls')
    print_groot()
    print('Hello, my name is groot. I am the boss of the guardians of the galaxy Haha!\nI was told to create a key out of my roots, I don´t know why and I nearly forgot it...\n')
    answer = input(
        'I can give it to you if you play a game with me. Are you ready? (yes/no): \n')
    if answer.lower() == 'yes':
        os.system('cls')
        print_groot()
        answer = input(
            'With whom in the room have I been a bounty hunter before we met starlord?\n')
        if answer.lower() == 'rocket':
            return 1
        else:
            return 4
    if answer.lower() == 'no':
        return 2
    else:
        return 3

# END Amelie Functions

# ASCII Prinouts start here


def print_galaxy():
    mixer.init()
    mixer.music.load('groot.mp3')
    mixer.music.play()
    mixer.music.set_volume(0.2)
    print(r"""
    
             You find yourself in an unknown planet far from home....
    
                .                                            .
     *   .                  .              .        .   *          .
  .         .                     .       .           .      .        .
        o                             .                   .
         .              .                  .           .
          0     .
                 .          .                 ,                ,    ,
 .          \          .                         .
      .      \   ,
   .          o     .                 .                   .            .
     .         \                 ,             .                .
               #\##\#      .                              .        .
             #**#O##\###                .                        .
   .        #*#**#\##\###                       .                     ,
        .   ##*#**#\##\##               .                     .
      .      ##*#**#o##\#         .                             ,       .
          .     *#**#\#     .                    .             .          ,
                      \          .                         .
____^/\___^--____/\____O______________/\/\---/\___________---______________
   /\^   ^  ^    ^                  ^^ ^  '\ ^          ^       ---
         --           -            --  -      -         ---  __       ^
   --  __                      ___--  ^  ^                         --  __
   
     """)


def print_hogwarts():
    mixer.init()
    mixer.music.load('hpot.mp3')
    mixer.music.play()
    mixer.music.set_volume(0.2)
    print(r"""     
                 Hogwarts: School of Wizardy
                                                   
                                                 /^\
                   !_                           /   \
                   |*`~-.,                     /,    \
                   |.-~^`                     /#"     \
                   |                        _/##_   _  \_
              _   _|  _   _   _            [ ]_[ ]_[ ]_[ ]
             [ ]_[ ]_[ ]_[ ]_[ ]            |_=_-=_ - =_|
           !_ |_=_ =-_-_  = =_|           !_ |=_= -    |
           |*`--,_- _        |            |*`~-.,= []  |
           |.-'|=     []     |   !_       |_.-"`_-     |
           |   |_=- -        |   |*`~-.,  |  |=_-      |
          /^\  |=_= -        |   |_,-~`  /^\ |_ - =[]  |
      _  /   \_|_=- _   _   _|  _|  _   /   \|=_-      |
     [ ]/,    \[ ]_[ ]_[ ]_[ ]_[ ]_[ ]_/,    \[ ]=-    |
      |/#"     \_=-___=__=__- =-_ -=_ /#"     \| _ []  |
     _/##_   _  \_-_ =  _____       _/##_   _  \_ -    |\
    [ ]_[ ]_[ ]_[ ]=_0~{_ _ _}~0   [ ]_[ ]_[ ]_[ ]=-   | \
    |_=__-_=-_  =_|-=_ |  ,  |     |_=-___-_ =-__|_    |  \
     | _- =-     |-_   | ((* |      |= _=       | -    |___\
     |= -_=      |=  _ |  `  |      |_-=_       |=_    |/+\|
     | =_  -     |_ = _ `-.-`       | =_ = =    |=_-   ||+||
     |-_=- _     |=_   =            |=_= -_     |  =   ||+||
     |=_- /+\    | -=               |_=- /+\    |=_    |^^^|
     |=_ |+|+|   |= -  -_,--,_      |_= |+|+|   |  -_  |=  |
     |  -|+|+|   |-_=  / |  | \     |=_ |+|+|   |-=_   |_-/
     |=_=|+|+|   | =_= | |  | |     |_- |+|+|   |_ =   |=/
     | _ ^^^^^   |= -  | |  <&>     |=_=^^^^^   |_=-   |/
     |=_ =       | =_-_| |  | |     |   =_      | -_   |
     |_=-_       |=_=  | |  | |     |=_=        |=-    |
^^^^^^^^^^`^`^^`^`^`^^^""""""""^`^^``^^`^^`^^`^`^``^`^``^``^^
      
       """)


def print_shelf():
    print(r"""    
           ________________________________________________
  ________|                  __        _   __    _        |_______
  \       |       |\    /|  |  |  | /  |  |__   /_        |      /
   \      |       |  \/  |  |__|  |/   |  |__   __\       |     /
   /      |_______________________________________________|     \
  /__________)                                        (__________\
    
      _________________________________________________________
    ||---------------------------------------------------------||
    ||.--.    .-._                        .----.               ||
    |||==|____| |H|___            .---.___|****|_____.--._____ ||
    |||  |====| | |xxx|_          |+++|=-=|_  _|-=+=-|==|-=+=-|||
    |||==|    | | |   | \         |   |   |_\/_|     Alice    |||
    |||  | HP | | |   |\ \   .--. |   |=-=|_/\_|-=+=-|In|-=+=-|||
    |||  |    | | |   |_\ \_( oo )|   |   |    |  Wonderland  |||
    |||==|====| |H|xxx|  \ \ |''| |+++|=-=|****|-=+=-|==|-=+=-|||
    ||`--^----'-^-^---'   `-' ""  '---^---^----^-----^--^-----^||
    ||-------------------------------------------------------  ||
    ||-------------------------------------------------------  ||
    ||               ___                   .-.__.-----. .---.  ||
    ||              |===| .---.   __   .---| |XX|<(*)>|_|^^^|  ||
    ||         ,  /(|   |_|III|__|''|__|:x:|=|  |     |=| L |  ||
    ||      _a'{ / (|===|+|   |++|  |==|   | |  |I  Am| | O |  ||
    ||      '/\\/ _(|===|-|   |  |''|  |:x:|=|  |Groot| | T |  ||
    ||_____  -\{___(|   |-|   |  |  |  |   | |  |     | | R |  ||
    ||       _(____)|===|+|[I]|--|''|==|:x:|=|XX|<(*)>|=|^^^|  ||
    ||              `---^-^---^--^--'--^---^-^--^-----^-^---^  ||
    ||-------------------------------------------------------  ||
    ||_________________________________________________________||
       
       """)


def print_wonderland():
    print(r"""
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

$$$$$******??*****3$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$c          d$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$???$$$$$$$$$$$$$$$$????$$$
$$$$$$$          $$$$`******)$$$$,`******,$$$P"   . '*** J `****`..    `?$
$$$$$$$  dk      $$$$h      $$$$$$L     ;$$$"   :$$$     dk     J$$>     $
$$$$$$E d$$L     `$$$$     :$$$$$$h     9$$     9$$$h   .$E     9$$L,uzcd$
$$P*** :$$$$.     9$$$     :$$$$$$$     9$F     $$$$$$hd$$E     9P""?$$$$$
P"      "$$$$     `$$$     :$$$?$$$     9$>     $$$$$$$$$$$           `' 9
          "??'     ?$$>    :P"   "$     9$>     $$$$$$$F?$$     ;cc,    z$
c,cdF  .     u     `?$>    :>     4     9$k     9$$$$$$  $$     9$$$?dd???
$$$P  ;$$cccd$k     `$>    :hcd>  d     9$$      ?$$$P"  $E     9$$$
$$$   `$$$$$$$$      ?>    `$$$' ,F     `$$h.           d$"     '$$$>    ,
$$"    `?$$$$$F       ? .   `` ,cP,,,,,,,`$$$c,       ud$" .,,,. '""   ,c$
" .,,,,,,`3$$C,,,uuu,,,2$$$$hd$$$F"3$$$$$$$$$$$$bbcd$$$$$$$$$$$$$$$$h$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$C"JF , `$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$F )L 9; 2$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
***$P??$**$P**?$$**?$)"9F****?$P*****?F*****?E***$$$b****3E""?$>"96****?$$
h  $'  $'," 9$  ?  `?) $$  $h  $  c==?E  ?P ,$  J$$$F c  $$   ?> $$  $h  $
$L ` , ` b  $$  J J,   $$  $P  $  sc==E  c '$$  ?$?$' "  "$ J,   $$  $P  $
$$..9b..J$c,`".zC.?$L..?P  "',d$,.`" ,E..$L..$..`'.F.J$L..I.?$L..?6  "',d$
-------------------------------------------------------------------------- 
      
       """)


def print_title():
    print(r"""
                                              _______________________
   _______________________-------------------                       `\
 /:--__                                                              |
||< > |                                   ___________________________/
| \__/_________________-------------------                        |
|                                                                 |
 |              Welcome to the Multiverse of Blockbuster!         |
 |                                                                 |
 |      Have you ever dreamed of being the hero of your            |
  |       favorite movie?                                          |
  |   Welcome to this multiverse where you can make your dreams     |
  |   come true, you will become the hero of different movies       |
  |   and only with cunning and intelligence you will be able       |
  |   to escape and continue discovering new worlds.                |
  |                                                                |
   |                    Are you ready? Let's go!                   |	                      
   |                                                               |
   |             "May the Force be with you" - Star Wars            |
  |                                              _________________  |_
  |  ___________________-------------------------                      `\
  |/`--_                                                                 |
  ||[ ]||                                            ___________________/
   \===/___________________--------------------------
    """)


def print_dobby():
    print(r"""
       _____
      /     \
    /- (*) |*)\
    |/\.  _>/\|
        \__/    |\
       _| |_   \-/
      /|\__|\  //
     |/|   |\\//
     |||   | ~'
     ||| __|
     /_\| ||
     \_/| ||
       |7 |7
       || ||
       || ||
       /\ \ \   
      ^^^^ ^^^
    """)


def print_voldemort():
    print(r""" 
                            ''''
                           :o  o:
                           : .. :
                           _:"":\___
            ' '      ____.' :::     '._
           . *=====<<=)           \    :
            .  '      '-'-'\_      /'._.'
                             \====:_ ""
                            .'     \\
                           :       :
                          /   :    \
                         :   .      '.
         ,. _            :  : :      :
      '-'    ).          :__:-:__.;--'
    (        '  )        '-'   '-'
    
    """)


def print_gandalf():
    mixer.init()
    mixer.music.load('gandalf.mp3')
    mixer.music.play()
    mixer.music.set_volume(0.2)
    print(r""" 
                         ,-----.
                        /      |
                       /       |
                  ___,'        |
                <  -'          :
                 `-.__..--'``-,_\_
                    |o/ ` o  )_`>
                    :/ `     ||/)
                    (_.).__,-` |\
                    /( `.``   `| :
                    \'`-.)  `  ; ;
                    | `       /-<
                    |     `  /   `.
    ,-_-..____     /|  `    :__..-'\
   /,'-.__\\  ``-./ :`      ;       \
   `\ `\  `\\  \ :  (   `  /  ,   `. \
     \` \   \\   |  | `   :  :     .\ \
      \ `\_  ))  :  ;     |  |      ): :
     (`-.-'\ ||  |\ \   ` ;  ;       | |
      \-_   `;;._   ( `  /  /_       | |
       `-.-.// ,'`-._\__/_,'         ; |
          \:: :     /     `     ,   /  |
    
    """)


def print_mad_hatter():
    print(r""" 
                              ,.--""-._
                            __/         `.
                       _,**"   "*-.       `.
                     ,'            `.       \
                    ;    _,.---._    \  ,'\  \
                   :   ,'   ,-.. `.   \'   \ :
                   |  ;_\  (___)`  `-..__  : |
                   ;-'`o'"  `o'    `--._ ` | ;
                  /,-'/  -.        `---.`  |"
                  /_,'`--='.       `-.._,-" _
                   (/\\,--. \    ___-.`:   //___
                      /\'''\ '  |   |-`|  ( -__,'
                     '. `--'    ;   ;  ; ;/_/
                       `. `.__,/   /_,' /`.~;
                       _.-._|_/_,'.____/   /
                  ..--" /  =/  \=  \      /
                 /  ;._.\_.-`--'-._/ ____/
                 \ /   /._/|.\     ."
                  `*--'._ "-.:     :
                       :/".A` \    |
                       |   |.  `.  :
                       ;   |.    `. \
    
    """)


def print_cat():
    print(r""" 
                 .'\   /`.
               .'.-.`-'.-.`.
          ..._:   .-. .-.   :_...
        .'    '-.(o ) (o ).-'    `.
       :  _    _ _`~(_)~`_ _    _  :
      :  /:   ' .-=_   _=-. `   ;\  :
      :   :|-.._  '     `  _..-|:   :
       :   `:| |`:-:-.-:-:'| |:'   :
        `.   `.| | | | | | |.'   .'
          `.   `-:_| | |_:-'   .'
             `-._   ````    _.-'
                 ``-------''
    
    """)


def print_groot():
    print(r"""     
            .^. .  _    
           /: ||`\/ \~  ,       
        , [   &    / \ y'   
       {v':   `\   / `&~-,  
       'y. '    |`   .  ' /   
       \   '  .       , y   
        v .        '     v   
        V  .~.      .~.  V   
        : (  0)    (  0) :   
         i `'`      `'` j     
          i     __    ,j     
           `%`~....~'&         
        <~o' /  \/` \-s,        
        o.~'.  )(  r  .o ,.  
        o',  %``\/``& : 'bF  
       d', ,ri.~~-~.ri , +h  
       `oso' d`~..~`b 'sos`  
            d`+ II +`b              
            i_:_yi_;_y          
     
     """)


def print_sword_grab():
    print(r"""
    
               )         
              (            
            '    }      
            (    '      
           '      (   
            )  |    ) 
          '   /|\    `
         )   / | \  ` )   
        {    | | |  {   
       }     | | |  .
        '    | | |    )
       (    /| | |\    .
        .  / | | | \  (
      }    \ \ | / /  .        
       (    \ `-' /    }
       '    / ,-. \    ' 
        }  / / | \ \  }
       '   \ | | | /   } 
        (   \| | |/  (
          )  | | |  )
          .  | | |  '
             J | L
       /|    J_|_L    |\
       \ \___/ o \___/ /
        \_____ _ _____/
              |-|
              |-|
              |-|
             ,'-'.
             '---'   

    """)


def print_sword():
    print(r"""
                       \ : /
                    '-: __ :-'
                    -:  )(_ :--
                    -' |r-_i'-
            ,sSSSSs,   (2-,7
            sS';:'`Ss   )-j
           ;K 0 (0 s7  /  (
            S, ''  SJ (  ;/
            sL_~~_;(S_)  _7
|,          'J)_.-' />'-' `Z
j J         /-;-A'-'|'--'-j\
 L L        )  |/   :    /  \
  \ \       | | |    '._.'|  L
   \ \      | | |       | \  J
    \ \    _/ | |       |  ',|
     \ L.,' | | |       |   |/
    _;-r-<_.| \=\    __.;  _/
      {_}"  L-'  '--'   / /|
            |   ,      |  \|
            |   |      |   ")
            L   ;|     |   /|
           /|    ;     |  / |
          | |    ;     |  ) |
         |  |    ;|    | /  |
         | ;|    ||    | |  |
         L-'|____||    )/   |
             % %/ '-,- /    /
             |% |   \%/_    |
          ___%  (   )% |'-; |
        C;.---..'   >%,(   "'
                   /%% /
                  Cccc'     

    """)


def print_ending():
    print(r"""
                       \ : /
                    '-:  _ :-'
                    -:  (_) :--
                      -'  _'-
            ,sSSSSs,   (2-,7
            sS';:'`Ss   )-j
           ;K 0 (0 s7  /  (
            S, ''  SJ (  ;/
            sL_~~_;(S_)  _7
            'J)_.-' />'-' `Z
            /-;-A'-'|'--'-j\
            )  |/   :    /  \
            | | |    '._.'|  L
            | | |       | \  J
           _/ | |       |  ',|
        .,' | | |       |   |/
       r-<_.| \=\    __.;  _/
      {_}"  L-'  '--'   / /|
            |   ,      |  \|
            |   |      |   ")
            L   ;|     |   /|
           /|    ;     |  / |
          | |    ;     |  ) |
         |  |    ;|    | /  |
         | ;|    ||    | |  |
         L-'|____||    )/   |
             % %/ '-,- /    /
             |% |   \%/_    |
          ___%  (   )% |'-; |
        C;.---..'   >%,(   "'
                   /%% /
                  Cccc'     

    """)


def print_gollum():
    print(r"""
                       _..
                    .'   `",
                   ;        \
            .---._; ^,       ;
         .-'      ;{ :  .-. ._;
    .--""          \*'   o/ o/
   /   ,  /         :    _`";
  ;     \;          `.   `"+'
  |      }    /    _.'T"--"\
  :     /   .'.--""-,_ \    ;
   \   /   /_         `,\   ;
    : /   /  `-.,_      \`.  :
    |;   {     .' `-     ; `, \
    : \  `;   {  `-,__..-'   \ `}+=,
     : \  ;    `.   `,        `-,\"
     ! |\ `;     \}?\|}
  .-'  | \ ;
.'}/ i.'  \ `,                           
``''-'    /   \
         /J|/{/
           `'        
    """)


def print_lotr():
    mixer.init()
    mixer.music.load('lotr.mp3')
    mixer.music.play()
    mixer.music.set_volume(0.2)
    print(r"""
 ______________     __             _,-----------._        ___
|              |   (_,.-      _,-'_,-----------._`-._    _)_)
| THE _  _  _  |      |     ,'_,-'  ___________  `-._`.
| |  / \|_)| \ |     `'   ,','  _,-'___________`-._  `.`.
| |__\_/| \|_/ |        ,','  ,'_,-'     .     `-._`.  `.`.
|              |       /,'  ,','        >|<        `.`.  `.\
| OF THE  _ _  |      //  ,','      ><  ,^.  ><      `.`.  \\
| |_)||\|/_(_  |     //  /,'      ><   / | \   ><      `.\  \\
| | \|| |\_|_) |    //  //      ><    \/\^/\/    ><      \\  \\
|______________|   ;;  ;;              `---'              ::  ::
                   ||  ||              (____              ||  ||
 DOOR TO MORDOR   _||__||_            ,'----.            _||__||_
                 (o.____.o)____        `---'        ____(o.____.o)
                   |    | /,--.)                   (,--.\ |    |
                   |    |((  -`___               ___`   ))|    |
                   |    | \\,'',  `.           .'  .``.// |    |
                   |    |  // (___,'.         .'.___) \\  |    |
                  /|    | ;;))  ____) .     . (____  ((\\ |    |\
                  \|.__ | ||/ .'.--.\/       `/,--.`. \;: | __,|;
                   |`-,`;.| :/ /,'  `)-'   `-('  `.\ \: |.;',-'|
                   |   `..  ' / \__.'         `.__/ \ `  ,.'   |
                   |    |,\  /,                     ,\  /,|    |
                   |    ||: : )          .          ( : :||    |
                  /|    |:; |/  .      ./|\,      ,  \| :;|    |\
                  \|.__ |/  :  ,/-    <--:-->    ,\.  ;  \| __,|;
                   |`-.``:   `'/-.     '\|/`     ,-\`;   ;'',-'|
                   |   `..   ,' `'       '       `  `.   ,.'   |
                   |    ||  :                         :  ||    |
                   |    ||  |                         |  ||    |
                   |    ||  |                         |  ||    |
                   |    |'  |            _            |  `|    |
                   |    |   |          '|))           |   |    |
                   ;____:   `._        `'           _,'   ;____:
                  {______}     \___________________/     {______}
                  |______|_______________________________|______|
     
     """)


game_state = INIT_GAME_STATE.copy()

os.system('mode con: cols=87 lines=40')

# Intro sound
mixer.init()
mixer.music.load('fox.mp3')
mixer.music.play()
mixer.music.set_volume(0.2)
# End intro sound

print_title()
time.sleep(2)
input("Press Enter to continue...")
start_game()
