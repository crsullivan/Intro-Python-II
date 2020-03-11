from room import Room
from player import Player
from items import Items
from baddies import Baddies
import random
# Declare all the rooms

room = {
    'forest':  Room("Charred Forest", """This burnt forest is surrounded on all sides by canyon walls, except one.. The canyon winds to the west, the same direction you heard that   scream.""", [], []),

    'outside':  Room("Outside Cave Entrance", """North of you, a cave mount beckons, to the east lies the charred forest you awakened in.""", [], []),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east.""", [], []),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in
        the distance, but there is no way across the chasm.""", [], []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air.""", [], []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south.""", [], []),
}

for item in Items:
    room[random.choice(list(room.keys()))].items.append(Items[item])

for baddie in Baddies:
    room[random.choice(list(room.keys()))].baddies.append(Baddies[baddie])

# Link rooms together
room['forest'].w_to = room['outside']
room['outside'].n_to = room['foyer']
room['outside'].e_to = room['forest']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player_name = input("\n Who are you? ")

print(f'\n   {player_name}, you awaken to the faint scent of brimstone and lingering smoke. As you lie in the dirt you try to recall how you got to this place, but your mind is racing, and your thoughts escape you.\n\n   Where you are you do not know. However this place, it seems somewhat familiar... \n\n   You stand up and look around, the forest around you, or at least what remains is burnt and charred, all that lies in many places is ash. \n\n   You feel around in your pockets, nothing, nothing... There! Something in your left breast pocket, the one you never use.... A compass, hopefully it comes in handy.   \n\n   At this moment something unmistakeable catches your ear, a scream.\n\n   Not a horror movie theme park thriller scream either, this is bloodcurdling, throaty, desperate, a fight for your life kind of scream.\n\n   Your goose bumps have goose bumps, the hairs on your neck bristle so hard you feel you shirt lift up ever so slightly. \n\n   You take out your compass, the scream came from the west. \n\n   {player_name}, what do you do?  \n')
# player_agree = input("Well? What say you? [y] Yes [n] No\n " )
# player_agree = player_agree.split(" ")   
# choice = input(player_agree)    
# if choice == "y":
#     print("\nVery good, your cooperation is, well, appreciated")
# else: 
#     print("\nThats really too bad.. For you. You don't seem to have a choice, something beckons you forward")

player = Player(player_name, room["forest"])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.


# print(f'\nBefore you lies the {location}, as you look around you can see {player_info.room.description}.')

game = True 
intro = True
continue_game = True

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# trying to set this while loop to keep iterating even if the user provides invalid input instead of forcing them to reopen the file

print("\n Watch your step...\n")
print(player.location)
while True:
    print("\nWhat would you like to do? [n] Go North [e] Go East [s] Go South [w] Go West [get (item)] Pick up item [i] Check inventory [q] Quit")
    cmd = input("-> ").split(" ")
    if len(cmd) >= 2:
        if cmd[0].lower() == 'get' or cmd[0].lower() == 'take':
            for i in range(len(player.location.items)):
                item = player.location.items[i]
                if cmd[1].lower() == item.name.lower():
                    player.items.append(player.location.items.pop(i))
                    item.pickup()
                    # print(player.items[0].name)
                    break
        elif cmd[0].lower() == 'drop':
            for i in range(len(player.items)):
                item = player.items[i]
                if cmd[1].lower() == item.name.lower():
                    player.location.items.append(player.items.pop(i))
                    item.drop()
                    break
    elif cmd[0].lower() in ["n", "s", "e", "w"]:
        player.travel(cmd[0])
    elif cmd[0].lower() == "q":
        print("Thanks for playing sully's wild ride!")
        exit()
    else:
        print("That doesn't look like a valid command.... look at your keyboard this time and try again")
