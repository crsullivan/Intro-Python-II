class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def pickup(self, item):
        return f'\n You found {item}... Hopefully it will come in handy\n'

    def __str__(self):
        return f'Item: {self.name}\nItem Description: {self.description}'
