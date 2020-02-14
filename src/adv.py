from room import Room
from player import Player
from items import Items
import random
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", []),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", []),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),
}

for item in Items:
    room[random.choice(list(room.keys()))].items.append(Items[item])

# Link rooms together

room['outside'].n_to = room['foyer']
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

player_name = input("\nWho are you? ")

print(f'\nWelcome, {player_name}. An adventure awaits you\nshould you choose to accept it.\n')
# player_agree = input("Well? What say you? [y] Yes [n] No\n " )
# player_agree = player_agree.split(" ")   
# choice = input(player_agree)    
# if choice == "y":
#     print("\nVery good, your cooperation is, well, appreciated")
# else: 
#     print("\nThats really too bad.. For you. You don't seem to have a choice, something beckons you forward")

player = Player(player_name, room["outside"])

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

print("\nWatch your step...\n")
print(player.location)
while True:
    print("\nWhat would you like to do? [n] Go North [e] Go East [s] Go South [w] Go West [p] Pick up item [q] Quit")
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
