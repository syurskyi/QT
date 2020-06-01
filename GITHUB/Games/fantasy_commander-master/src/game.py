import sys
from PyQt5.QtWidgets import QApplication

from map import *
from location import *
from creature import *
from player import *
from GUI import *


class Game():
    
    MOVESELECT = 0
    MOVEACTION = 1
    ATTACKSELECT = 2
    ATTACKACTION = 3
    
    
    def __init__(self, filename, map, print_msg):
        self.map = map
        self.read_from_file(filename)
        self.print_msg = print_msg
        self.squares = []
        self.turn = 0
        self.gamestate = 0
        self.currentplayer = self.player1
        self.statemethods = [self.move_select, self.move_action, self.attack_select, self.attack_action]
        self.print_msg("Player1, your turn")
        self.print_msg("Select creature to move")
        
    def read_from_file(self, filename):
        typelist = {'TANK':Tank, 'NINJA':Ninja, 'MAGE':Mage, 'SNIPER':Sniper}
        with open(filename, 'r') as file:
            line = file.readline()
            while line.startswith("Player1") == False:
                line = file.readline()
            read = line.split()[1].upper()
            if read == "HUMAN":
                type = Player.HUMAN
            else:
                type = Player.AI
            self.player1 = Player(1, type)
            while line.startswith("Player2") == False:
                line = file.readline()
                if not line.strip() or len(line.split()) < 4:
                    continue
                creature = line.split()[0].upper()
                name = line.split()[1]
                location = Location(int(line.split()[2]), int(line.split()[3]))
                if self.map.get_tile(location).is_empty():
                    new_creature = typelist[creature](name, self.player1, location)
                    self.player1.add_teammember(new_creature)
                    self.map.add_creature(new_creature, location)
            read = line.split()[1].upper()
            if read == "HUMAN":
                type = Player.HUMAN
            else:
                type = Player.AI
            self.player2 = Player(2, type)
            for line in file:
                if not line.strip() or len(line.split()) < 4:
                    line = file.readline()
                creature = line.split()[0].upper()
                name = line.split()[1]
                location = Location(int(line.split()[2]), int(line.split()[3]))
                if self.map.get_tile(location).is_empty():
                    new_creature = typelist[creature](name, self.player2, location)
                    self.player2.add_teammember(new_creature)
                    self.map.add_creature(new_creature, location)
            
            
    def undo_select(self):
        if self.gamestate == 1:
            self.gamestate = 0
            self.unhighlight()
            self.print_msg("Select creature to move")
        elif self.gamestate == 3:
            self.gamestate = 2
            self.unhighlight()
            self.print_msg("Select creature to attack with")
        
    def change_state(self):
        if self.gamestate == 0 or self.gamestate == 1:
            self.gamestate = 2
            self.unhighlight()
            self.print_msg("Select creature to attack with")
        elif self.gamestate == 2 or self.gamestate == 3:
            self.gamestate = 0
            self.unhighlight()
            self.change_players()
            self.print_msg("Select creature to move")
        
    
    def move_select(self, location):
        creature = self.map.get_creature(location)
        if creature != None and creature.player == self.currentplayer:
            self.gamestate = Game.MOVEACTION
            self.currentcreature = creature
            self.print_msg("Select where to move")
            self.squares = self.currentcreature.movement_squares()
            self.highlight(self.squares)
            
            
    def move_action(self, location):
        if self.map.get_tile(location) in self.squares:
            empty = self.map.get_tile(location).is_empty()
            if empty == True:
                self.unhighlight()
                self.map.get_tile(self.currentcreature.location).remove_creature()
                self.currentcreature.location = location
                self.map.get_tile(location).set_creature(self.currentcreature)
                self.currentcreature = None
                self.gamestate = Game.ATTACKSELECT
                self.print_msg("Select creature to attack with")
            
    def attack_select(self, location):
        creature = self.map.get_creature(location)
        if creature != None and creature.player == self.currentplayer:
            self.currentcreature = creature
            self.print_msg("Select where to attack")
            self.squares = self.currentcreature.attack_squares()
            self.highlight(self.squares)
            self.gamestate = Game.ATTACKACTION
    
    def attack_action(self, location):
        if self.map.get_tile(location) in self.squares:
            self.unhighlight()
            self.currentcreature.attack(location)
            self.gamestate = Game.MOVESELECT
            self.currentcreature = None
            self.change_players()
            self.print_msg("Select creature to move")
            
    def change_players(self):
        self.turn += 1
        self.map.reduce_fire_counter()
        if len(self.player1.team) == 0:
            self.winning = Win_message("Player2", self)
            self.winning.win_msg_handler = self.end_handling
        elif len(self.player2.team) == 0:
            self.winning = Win_message("Player1", self)
            self.winning.win_msg_handler = self.end_handling
        else:
            if self.currentplayer == self.player1:
                self.currentplayer = self.player2
                opponent = self.player1
                self.print_msg("\nPlayer2, your turn")
            else:
                self.currentplayer = self.player1
                opponent = self.player2
                self.print_msg("\nPlayer1, your turn")
            if self.currentplayer.type == Player.AI: # ai plays turn, not finished
                self.currentplayer.ai_turn(opponent)
                self.gamestate = Game.MOVESELECT
                self.change_players()
    
    def on_click(self, location):
        self.statemethods[self.gamestate](location)
    
    def end_handling(self, message):
        if message == 0:
            sys.exit()
        else:
            self.gui.close()
            self.restart_game()
        
    def restart_game(self):
        self.map = Map("maps/map2.txt")
        self.read_from_file("settings.txt")
        self.gui = Gamewindow(self.map, 50)
        self.squares = []
        self.turn = 0
        self.gamestate = 0
        self.gui.add_creature_graphitems()
        self.gui.scene.click_handler = self.on_click
        self.highlight = self.gui.highlight_squares
        
        self.unhighlight = self.gui.remove_highlighted
        self.map.set_console(self.gui.print_message)
        self.gui.skip_btn.clicked.connect(self.change_state)
        self.gui.undo_btn.clicked.connect(self.undo_select)
        self.currentplayer = self.player1
        self.statemethods = [self.move_select, self.move_action, self.attack_select, self.attack_action]
        self.print_msg("Player1, your turn")
        self.print_msg("Select creature to move")

def main():
    
    test_map = Map('maps/map2.txt')
    
    # Every Qt application must have one instance of QApplication.
    global app # Use global to prevent crashing on exit
    app = QApplication(sys.argv)
    
    gui = Gamewindow(test_map, 50)
    game = Game("settings.txt" ,test_map, gui.print_message)
    game.gui = gui
    gui.add_creature_graphitems()
    gui.scene.click_handler = game.on_click
    game.highlight = gui.highlight_squares
    
    game.unhighlight = gui.remove_highlighted
    test_map.set_console(gui.print_message)
    gui.skip_btn.clicked.connect(game.change_state)
    gui.undo_btn.clicked.connect(game.undo_select)
    
    # Start the Qt event loop. (i.e. make it possible to interact with the gui)
    sys.exit(app.exec_())

    # Any code below this point will only be executed after the gui is closed.

if __name__ == '__main__':
    main()
