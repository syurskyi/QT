from tile import Tile
from location import Location

class Map():
    


    def __init__ (self, filename):
        
        with open(filename, 'r') as file:
            firstline = file.readline()
            # files in format that first line contains dimensions
            self.width = int(firstline.split()[0])
            self.height = int(firstline.split()[1])
        
            # initialises array
            self.tiles = [None] * self.width
            for x in range(self.get_width()):
                self.tiles[x] = [None] * self.height
                    
            # places tiles according to file
            for y in range(self.get_height()):
                line = file.readline()
                for x in range(self.get_width()):
                    self.tiles[x][y] = Tile(Location(x, y), int(line[x]))
        self.creatures = []
        self.turn = 0



    def get_width(self):
        
        return self.width


    def get_height(self):
        
        return self.height


    def add_creature(self, creature, location):
        
        if creature.set_map(self, location):
            self.creatures.append(creature)
            self.get_tile(location).set_creature(creature)
            return True
        else:
            return False


    def get_tile(self, location):
        return self.tiles[int(location.get_x())][int(location.get_y())]


    def get_number_of_creatures(self):
        
        return len(self.creatures)


    def get_creature(self, location):
        
        for creature in self.creatures:
            if location.x == creature.location.x and location.y == creature.location.y:
                return creature
        return None


    def get_next_creature(self):
        
        if self.get_number_of_creatures() < 1:
            return None
        else:
            return self.creatures[self.turn]


    def next_creature_turn(self):
        
        current = self.get_next_creature()
        if current is not None:
            self.turn = (self.turn + 1) % self.get_number_of_creatures()
            current.take_turn()


    def next_full_turn(self):
        
        for count in range(self.get_number_of_creatures()):      # stepper
            self.next_creature_turn()


    def contains(self, location):
        
        x_coordinate = location.get_x()
        y_coordinate = location.get_y()
        return 0 <= x_coordinate < self.get_width() and 0 <= y_coordinate < self.get_height()


    def get_creatures(self): #maybe make player specific?
        
        return self.creatures[:]
    
    def reduce_fire_counter(self):
        for y in range(self.get_height()):
                for x in range(self.get_width()):
                    if self.tiles[x][y].on_fire > 0:
                        self.tiles[x][y].on_fire -= 1
                        creature = self.tiles[x][y].get_creature()
                        if creature != None:
                            creature.take_damage(5)
                        '''if self.tiles[x][y].on_fire == 0:
                            self.tiles[x][y].type = Tile.FREE'''
    
    def set_console(self, console):
        for creature in self.creatures:
            creature.print_msg = console
    
    
        
