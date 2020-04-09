import textwrap

from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside': Room(
        "Outside Cave Entrance",
        "North of you, the cave mount beckons"
    ),
    'foyer': Room(
        "Foyer", 
        """Dim light filters in from the south. Dusty passages run north and east."""
    ),
    'overlook': Room(
        "Grand Overlook", 
        """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."""
    ),
    'narrow': Room(
        "Narrow Passage", 
        """The narrow passage bends here from west to north. The smell of gold permeates the air."""
    ),
    'treasure': Room(
        "Treasure Chamber", 
        """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""
    ),
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
player = Player(input("Please enter your name: "), room["outside"])

#REPL ==> Read, Evaluate, Print, Loop
print(f"\nYou are {player.current_room.name}\n{player.current_room.description}\n")

while True:
    print("\nWhere to next?\n  Type -> [n, s, e, w] or [q] to exit")
    print("  To pick item from the room, or type >>> (p)ick <object_name>")
    print("  To drop item into the room, or type >>> (d)rop <object_name>\n")
    command = input("~~~~> ")

    if command == "q":
        print(f"\nBye {player.name} 👋😁\n")
        exit()
    elif command in ("n", "s", "e", "w"):
        player.travel(command)
    elif len(command) > 1:
        cmd = command.split(' ')
        item_name = cmd[1].strip()
        if cmd[0] == "p" or cmd[0] == "pick":
            player.get(item_name)
    else:
        print("\nCan't understand your command, please choose valid keys such as [n, s, e, w] or [q] to exit.\n")