from location import Location
from tile import Tile

class Creature():
    TANK = 0
    MAGE = 1
    NINJA = 2
    SNIPER = 3

    def __init__(self, name, type, player, location):
        
        self.set_name(name)
        self.map = None
        self.location = location     # most-recent location
        self.destroyed = False   # flag if character is destroyed
        self.set_type(type)      # creature type, defines movement and attack
        self.player = player
        #self.set_hp()

    
            
    def get_hp(self):
        return self.hp
        
    
    def set_name(self, name):
        
        if not name:
            self.name = "Incognito"
        else:
            self.name = name


    def get_name(self):
        
        return self.name



    def set_type(self, type):
        
        self.type = type


    def get_type(self):
        
        return self.type
    
    def take_damage(self, amount):
        self.print_msg("{} took {} damage!".format(self.name, amount))
        if self.hp > amount:
            self.hp -= amount
        else:
            self.hp = 0
            self.destroy()
            self.print_msg("{} is dead!".format(self.name))


    def get_map(self):
        
        return self.map


    def get_location(self):
        
        return self.location


    def get_tile(self):
        
        return self.get_map().get_tile(self.get_location())



    def destroy(self):
        
        self.destroyed = True
        self.map.get_tile(self.location).remove_creature()
        self.map.creatures.remove(self)
        self.player.team.remove(self)



    def is_dead(self):
        
        return self.destroyed



    def set_map(self, map, location):
        
        target_tile = map.get_tile(location)
        if not target_tile.is_empty() or self.get_map() is not None:
            return False
        else:
            self.map = map
            self.location = location
            return True
    

    def __str__(self):
        return self.get_name() + ' at location ' + str(self.get_location())
    
    
class Tank(Creature):
       
    def __init__(self, name, player, location):
        super().__init__(name, Creature.TANK, player, location)
        self.hp = 30
    
    def movement_squares(self):
        squares = []
        location = self.location
        for x in range(location.x - 2, location.x + 3):
            for y in range(location.y - 2, location.y + 3):
                if self.map.contains(Location(x, y)) and self.map.get_tile(Location(x, y)).is_empty():
                    squares.append(self.map.get_tile(Location(x, y)))
        return squares
    
    def attack_squares(self):
        squares = []
        location = self.location
        for x in range(location.x - 1, location.x + 2):
            for y in range(location.y - 1, location.y + 2):
                if x == location.x and y == location.y:
                    continue
                if self.map.contains(Location(x, y)) and self.map.get_tile(Location(x, y)).type == Tile.FREE:
                    squares.append(self.map.get_tile(Location(x, y)))
        return squares
    
    def attack(self, location):
        creature = self.map.get_tile(location).get_creature()
        if creature != None:
            creature.take_damage(10)
    
    
class Mage(Creature):
    
    def __init__(self, name, player, location):
        super().__init__(name, Creature.MAGE, player, location)
        self.hp = 10
    
    def movement_squares(self):
        squares = []
        location = self.location
        for x in range(location.x - 1, location.x + 2):
            for y in range(location.y - 1, location.y + 2):
                if self.map.contains(Location(x, y)) and self.map.get_tile(Location(x, y)).is_empty():
                    squares.append(self.map.get_tile(Location(x, y)))
        return squares
    
    def attack_squares(self):
        squares = []
        location = self.location
        for x in range(location.x - 4, location.x + 5):
            if x in range(location.x - 1, location.x + 2):
                    continue
            if self.map.contains(Location(x, location.y)) and self.map.get_tile(Location(x, location.y)).type != Tile.ROCK:
                squares.append(self.map.get_tile(Location(x, location.y)))
        for y in range(location.y - 4, location.y + 5):
            if y in range(location.y - 1, location.y + 2):
                    continue
            if self.map.contains(Location(location.x, y)) and self.map.get_tile(Location(location.x, y)).type != Tile.ROCK:
                squares.append(self.map.get_tile(Location(location.x, y)))
        return squares
    
    def attack(self, location):
        for x in range(location.get_x() - 1, location.get_x() + 2):
            for y in range(location.get_y() - 1, location.get_y() + 2):
                if self.map.contains(Location(x,y)) and self.map.get_tile(Location(x, y)).type != Tile.ROCK:
                    self.map.get_tile(Location(x, y)).set_on_fire()
    
class Ninja(Creature):
    
    def __init__(self, name, player, location):
        super().__init__(name, Creature.NINJA, player, location)
        self.hp = 20
        
    def movement_squares(self):
        squares = []
        directions = [[1, 1], [-1, 1], [-1, -1], [1, -1]]
        location = self.location
        for direction in directions:
            step = 1
            while (1):
                next = Location(location.x + (direction[0] * step), location.y + (direction[1] * step))
                if self.map.contains(next) and self.map.get_tile(next).is_empty():
                    squares.append(self.map.get_tile(next))
                else:
                    break
                step = step + 1
        return squares
    
    def attack_squares(self):
        squares = []
        location = self.location
        for x in range(location.x - 1, location.x + 2):
            for y in range(location.y - 1, location.y + 2):
                if x == location.x and y == location.y:
                    continue
                if self.map.contains(Location(x, y)) and self.map.get_tile(Location(x, y)).type == Tile.FREE:
                    squares.append(self.map.get_tile(Location(x, y)))
        return squares
        
    
    def attack(self, location):
        creature = self.map.get_tile(location).get_creature()
        if creature != None:
            creature.take_damage(5)
    
    
class Sniper(Creature):
    
    def __init__(self, name, player, location):
        super().__init__(name, Creature.SNIPER, player, location)
        self.hp = 10
        
    def movement_squares(self):
        squares = []
        location = self.location
        for x in range(location.x - 1, location.x + 2):
            for y in range(location.y - 1, location.y + 2):
                if self.map.contains(Location(x, y)) and self.map.get_tile(Location(x, y)).is_empty():
                    squares.append(self.map.get_tile(Location(x, y)))
        return squares
    
    def attack_squares(self):
        squares = []
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        location = self.location
        for direction in directions:
            step = 1
            while (1):
                next = Location(location.x + (direction[0] * step), location.y + (direction[1] * step))
                if self.map.contains(next) and self.map.get_tile(next).type == Tile.FREE:
                    squares.append(self.map.get_tile(next))
                else:
                    break
                step = step + 1
        return squares
    
    def attack(self, location):
        creature = self.map.get_tile(location).get_creature()
        if creature != None:
            creature.take_damage(5)