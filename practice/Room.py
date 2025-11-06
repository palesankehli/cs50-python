Class Room:

  def __init__(self, name, description, exits, items):
    self.name = name
    self.description = description
    self.exits = exits
    self.items = items





room = Room("liberty", 
            "You are in the Restricted Section of the Hogwarts Library",
            {"north": "Potion Storeroom", "west": "Potion Storeroom"},
            ["glowing book", "umese"])