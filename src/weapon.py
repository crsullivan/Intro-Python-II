class Weapon:
    def __init__(self, name, description, damage):
        self.name = name
        self.description = description
        self.damage = damage

    def pickup(self):
        print(f'\n You picked up {self.name}... Hopefully it will come in handy\n')

    def drop(self):
        print(f'\n You tossed {self.name}')

    def __str__(self):
        return f'\n Weapon: {self.name}\n Weapon Description: {self.description}'