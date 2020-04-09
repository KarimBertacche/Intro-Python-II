# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def travel(self, direction):
        if getattr(self.current_room, f"{direction}_to") is not None:
            self.current_room = getattr(self.current_room, f"{direction}_to")
            print(self.current_room)
        else:
            print("-------------")
            print("\nYou shall not pass!✨🧙‍♂️\n")

    def pick(self, chosen_item):
        for item in self.current_room.items:
            if item == chosen_item:
                self.inventory.append(item)
            else:
                print(f"There is no {chosen_item} in the {self.current_room}")