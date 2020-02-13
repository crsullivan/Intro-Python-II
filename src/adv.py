from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


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

def travel(to_location):
    if to_location != None:
        player.location = to_location
    else:
        print("Something doesn't look right up ahead... No you can't go that way. You turn around and head back.") 

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
    print("Where would you like to go? [n] North [e] East [s] South [w] West [q] Quit")
    cmd = input("-> ").lower()
    if cmd in ["n", "s", "e", "w"]:
        # Move to that room
        player.travel(cmd)
    elif cmd == "q":
        print("Thanks for playing sully's wild ride!")
        exit()
    else:
        print("That doesn't look like a valid command.... look at your keyboard this time and try again")
