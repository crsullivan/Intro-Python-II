class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def pickup(self):
        print(f'\n You picked up {self.name}... Hopefully it will come in handy\n')

    def drop(self):
        print(f'\n You tossed {self.name}')

    def __str__(self):
        return f'\nItem: {self.name}\nItem Description: {self.description}'
