# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, in_room, items):
        self.name = name
        self.in_room = in_room
        self.items = items
