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

    def get(self, chosen_item):
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

    def drop(self, chosen_item):
        room_items = self.current_room.items
        player_items = self.inventory
        for item in player_items:
            if item == chosen_item:
                room_items.append(item)
                player_items.remove(item)
                print("-------------")
                print(f"\n{self.name} you have dropped {item} in {self.current_room.name}\n")
                print(f"\nYou're in {self.current_room}")
            else:
                print("-------------")
                print(f"\nThere is no {chosen_item} in your inventory")
                print("\nPlease chose an item from this list to drop:\n")
                self.show_inventory()
        
    def show_inventory(self):
        if len(self.inventory) >= 1:
            for item in self.inventory:
                print(f"> {item}")
        else:
            print("> No items available")
                
    