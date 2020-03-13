class Weapon:
    def __init__(self, name, description, damage):
        self.name = name
        self.description = description
        self.damage = damage

    def equip(self):
        print(f'\n You equipped {self.name}... Hopefully it will come in handy\n')


    def __str__(self):
        return f'\n Weapon: {self.name}\n Weapon Description: {self.description}'