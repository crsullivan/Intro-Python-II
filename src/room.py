# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        stuff = f"Room name: {self.name} \nDescription: {self.description} \nItems: "
        if len(self.items)>0:
            for i in self.items:
                stuff += f" {i}"
        else:
            stuff += "None"
        return stuff
    
    def __str__(self):
        return f"You enter the {self.name} room and see {self.description}"