from creature import Creature
from location import Location
from math import sqrt

class Player():
    
    HUMAN = 0
    AI = 1
    
    def __init__(self, side, type):
        self.team = []
        self.side = side # player 1 or 2
        self.type = type
        
    def add_teammember(self, creature):
        self.team.append(creature)

    def ai_turn(self, opponent):
        # ai plays turn
        # move
        list = self.possible_attacks()
        moved = self.fire_check()
        if not moved:
            moved = self.mage_or_sniper_in_danger()
        if not moved:
            move_candidates = []
            # move cratures that can't attack currently
            for creature in list:
                if len(list[creature]) == 0:
                    move_candidates.append(creature)
            # move to attack range if possible
            moved = self.move_to_attack_range(move_candidates)
            if not moved: # move tank or ninja closer to opponent
                for creature in move_candidates:
                    if not moved:
                        if creature.type == Creature.TANK or creature.type == Creature.NINJA:
                            self.move_closer(creature, opponent)
                            moved = True
            if not moved: # move tank or ninja closer to opponent
                for creature in move_candidates:
                    if not moved:
                        if creature.type == Creature.MAGE or creature.type == Creature.SNIPER:
                            self.move_closer(creature, opponent)
                            moved = True
                
        #attack
        list = self.possible_attacks() #update list after moving
        attacked = False
        for creature in list:
            if not attacked and len(list[creature]) != 0:
                if creature.type == Creature.MAGE:
                    final = None
                    for target in list[creature]:
                        if final == None or target.get_creature().get_hp() < final.get_creature().get_hp():
                            final = target
                    creature.attack(final.location)
                    attacked = True
        if not attacked:
            for creature in list:
                if len(list[creature]) != 0:
                    if creature.type == Creature.TANK:
                        final = None
                        for target in list[creature]:
                            if final == None or target.get_creature().get_hp() < final.get_creature().get_hp():
                                final = target
                        creature.attack(final.location)
                        attacked = True
        if not attacked:
            for creature in list:
                if len(list[creature]) != 0:
                    if creature.type == Creature.SNIPER:
                        final = None
                        for target in list[creature]:
                            if final == None or target.get_creature().get_hp() < final.get_creature().get_hp():
                                final = target
                        creature.attack(final.location)
                        attacked = True
        if not attacked:
            for creature in list:
                if len(list[creature]) != 0:
                    if creature.type == Creature.NINJA:
                        final = None
                        for target in list[creature]:
                            if final == None or target.get_creature().get_hp() < final.get_creature().get_hp():
                                final = target
                        creature.attack(final.location)
                        attacked = True
    
    # moves creature closer to opposing team's weakest player                   
    def move_closer(self, creature, opponent):
        squares = creature.movement_squares()
        target = None
        destination = None
        for shit in opponent.team:
            if target == None or shit.get_hp() < target.get_hp():
                target = shit
        for square in squares:
            distance = sqrt((square.location.x - target.location.x)**2 + (square.location.y - target.location.y)**2)
            if destination == None:
                destination = square
                lowest = distance
            else:
                if distance < lowest:
                    destination = square
                    lowest = distance
        creature.map.get_tile(creature.location).remove_creature()
        creature.location = destination.location
        creature.map.get_tile(destination.location).set_creature(creature)
            
        
    
    # move to a square in which you can attack    
    def move_to_attack_range(self, list):
        for creature in list:
            movement_squares = creature.movement_squares()
            for square_1 in movement_squares:
                attack_squares = creature.attack_squares()
                for square_2 in attack_squares:
                    target = square_2.get_creature()
                    if target != None and target.player != self:
                        creature.map.get_tile(creature.location).remove_creature()
                        creature.location = square_1.location
                        creature.map.get_tile(square_1.location).set_creature(creature)
                        return True
        return False            
    
    def possible_attacks(self): #returns a dictionary of possible attacks landing on the opponent
        teammembers = {}
        for creature in self.team:
            teammembers[creature] = []
            squares = creature.attack_squares()
            for square in squares:
                target = square.get_creature()
                if target != None and target.player != self:
                    teammembers[creature].append(square)
        return teammembers
    
    def fire_check(self): #checks if there are creatures in fire and moves one away, returns true if successful
        creatures = []
        for creature in self.team:        
            if creature.get_tile().on_fire > 0:
                    creatures.append(creature)
        # move creature away
        if len(creatures) != 0:
            for shit in creatures:
                squares = shit.movement_squares()
                for square in squares:
                    if square.on_fire == 0:
                        shit.map.get_tile(shit.location).remove_creature()
                        shit.location = square.location
                        shit.map.get_tile(square.location).set_creature(shit)
                        return True
        return False
    
    def mage_or_sniper_in_danger(self): #check to see if a sniper or a mage are in danger of getting one shotted
        creatures = []
        for creature in self.team:
            if creature.type == Creature.MAGE or creature.type == Creature.SNIPER:
                # check surrounding squares to see if there's a tank
                location = creature.location
                for x in range(location.x - 1, location.x + 2):
                    for y in range(location.y - 1, location.y + 2):
                        if creature.map.contains(Location(x, y)) and creature.map.get_tile(Location(x, y)).get_creature() != None:
                            if creature.map.get_tile(Location(x, y)).get_creature().type == Creature.TANK and creature.map.get_tile(Location(x, y)).get_creature().player != self:
                                creatures.append(creature)
        # move creature away
        if len(creatures) != 0:
            for shit in creatures:
                squares = shit.movement_squares()
                for square in squares:
                    location = shit.location
                    for x in range(location.x - 1, location.x + 2):
                        for y in range(location.y - 1, location.y + 2):
                            if shit.map.contains(Location(x, y)) and shit.map.get_tile(Location(x, y)).get_creature() != None:
                                if shit.map.get_tile(Location(x, y)).get_creature().type == Creature.TANK and shit.map.get_tile(Location(x, y)).get_creature().player != self:
                                    shit.map.get_tile(shit.location).remove_creature()
                                    shit.location = square.location
                                    shit.map.get_tile(square.location).set_creature(shit)
                                    return True
        return False
    
    

        
        