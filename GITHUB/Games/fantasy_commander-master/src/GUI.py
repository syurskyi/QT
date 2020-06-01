from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.Qt import QGraphicsRectItem, QGraphicsPixmapItem, QPixmap, QTextBrowser,\
    QMessageBox
from PyQt5.QtGui import QColor, QBrush

from location import Location
from tile import Tile
from creature_graphitem import Creature_graphitem
from tile_graphitem import Tile_graphitem

class MyScene(QtWidgets.QGraphicsScene):
    def __init__(self, map):
        super().__init__()
        self.map = map
        
    def mousePressEvent(self, event):
        if 0 <= event.scenePos().x() <= (self.map.get_width() * 50) and 0 <= event.scenePos().y() <= (self.map.get_height()*50):
            location = Location(int(event.scenePos().x()//50), int(event.scenePos().y()//50))
            self.click_handler(location)
            

class Gamewindow(QtWidgets.QMainWindow):
    
    def __init__(self, map, tile_size):
        super().__init__()
        self.setCentralWidget(QtWidgets.QWidget()) # QMainWindown must have a centralWidget to be able to add layouts
        self.vertical= QtWidgets.QVBoxLayout() # vertical main layout
        self.horizontal = QtWidgets.QHBoxLayout()
        self.centralWidget().setLayout(self.vertical)
        self.map = map
        self.tile_size = tile_size
        self.gameobjects = []
        self.highlighted = []
        self.tile_graphitems = []
        self.init_window()
        self.init_textconsole()
        self.init_buttons()

        self.add_tile_graphitems()
        #self.add_creature_graphitems()
        self.update_objects()

        # Set a timer to call the update function periodically
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_objects)
        self.timer.start(10) # Milliseconds


    def init_textconsole(self):
        self.console = QTextBrowser()
        self.console.setText("Welcome to Fantasy Commander 1.0!\nPlayer 1: Red        Player 2: Blue\n")
        self.vertical.addWidget(self.console)

    def add_tile_graphitems(self):
        
        for x in range(0, self.map.get_width()):
            for y in range(0, self.map.get_height()):
                tile = self.map.get_tile(Location(x, y))
                item = Tile_graphitem(tile, self.tile_size, x, y)
                self.scene.addItem(item)
                self.tile_graphitems.append(item)
                
    def update_map(self):
        for item in self.tile_graphitems:
            item.set_sprite()
            if item.tile.on_fire > 0:
                item.set_on_fire()
                
    
    def highlight_squares(self, squares):
        
        for square in squares:
            item = QGraphicsRectItem(square.location.x * self.tile_size, square.location.y *self.tile_size, self.tile_size, self.tile_size)
            item.setBrush(QBrush(QColor(255, 145, 0, 128)))
            self.scene.addItem(item)
            self.highlighted.append(item)
        
    def remove_highlighted(self):
        
        for item in self.highlighted:
            self.scene.removeItem(item)
        self.highlighted = []

            
                
    def get_gameobjects(self):
        return self.gameobjects


    def add_creature_graphitems(self):
        
        for creature in self.map.get_creatures():
            if creature not in self.get_gameobjects():
                item = Creature_graphitem(creature, self.tile_size)
                self.scene.addItem(item)
                self.gameobjects.append(item)


    def init_buttons(self):
        
        self.skip_btn = QtWidgets.QPushButton("Skip")
        self.vertical.addWidget(self.skip_btn)
        #self.skip_btn.move(850, 4*50)
        self.undo_btn = QtWidgets.QPushButton("Undo select")
        self.vertical.addLayout(self.horizontal)
        self.horizontal.addWidget(self.undo_btn) # tried to make the buttons noxt to each other but didn't succeed :(
        

    def update_objects(self): # update alive characters and remove dead
        
        for item in self.get_gameobjects():
            if item.creature.is_dead():
                self.gameobjects.remove(item)
                self.scene.removeItem(item)
            else:
                item.updateAll()
        self.update_map()

    def init_window(self):
        '''
        Sets up the window.
        '''
        self.setGeometry(300, 300, 1000, 650)
        self.setWindowTitle('Fantasy Commander 1.0')
        self.show()

        # Add a scene for drawing 2d objects
        self.scene = MyScene(self.map)
        self.scene.setSceneRect(0, 0, 800, 50 * 9)

        # Add a view for showing the scene
        self.view = QtWidgets.QGraphicsView(self.scene, self)
        self.view.adjustSize()
        self.view.show()
        self.vertical.addWidget(self.view)
        
    def print_message(self, msg):
        self.console.append(msg)
        
class Win_message(QMessageBox):
    def __init__(self, player, game):
        super().__init__()
        self.game = game
        self.buttonReply = self.question(self, '{} you won!'.format(player), "Do you want to play again?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if self.buttonReply == QMessageBox.Yes:
            self.game.end_handling(1)
        else:
            self.game.end_handling(0)