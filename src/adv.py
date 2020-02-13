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

player = input("Who are you? ")
location = "outside"
player_info = Player(room[location],player)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

print('\nWelcome, {player}. An adventure awaits you,\nshould you choose to accept it.')

print('\n{player}, {player.location}')

game = True 
player_input = input("Where would you like to go> [n] North [e] East [s] South [w] West [q] Quit")
player_input = player_input.split(" ")
intro = True
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while game:
    if intro:
        print("Watch your step.")
        intro = False
        print("You have entered the {player.location.name} room, from here you can see {player.location.description}.")
        direction = input(player_input)
        if direction == "n":
            ## go north
            pass
        if direction == "e":
            ## go east
            pass
        if direction == "s":
            ## go south
            pass
        if direction == "w":
            ## go west
            pass
        if direction == "q":
            ## quit game
            pass