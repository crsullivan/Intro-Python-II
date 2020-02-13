# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, place):
        self.name = name
        self.place = place

    def __str__(self):
        print(f"{self.name}\n{self.place}")
