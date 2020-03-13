# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, location, *items):
        self.name = name
        self.location = location
        self.items = []
        self.hp = 100

    def travel(self, direction):
        next_room = getattr(self.location, f"{direction}_to")
        if next_room is not None:
            self.location = next_room
            print(self.location)
        else:
            print("Something doesn't look right up ahead... No you can't go that way. You turn around and head back.")

    def inventory(self):
        stuff = f"\n Inventory: "
        if self.items != []:
            for i in self.items:
                print("Inventory:", i)
        elif self.items == []:
            print("Inventroy Empty")



    def __str__(self):
            return f"{self.name}\n{self.location}"