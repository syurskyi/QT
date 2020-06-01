class Tile():
    
    FREE = 0
    TREE = 1
    ROCK = 2

    def __init__(self, location, tile_type = FREE):
        
        self.creature = None     # most-recent holder (None if no robot in square)
        self.type = tile_type  # flag (one-way currently, since walls can not be removed)
        self.location = location
        self.on_fire = 0


    def set_type(self, type):
        self.type = type
        
    def get_creature(self):
        return self.creature
    
    def set_on_fire(self):
        self.on_fire = 4 #number of turns left on fire
        self.type = Tile.FREE


    def get_type(self):
        return self.type


    def is_empty(self):
        
        if self.type == Tile.FREE:
            if self.creature == None:
                return True
        return False


    def set_creature(self, creature):
        
        if self.is_empty():
            self.creature = creature
            return True
        else:
            return False


    def remove_creature(self):
        
        removed = self.get_creature()
        self.creature = None
        return removed

