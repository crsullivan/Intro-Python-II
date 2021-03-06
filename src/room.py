# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items, baddies, weapons):
        self.name = name
        self.description = description
        self.items = items
        self.baddies = baddies
        self.weapons = weapons
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
    
    def __str__(self):
        stuff = f"\n Items here: "
        if len(self.items)>0:
            for i in self.items:
                stuff += f" {i}"
        else:
            stuff += "None"
        enemies = f"\n Enemies here: "
        if len(self.baddies)>0:
            for i in self.baddies:
                enemies += f" {i}"
                print("ENEMIES", enemies)
        else:
            enemies += "None"
        weps = f"\n Weapons here: "
        if len(self.baddies)>0:
            for i in self.weapons:
                weps += f" {i}"
        else:
            weps += "None"
        return f"\nYou enter the {self.name} and see {self.description} \n {stuff} \n {enemies} \n {weps}"

    # def __str__(self):
    #     stuff = f"\nEnemies here: "
    #     if len(self.baddies)>0:
    #         for i in self.baddies:
    #             stuff += f" {i}"
    #     else:
    #         stuff += "None"

    #     return f"\n{stuff}"