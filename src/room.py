# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"name: {self.name}, description: {self.description}"

room = Room("Only Cow", "Great room with awesome things in it, bigly and great")

print(room)