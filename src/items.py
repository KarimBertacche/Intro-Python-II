class Item:
    def __init__(self, name, description = ""):
        self.name = name
        self.description = description

    def on_take(self, player):
        print(f"\n{player} you have picked up {self.name}\n")

    def on_drop(self, player, room):
        print(f"\n{player} you have dropped {self.name} in {room}\n")
    