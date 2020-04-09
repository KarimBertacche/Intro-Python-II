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
            print("-------------")
            print(f"\nYou entered {self.current_room}")
        else:
            print("-------------")
            print("\nYou shall not pass!✨🧙‍♂️\n")

    def pick(self, chosen_item):
        room_items = self.current_room.items
        for item in room_items:
            if item == chosen_item:
                self.inventory.append(item)
                room_items.remove(item)
                print("-------------")
                print(f"\n{self.name} you have picked {item}\n")
                print(f"\nYou're in {self.current_room}")
            else:
                print("-------------")
                print(f"\nThere is no {chosen_item} in {self.current_room.name}")