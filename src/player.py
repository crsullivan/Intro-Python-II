# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.items = []

    def travel(self, direction):
        next_room = getattr(self.location, f"{direction}_to")
        if next_room is not None:
            self.location = next_room
            print(self.location)
        else:
            print("You cannot move in that direction")

    def __str__(self):
        return f"{self.name}\n{self.location}"
