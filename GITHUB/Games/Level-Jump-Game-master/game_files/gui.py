
import sys, os
from PyQt5.QtWidgets import QMainWindow, QMenuBar, QMessageBox, QDialog
from PyQt5.QtWidgets import QPushButton, QGraphicsScene,  QGraphicsView, QGraphicsTextItem, QLineEdit
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QStackedLayout, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import Qt, QObject, pyqtSignal, QEvent, QSize, QRect, QPoint
from PyQt5.QtGui import QPixmap, QColor, QPalette,QFont
from gamefield import GameField
from position import Position
from drawdynamic import DrawDynamic
from drawstatic import DrawStatic
from drawvisible import DrawVisible
from drawground import DrawGround
from drawfinish import DrawFinish
from config import Config
from leveleditor import LevelEditor
from drawlevelobject import DrawLevelObject



class Gui(QMainWindow):
    #GUI handles the whole user interface that's why this is a pretty long class
    #also there is many text creations etc. that must be written and take lines

    #class variables
    
    Distance_right_limit = Config.distance_right_limit
    Level_number = Config.level_number

    #signal for emitting key presses
    key_pressed = pyqtSignal(QEvent)
    
    #if the main game ends these signals are raised
    lose_screen_signal = pyqtSignal()
    win_screen_signal = pyqtSignal()
    
    reset_signal = pyqtSignal() #this is not even used anymore


    def __init__(self):
        #This is a really heavy init method
        
        super(Gui, self).__init__()  #calls the upper class init

        self.update_class_variables()

        #variables used to capture key press
        self.space = 0
        self.right_arrow = 0
        self.left_arrow = 0
        self.enter = 0
        
        
        self.game = False #tells if main game is running
        self.scene = None #graphicsscene added later
        self.editor_scene = None
        self.gamefield = None #gamefield object, added later
        
        self.gamefield_level = '' #tells which level (file) is currently used as gamefield

        #for capturing key presses
        self.key_pressed.connect(self.determine_key)
        
        #Main window size:
        #starting screen can be dynamically adjusted
        #for dynamic window size changes
        self.win_width = 0
        self.win_width_prev = 0
        self.win_height = 0
        self.win_changed = False
        self.restart = False # is game is restarted the scene has to be adjusted
        self.screen = 0 #these are used to determine which object the player should see
        self.screen_prev = 0
        
        self.setWindowTitle('Main Menu')#can be changed later


        #for the different screens
        self.first_win_screen = True
        self.first_lose_screen = True
        self.first_editor = True
        self.selecting_level = False
        self.editing_level = False
        self.create_some_texts() # FYI:this method physically locates very late in this file
        
        self.message_box = QMessageBox() #set a handle to a message box which is used to display user usefull information
        self.question_box = None #a message box for questions is added later
        
        self.create_mainmenu() #create a mainmenu layout system

        #connect all the end game signals
        self.__connect_signals__()
    
        
        #handles to scene items, set when items are added to scene
        self.enemy_items = []
        self.static_items = []
        self.player_item = None
      

        #when main game is started gui updates screen by calling self.update_game
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_game)
        
        #set timer value to 19 ms, can be changed (a prime number)
        self.timer.start(19)

        #when level editor is activated
        self.editor_timer = QTimer()
        self.editor_timer.timeout.connect(self.level_editor)
        self.editor_timer.start(31)#timer value (a prime number -> connections shouldn't happen at the same time)
        
        #background color
        self.setStyleSheet("""background: rgb(20,5,40);""")
        self.setAttribute(Qt.WA_NoSystemBackground, True) #these are used to fix problem with buttons translucent background in Linux
        self.setAttribute(Qt.WA_TranslucentBackground, True) #testing has shown controversial results (with one computer they fixed the problem but with other they didn't) 
        

    

    def create_mainmenu(self):

        #This method is used to create the mainmenu layout where there is a horizontal
        #layout inside a vertical layout
        
        #NOTICE: This method was implemented as one of the last methods for this game. The main designing goal
        #was to implement this method a way that already existing (and working) code needs minimal changes
        
        
        #create a new horizontal layout
        self.layout = QHBoxLayout()
        #create a new vertical layout
        self.main_layout = QVBoxLayout()
        self.main_layout.setAlignment(Qt.AlignHCenter) #align object to center of the screen

        #create a label and do style changes
        game_name = QLabel('LEVEL JUMPING GAME')
        game_name.setStyleSheet('QLabel{color:green}')
        font = QFont('Helvetica',20,QFont.Bold)
        
        game_name.setFont(font)
        self.main_layout.addWidget(game_name)
        
        self.main_layout.addLayout(self.layout) #add the horizontal layout inside the vertical layout

        #create a label and do style changes
        creator = QLabel('Created by Lauri Westerholm')
        creator.setStyleSheet('QLabel{color:green}')
        font2 = QFont('Helvetica',10)
        self.main_layout.addWidget(creator)
        

        

        #set a central widget and layout for it 
        self.setCentralWidget(QWidget())

        self.centralWidget().setLayout(self.main_layout)

        self.create_buttons() #buttons have to be recreated (or created first time if called from init) because new layout object was created
        

    def exit_mainmenu(self):
        #This method is used to exit from the maimmenu douple layout system to a single horizontal layout

        #NOTICE: This method was implemented as one of the last methods for this game. The main designing goal
        #was to implement this method a way that already existing (and working) code needs minimal changes

        #remove horizontal layout from mainmenu layout and create a new object for it
        self.main_layout.removeItem(self.layout)

        self.layout = QHBoxLayout()
        
        
        #set a central widget and layout for it
        
        self.setCentralWidget(QWidget())
        self.centralWidget().setLayout(self.layout) #set the standard horizontal layout which is used in almost all implementations

        self.create_buttons() #recreate the buttons
        

    def create_buttons(self):
        #This is a helper method which creates buttons
        # Called from create_mainmenu

        #cancel button names were later on changed to 'Menu' because that is more informative

        #notice that qt standard colors are used because they should be always os independend

        #create a continue button for win and lose screens
        self.continue_button = QPushButton('Continue')
        self.continue_button.setFixedSize(0,0)
        self.continue_button.clicked.connect(self.reset_gui)
        self.continue_button.setEnabled(False)

        #add continue button to the layout
        self.layout.addWidget(self.continue_button)


        #create a cancel button which moves user back to main menu from game screen
        self.cancel_game_button = QPushButton('Menu')
        self.cancel_game_button.clicked.connect(self.cancel_game)
        self.cancel_game_button.setFixedSize(0,0)
        self.cancel_game_button.setEnabled(False)
        self.cancel_game_button.setStyleSheet('QPushButton {background-color: transparent;color:red}')#can be changed
        self.layout.addWidget(self.cancel_game_button)
        
        #create a cancel button which moves user back to main menu from level_select
        self.cancel_level = QPushButton('Menu')
        self.cancel_level.clicked.connect(self.cancel_level_select)
        self.cancel_level.setFixedSize(0,0)
        self.cancel_level.setEnabled(False)
        self.cancel_level.setStyleSheet('QPushButton {background-color: transparent;color:red}')#can be changed 
        self.layout.addWidget(self.cancel_level)

        #create a cancel button which moves user back to main menu from level editor
        self.cancel_editor = QPushButton('Menu')
        self.cancel_editor.clicked.connect(self.cancel_level_editor)
        self.cancel_editor.setFixedSize(0,0)
        self.cancel_editor.setEnabled(False)
        self.cancel_editor.setStyleSheet('QPushButton {background-color: transparent;color:red}')#can be changed 
        self.layout.addWidget(self.cancel_editor)

        #crete a button which leads to main game
        self.switch_button = QPushButton('Game')
        self.switch_button.clicked.connect(self.game_)
        self.switch_button.setFixedSize(100,50)
        self.switch_button.setStyleSheet('QPushButton {color:green;}')
        self.layout.addWidget(self.switch_button)
        
        #create a button which leads to level select
        self.switch3 = QPushButton('Select Level')
        self.switch3.clicked.connect(self.select_level)
        self.switch3.setFixedSize(100,50)
        self.switch3.setStyleSheet('QPushButton {color:green;}')
        self.layout.addWidget(self.switch3)

        #create a button which leads to level editor
        self.switch4 = QPushButton('Level Editor')
        self.switch4.clicked.connect(self.start_level_editor)
        self.switch4.setFixedSize(100,50)
        self.switch4.setStyleSheet('QPushButton {color:green;}')
        self.layout.addWidget(self.switch4)

        #create a button which opens a help screen
        self.switch2 = QPushButton('Help')
        self.switch2.clicked.connect(self.help_screen)
        self.switch2.setFixedSize(100,50)
        self.switch2.setStyleSheet('QPushButton {color:green;}')
        self.layout.addWidget(self.switch2)


        #create a start button which starts the main game and connect to start game method
        self.start_button = QPushButton('Start Game')
        self.start_button.setStyleSheet('QPushButton {background-color: transparent;color:red}')#can be changed 
        self.start_button.clicked.connect(self.start_game)
        self.start_button.setFixedSize(0,0)
        self.start_button.setEnabled(False)
        #add the start button to layout
        self.layout.addWidget(self.start_button)


    def help_screen(self):
        #This method is called after switch2 has been pressed
        #Switch2 opens a help dialog screen
        #This may not be the most sophisticated implementation
      
        self.help = QDialog()
        
        #set window title and add a vertical layout    
        self.help.setWindowTitle('Help')
        self.help_layout = QVBoxLayout()
        self.help.setLayout(self.help_layout)

        #just add all help texts as labels
        
        
        label = QLabel()
        label.setText('GENERAL INFO:')
        self.help_layout.addWidget(label)

        label2 = QLabel()
        label2.setText("'ESC' is used to exit the game (if in main game, stops the main game)\n"
                       "'Menu'-button is always used to return to the main menu")
        self.help_layout.addWidget(label2)

        label3 = QLabel()
        label3.setText("Press 'Game' in order to switch to a window where you can start the main game\n" 
                        "By pressing 'Select level' you can choose which level you want to play\n"
                        "Press 'Level Editor' to create your own levels")
        
        self.help_layout.addWidget(label3)

        label4 = QLabel()
        label4.setText('CONTROLS:')
        self.help_layout.addWidget(label4)

        label5 = QLabel()
        label5.setText("A (or left arrow) moves the player left\n"
                       "D (or right arrow) moves the player right\n"
                       "Space: jump upwards, Q: left and upwards, E: right and upwards\n"
                       "In Level Editor: W (up), S (down), A (left), D (right)" )

        self.help_layout.addWidget(label5)

        label9 = QLabel()
        label9.setText('SELECT LEVEL')
        self.help_layout.addWidget(label9)
        
        label6 = QLabel()
        label6.setText("To select a level type the level (file) name and press enter in 'Select level'")
        self.help_layout.addWidget(label6)

        label7 = QLabel()
        label7.setText("WINNING AND LOSING")
        self.help_layout.addWidget(label7)

        label8 = QLabel()
        label8.setText("Reaching one win object (marked with a green color) leads to winning the game\n"
                       "Jumping or falling on an enemy will destroy the enemy\n"
                       "Otherwise, touching an enemy will lead to losing the game\n"
                       "Falling to a cave will lead losing the game")
        self.help_layout.addWidget(label8)
        
        #open the dialog
        self.help.open()
       

        
    def select_level(self):
        #This method is called when user starts selecting level

        self.setWindowTitle('Select Level')

        self.exit_mainmenu() #set layout to normal
        
        #set switches to the correct state
        self.set_switches_off('level')

        #initialize enter-key value and set correct state to selecting_level
        self.enter = 0
        self.selecting_level = True
        self.level_text = ''
        

        #initialize a scene where to put levels
        self.level_scene = QGraphicsScene()
        
        #view for scene
        self.level_scene_view = QGraphicsView(self.level_scene, self)
        
        self.level_scene_view.adjustSize()
        self.level_scene_view.show()
        self.layout.addWidget(self.level_scene_view) #add the view to the layout
        
        

        path = os.getcwd() #get the current working dir
        
        os.chdir('game_levels') #change to dir where levels should be located
        
        position = 50
        
        data = os.listdir() #list the dir content
        for item in data:
            if os.path.isfile(item):
                #check that only files are added
                
                #add item to level_scene to show user what levels there are to choose from
                
                level = QGraphicsTextItem(item[:-4])#cut .txt ending 
                #change color, can be changed later
                level.setDefaultTextColor(QColor(225,100,25)) #this color was just tested and it looked ok
                self.level_scene.addItem(level)
                level.setPos(0,position)
                position +=20


        self.qline_edit = QLineEdit() #create a QlineEdit
        
        #change text color
        
        palette = QPalette()
        palette.setColor(QPalette.Text,QColor(225,100,25)) #the color can be changed
        self.qline_edit.setPalette(palette)
        self.layout.addWidget(self.qline_edit)
        
        self.qline_edit.textEdited[str].connect(self.qline_edited) #connect editing qline to qline_edited        
                
                
        
        

        os.chdir(path) #remember to change back to the working dir where all classes etc are

    def qline_edited(self,text):
        #This is just a helper method which assigns qline edited text
        if self.editing_level:
            #it is called from level editor
            self.level_name = text

        else:
            #called from select level
            self.level_text = text + '.txt' #add .txt ending
        

    def set_level(self, reset):
        #This method sets the level to self.gamefield that user has chosen if possible
        #It is called via keypress event when enter is pressed and user is selecting level (self.selecting_level == True)
        #reset is a bool. if true this method is called from reset_gui otherwise this is called after keypress enter

        try :
            path = os.getcwd() #get the current working dir
            os.chdir(path) #change dir to the current working dir
            os.chdir('game_levels')

            #open the file if possible
            if not reset:
                file = open(self.level_text, 'r')

            else:
                #method is called from reset_gui 
                file = open(self.gamefield_level, 'r')

        

            #parse a gamefield from the file
            gamefield = GameField()
            
            return_value = gamefield.parse_gamefield(file)
                       
            file.close()
            
            if return_value:
                #if return value is False, the level is broken
                self.set_gamefield(gamefield)
                
                if not reset:
                    #if method is called from reset_gui these shouldn't be executed
                    self.gamefield_level = self.level_text #this value is used by reset_gui method
                    
                    #show user a message screen that level change was successfull
                    self.message_box.setIcon(QMessageBox.Information)
                    self.message_box.setText('Level successfully changed')

            else:
                #create a message box that informs the user
                self.message_box.setIcon(QMessageBox.Warning)
                self.message_box.setText('Level is not ok, using the previous level')
            
            
            
        except FileNotFoundError:
            self.message_box.setIcon(QMessageBox.Warning)
            self.message_box.setText('Level with name {} not found'. format(self.level_text))

        finally:
            os.chdir(path)#This changes back to working directory where classes etc are defined
            if not reset:
                #show the message box to the user
                self.message_box.setInformativeText('')#this is just because same message_box is also used in LevelEditor with infotext
                self.message_box.setWindowTitle('Level select')
                self.message_box.show()
        
        
    def cancel_level_select(self):
        #This method is used to switch back to the main menu view from level select

        
        self.selecting_level = False
        
        self.qline_edit.setFixedSize(0,0)
        self.layout.removeWidget(self.qline_edit)
        
        #make the level_scene not visible
        self.level_scene.setSceneRect(0,0,0,0)
        self.level_scene_view.setFixedSize(0,0)
        #delete all the items in the scene, when user enters level select again, new scene is created -> files can added or removed during the game is running
        self.level_scene.clear()
        self.layout.removeWidget(self.level_scene_view) #remove unnecessary scene view
        
        #also do style changes via
        self.cancel_game()

    def cancel_game(self):
        #This method returns the main menu view 

        
        
        self.setWindowTitle('Main Menu')
        
        self.setCentralWidget(QWidget())
        self.centralWidget().setLayout(self.layout) #this is now unnecessary, this is from the time when main menu used the same layout as rest of the game

        #set the buttons to correct states
        self.cancel_game_button.setFixedSize(0,0)
        self.cancel_game_button.setEnabled(False)
        self.cancel_level.setFixedSize(0,0)
        self.cancel_level.setEnabled(False)
        self.cancel_editor.setFixedSize(0,0)
        self.cancel_editor.setEnabled(False)

        self.start_button.setFixedSize(0,0)
        self.start_button.setEnabled(False)

        self.switch_button.setFixedSize(100,50)
        self.switch_button.setEnabled(True)
        self.switch2.setFixedSize(100,50)
        self.switch2.setEnabled(True)
        self.switch3.setFixedSize(100,50)
        self.switch3.setEnabled(True)
        self.switch4.setEnabled(True)
        self.switch4.setFixedSize(100,50)

        self.create_mainmenu() #set mainmenu layout


    def set_switches_off(self, screen):
        #This is a helper method called to set starting screen switches off
        #sets also cancel_button on
        #screen tells if next screen is level_select or game

        self.switch_button.setFixedSize(0,0)
        self.switch_button.setEnabled(False)
        self.switch2.setFixedSize(0,0)
        self.switch2.setEnabled(False)
        self.switch3.setFixedSize(0,0)
        self.switch3.setEnabled(False)
        self.switch4.setFixedSize(0,0)
        self.switch4.setEnabled(False)

        if screen == 'game':
            #next screen is the game screen so turn on/off correct cancel buttons
            self.cancel_game_button.setFixedSize(70,50) #this size was just tested and seemed ok (would be better if was set as a constant tuple)
            self.cancel_game_button.setEnabled(True)
            self.cancel_level.setFixedSize(0,0)
            self.cancel_level.setEnabled(False)
            self.cancel_editor.setFixedSize(0,0)
            self.cancel_editor.setEnabled(False)

            
        elif screen == 'level':
            #next screen is level select
            self.cancel_level.setFixedSize(70,50)
            self.cancel_level.setEnabled(True)
            self.cancel_game_button.setFixedSize(0,0)
            self.cancel_game_button.setEnabled(False)
            self.cancel_editor.setFixedSize(0,0)
            self.cancel_editor.setEnabled(False)

        else:
            #next screen is level editor
            self.cancel_level.setFixedSize(0,0)
            self.cancel_level.setEnabled(False)
            self.cancel_game_button.setFixedSize(0,0)
            self.cancel_game_button.setEnabled(False)
            self.cancel_editor.setFixedSize(70,50)
            self.cancel_editor.setEnabled(True)
            
        

    def game_(self):
        #This method creates window for starting the main game

        self.exit_mainmenu() #create normal layout

        level_name = self.gamefield_level
        #set the level name as window title (remove .txt ending)
        
        self.setWindowTitle(level_name[:-4])

        #Set the starting screen switches off
        self.set_switches_off('game')
        
        
        #set the game starting button on
        self.start_button.setFixedSize(100,50)
        self.start_button.setEnabled(True)
       
        
        #read pic (it min size can be set later)
        self.game_pixmap = QPixmap('screen_pic.png')#for reuse
        
        widget = QLabel()
        widget.setPixmap(self.game_pixmap)
        
        widget.setScaledContents(True)#makes dynamic scaling possible
        
        #set pic to back side of the screen
        self.setCentralWidget(widget)
    
        self.centralWidget().setLayout(self.layout)
       
    def start_level_editor(self):
        #This method is called when user enters level editor

        self.setWindowTitle('Level Editor') #this just changes the window title

        self.exit_mainmenu() #switch to normal layout
        
        self.editing_level = True
        
        #set the buttons to correct state
        self.set_switches_off('editor')
        

        #create a new scene (if there is None) and a view
        if self.editor_scene == None:
            self.editor_scene = QGraphicsScene()
            
        self.editor_scene_view = QGraphicsView(self.editor_scene, self)

        #manual scene view scrollling messes up automatic scrolling so disable manual scrolling
        #the vertical scrolling isn't disabled because there is no method that scrolls vertically
        self.editor_scene_view.horizontalScrollBar().blockSignals(True)
        self.editor_scene_view.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.editor_scene_view.show()
        self.layout.addWidget(self.editor_scene_view)


        #set a size based on window size
        self.editor_scene.setSceneRect(0,0, self.win_width, self.win_height)
       
        self.editor_scene_view.adjustSize()

        
        

        

        
        if self.first_editor:
            #create new objects if first scene otherwise use old (so that user can continue editing)

            self.create_new_level_edit()

            self.editor_items = [] #this is used to store pointers to items that are added to the scene

            self.first_editor = False

            #create help texts
            self.set_help_texts()

        self.save_level = False #This is used to detect when user wants to save a level
        self.level_name = '' #This is used to store level name
      
    def create_new_level_edit(self):
        #This is a help method called from start_level_editor and erase_level
        #it creates a new LevelEditor object and current object

        #create a new level editor object
        self.level_edit = LevelEditor()
            
        #create a 'current' object (see LevelEditor)
        self.editor_current = DrawLevelObject(self.level_edit.current)
        self.editor_scene.addItem(self.editor_current)

        #create a screen variable which is used to detect if current is outside the screen
        self.level_editor_screen = 0 

    def set_help_texts(self):
        #This is a method used to set help texts to the level editor scene upper partion

        #create all texts

        text1 = QGraphicsTextItem('Player P  Enemy E  Finish F  Block O  Cave I') 
        
        text2 = QGraphicsTextItem('Delete                                       Enter') #This is just done this way to minimize needed textitems (and aesthetic reasons)
        text3 = QGraphicsTextItem('erase one object                     save/erase level')  

        #set text color
        color = QColor(255,0,0) #red  
        text1.setDefaultTextColor(color)
        text2.setDefaultTextColor(color)
        text3.setDefaultTextColor(QColor(100,0,0)) #just want to use different color for description part (using one color would be simpler)
        
        #these texts are added to scene left upper corner so objects cannot be added that area
        #so DrawLevel distance_y has to match space taken by these texts (otherwise text and objects are placed on each other)

        #add textitems to the scene
        self.editor_scene.addItem(text1)
        self.editor_scene.addItem(text2)
        self.editor_scene.addItem(text3)

        #set correct positions, texts start from left corner, x position were manually tested and set
        text1.setPos(0 ,0)
        text2.setPos(0,15)
        text3.setPos(50,15)
        
      
        
        
        
    def level_editor(self):
        #This is a method which updates gui when user is in level_editor
        if self.editing_level:

            if self.win_changed:

                #user has changed window size or game has been restarted when the rect has to be readjusted
                self.editor_scene.setSceneRect(0,0,self.win_width,self.win_height)
                self.win_changed = False
                
            if self.save_level:
                #user wants to save a level
                self.save_level = False

                self.create_save_dialog()

            else:
                
                #move objects to correct positions
                self.level_edit.update_all_positions()
                #self.editor_current.move() #current is different than other objects so it updated separately (see LevelEditor)

                #scrolling the screen needs an error fixing constant
                pos = self.editor_scene_view.mapToParent(QPoint(0,0)) #get coordinates for the scene in layout coordinate system
                self.editor_x_fix = pos.x() + 40 #40 has been gotten through testing
                
                self.editor_current.adjust_position(self.level_editor_screen, self.win_width,self.editor_x_fix) #this is the new implementation
                
                #update the other objects
                self.add_level_draw_objects()
                self.remove_level_draw_objects()
                
                #update the screen
                self.update_level_editor_screen()

    def create_save_dialog(self):
        #This is a helper method used to create a QDialog screen for level_editor when user wants to save a level
        #This implementation could also be an own class and again tuples should be used when setting sizes
        
        #create a new dialog where user can set level_name 
        self.save_dialog = QDialog()
        self.save_dialog.setWindowTitle('Save/Erase level')

        #set dialog a static size (because scaling makes this screen look horrible)
        self.save_dialog.setFixedSize(450,350) #This can be changed, but these seem to be pretty good values
        
        self.save_dialog.show()
        #add a layout to the dialog
        self.dialog_layout = QVBoxLayout()
        self.save_dialog.setLayout(self.dialog_layout)
        #add help texts
        label = QLabel()
        label.setText("Check your level is not missing a player/finish position")
                              
        label2 = QLabel()
        label2.setText("Give your level a unique name\n"
                        "(if not unique, level will be saved with a standard name)")
                               
        label3 = QLabel()
        label3.setText("Save level by pressing 'Save level', exit without saving with 'ESC'")
                
        self.dialog_layout.addWidget(label)
        self.dialog_layout.addWidget(label2)
        self.dialog_layout.addWidget(label3)
                              
                
        #add a qline editor to get level_name
        self.editor_qline = QLineEdit()
        self.editor_qline.textEdited[str].connect(self.qline_edited)
        self.dialog_layout.addWidget(self.editor_qline)

        #add a button which confirms level_name
        self.save_button = QPushButton('Save level')
        self.save_button.clicked.connect(self.save_editor_level)
        self.save_button.setFixedSize(100,70)
        self.dialog_layout.addWidget(self.save_button)

        #add a button which erases the level
        self.erase_button = QPushButton('Erase level')
        self.erase_button.clicked.connect(self.confirm_delete)
        self.erase_button.setFixedSize(100,70)
        self.dialog_layout.addWidget(self.erase_button)

    def confirm_delete(self):
        #This method is called when user wants to erase a level
        #It is used to confirm that user really wants to erase the level (was not a misclick)

        #create a question messagebox if not created before (init to None)
        if not self.question_box:

            #create a question box
            self.question_box = QMessageBox()
            self.question_box.setIcon(QMessageBox.Question)
            self.question_box.setWindowTitle('Level Editor')
            self.question_box.setText('Remove the unsaved level')
            
            #set a yes button (if this is clicked the level is erased)
            self.question_box.setStandardButtons(QMessageBox.Yes)
            #set a no button this just closes qmessagebox
            self.question_box.addButton(QMessageBox.No)
            
            #erase_level check if yes has been clicked and then erases the level
            self.question_box.buttonClicked.connect(self.erase_level)

        self.question_box.setDefaultButton(QMessageBox.No) #make no highlighted
        self.question_box.show()

    def erase_level(self,button):
        #This method is used to erase the level user has created
        #button is the qpushbutton object which has been pressed
        #if yes button has been pressed, level will be erased (no button just closes the qmessagebox)

        #print(button.text())
        
        if button.text() == '&Yes':
            #This seems to be the easiest way to check the yes button has been pressed

            #clear all level scene rect items
            self.editor_scene.clear()

            #init a new LevelEditor object and a current object
            self.level_edit.init_class_variables() #see LevelEditor
            self.create_new_level_edit()
            self.set_help_texts() #set also help texts

    def save_editor_level(self):
        #This method is used to save a level if possible
        #level name is set in self.level_name by user input to editor_qline

        #close the dialog
        self.save_dialog.reject()

        #try to save the level
        return_val = self.level_edit.create_file(self.level_name) #see LevelEditor create_level

        #now inform user with qmessagebox based on return_val
        if return_val == 'error':
            #an error occurred during saving the level
            self.message_box.setIcon(QMessageBox.Warning)
            self.message_box.setText('Level saving failed!')
            self.message_box.setInformativeText('A valid level needs to have a player and at least one finish')

        else:
            #level was successfully saved as return_val + .txt
            self.message_box.setIcon(QMessageBox.Information)
            self.message_box.setText('Level successfully saved')
            self.message_box.setInformativeText('You can now play '+ return_val)
            


        self.message_box.setWindowTitle('Level Editor')
        self.message_box.show()#show the messagebox 
        


    def update_level_editor_screen(self):
        #This method is used to update screen when leveleditor is used
        #It updates screen based on 'current' location and the screen width and height
        #This method is called from level_editor

        #check if current has moved outside the screen (this does not check y dimension because levels should be mainly created left to right)
        #y dim check would be pretty easy to implement but then also main game needs to be modified in order to make new levels playable
            
        
        if self.editor_current.owner.x * DrawLevelObject.square_size  >=  self.win_width - self.editor_x_fix + (self.win_width - self.editor_x_fix) * self.level_editor_screen:
            #current is outside screen (right side), all level editor objects need to be moved left
        
            #update the screen variable
            self.level_editor_screen += 1


        elif self.editor_current.owner.x * DrawLevelObject.square_size < (self.win_width - self.editor_x_fix)* self.level_editor_screen:
            #current is now left side of the screen, all objects need to be moved
            
            #update the screen variable
            self.level_editor_screen -= 1

        self.move_level_objects() #adjust all objects positions
        

    def move_level_objects(self):
        #This is a helper method used to move level editor objects from update_level_editor_screen

            
        for item in self.editor_scene.items():
            #Editor scene contains DrawLevel objects but also text objects

            try:
                item.adjust_position(self.level_editor_screen,self.win_width, self.editor_x_fix)#see DrawLevelObject
                #this is fine for DrawLevel objects

            except AttributeError:
                #Attributerror is caused because text objects don't have adjust_position method
                #text items shouldn't even be moved
                pass
        
            
    def add_level_draw_objects(self):
        #This method is used to add a drawlevelobject for all objects
        #in self.level_edit
        #if an object is already added to the scene it doesn't do anything
        #Notice: using separate list for all the object causes that there is many mostly identical lines in this method (not so good implementation)
        #Would be a bit better if there was a help method to append items

        if self.level_edit.player:
            #check it's not None
            if not self.level_edit.player.is_added:
                drawobject = DrawLevelObject(self.level_edit.player)
                #add pointer to the object
                self.editor_items.append(drawobject)

                #add item to the scene
                self.editor_scene.addItem(drawobject)
                self.level_edit.player.added() #see LevelObject

        #add enemies
        for i in range(len(self.level_edit.enemies)):
            if not self.level_edit.enemies[i].is_added:
                drawobject = DrawLevelObject(self.level_edit.enemies[i])

                #add pointer to the object
                self.editor_items.append(drawobject)
                #add item to the scene
                self.editor_scene.addItem(drawobject)
                self.level_edit.enemies[i].added()
                
        for i in range(0, len(self.level_edit.visible)):
            if not self.level_edit.visible[i].is_added:
                drawobject = DrawLevelObject(self.level_edit.visible[i])

                #add pointer to the object
                self.editor_items.append(drawobject)
                #add item to the scene
                self.editor_scene.addItem(drawobject)
                self.level_edit.visible[i].added()

        for i in range(0, len(self.level_edit.finish)):
            if not self.level_edit.finish[i].is_added:
                drawobject = DrawLevelObject(self.level_edit.finish[i])

                #add pointer to the object
                self.editor_items.append(drawobject)
                #add item to the scene
                self.editor_scene.addItem(drawobject)
                self.level_edit.finish[i].added()

        for i in range(0, len(self.level_edit.invisible)):
            if not self.level_edit.invisible[i].is_added:
                drawobject = DrawLevelObject(self.level_edit.invisible[i])

                #add pointer to the object
                self.editor_items.append(drawobject)
                #add item to the scene
                self.editor_scene.addItem(drawobject)
                self.level_edit.invisible[i].added()

        

        
                
    def remove_level_draw_objects(self):
        #This method is used to remove all inactive leveleditor object items from editor_scene
        
        for i in range(len(self.editor_items)):
            if (not self.editor_items[i].owner.is_active) and (not self.editor_items[i].is_deleted) :
                #get all the non active items and remove them from the scene
                self.editor_scene.removeItem(self.editor_items[i])
                self.editor_items[i].is_deleted = True
            
                
                
        
        

    def cancel_level_editor(self):
        #This method is called when user exits level editor

        self.editing_level = False
        
        #reset the scene and view
        self.editor_scene.setSceneRect(0,0,0,0)
        self.editor_scene_view.setFixedSize(0,0)
        #all the items in the scene are not removed so that user can continue editing level
        
        self.layout.removeWidget(self.editor_scene_view) #remove unnecessary scene view
        
        #also do style changes via
        self.cancel_game()
        
        
    def __connect_signals__(self):
        #This method is called from init to init all the signals called
        #after the game has ended
        #This method is called only once
        self.reset_signal.connect(self.reset_gui)
        self.lose_screen_signal.connect(self.lose_screen)
        self.win_screen_signal.connect(self.win_screen)
        
        

        
    def update_class_variables(self):
        #This method is called from init to update all the gui class variables to match Config
        Gui.Distance_right_limit = Config.distance_right_limit
        Gui.Level_number = Config.level_number

       
        

    def keyPressEvent(self, event):
        #This is reimplementation of the QWidget standard keyPressEvent
        self.key_pressed.emit(event) # connects to determine_key -method

    def determine_key(self, event):
        #determines if pressed key should cause some actions
        #and forwards key press information
        #This method is used to capture key presses for all the 'subgames' so it's pretty messy
        # if self.game is true user is in main game and if self.editing_level user is editing a level

        if event.key() == Qt.Key_Return:
            self.enter += 1
            if self.selecting_level:
                self.set_level(False)#see set_level method

            elif self.editing_level:
                #user wants to save a level
                self.save_level = True
                
            
            
        if event.key() == Qt.Key_Space: # this is called whenever the space is pressed
            self.space += 1
            if self.game:
                GameField.Space += 1
             

        if event.key() == Qt.Key_A or event.key() == Qt.Key_Left:
            self.left_arrow += 1
            if self.game:
                GameField.Left_arrow += 1
                
                
            elif self.editing_level:
                LevelEditor.Left_arrow += 1
            

        if event.key() == Qt.Key_D or event.key() == Qt.Key_Right:
            self.right_arrow += 1
            if self.game:
                GameField.Right_arrow += 1
                

            elif self.editing_level:
                LevelEditor.Right_arrow += 1
            

        if event.key() == Qt.Key_Q:
            self.left_arrow += 1 #if Q is pressed, the player wants jump left
            self.space += 1
            
            if self.game:
                GameField.Left_arrow += 1
                GameField.Space += 1

        if event.key() == Qt.Key_E: #if E is pressed, the player wants jump right
            self.right_arrow += 1   #update: in level editor user wants add an enemy
            self.space += 1
            
            if self.game:
                GameField.Right_arrow += 1
                GameField.Space += 1

            elif self.editing_level:
                LevelEditor.Key_E += 1

        elif event.key() == Qt.Key_Up or event.key() == Qt.Key_W:
            if self.editing_level:
                LevelEditor.Up_arrow += 1

        elif event.key() == Qt.Key_Down or event.key() == Qt.Key_S:
            if self.editing_level:
                LevelEditor.Down_arrow += 1

        elif event.key() == Qt.Key_P :
            if self.editing_level:
                LevelEditor.Key_P += 1
            

        elif event.key() == Qt.Key_O:
            if self.editing_level:
                LevelEditor.Key_O += 1

        elif event.key() == Qt.Key_F:
            if self.editing_level:
                LevelEditor.Key_F += 1

        elif event.key() == Qt.Key_I:
            if self.editing_level:
                LevelEditor.Key_I += 1


        elif event.key() == Qt.Key_Delete:
            if self.editing_level:
                LevelEditor.Delete += 1
                
        

        elif event.key() == Qt.Key_Escape:
            if self.game:
                #just exit the maingame
                self.game = False #these need to be changed
                GameField.Game_running = False
                self.reset_gui()
            else:
                #exit the whole game
                print ("Exit button activated")
                self.close()

    def resizeEvent(self,event):
        #used to adjust scene object positions
        #This redefines Qt5 QWidget resizeEvent
       
        self.win_width = event.size().width()
        self.win_height = event.size().height()
        self.win_changed = True
        

    def start_game(self):
        #This method is used to start the main game
        
        #change to the game window
        
        self.cancel_game_button.setEnabled(False)
        self.cancel_game_button.setFixedSize(0,0)
        self.start_button.setEnabled(False)
        self.start_button.setFixedSize(0,0)

        #set new central widget for drawing the game
        self.setCentralWidget(QWidget())
        self.centralWidget().setLayout(self.layout)
        
        
        #init drawing scene for drawing game and add drawobjects to scene
        self.init_drawing_scene()
        self.add_DrawGame_objects()
        
        
        self.game = True
        GameField.Game_running = True

    def update_game(self):
        
    
        if self.game: 
                     
            
          
            if self.win_changed or self.restart:

                #user has changed window size or game has been restarted when the rect has to be readjusted
            
                self.scene.setSceneRect(0,0,self.win_width,self.win_height)
                self.correct_scene_item_positions()
                self.win_changed = False
                
                if self.restart:
                    self.adjust_static_objects_positions() #these need to be changed because otherwise incorrect position maybe used
                    self.restart = False
                
            
            self.gamefield.update_objects_positions()
            self.player_item.move_item() #see drawdynamic
            
            #also enemies has to be moved
           
            for i in range(len(self.enemy_items)):
                
                
                #move only items that aren't fallen out of game
                #(moving fallen items shouldn't broke the game but is unnecessary)
                
                if not self.enemy_items[i].owner_object.fallen:
                    self.enemy_items[i].move_item() #see drawdynamic

                elif not self.enemy_items[i].removed:
                        #check if there is a fallen item that hasn't been removed from the scene
                        self.remove_fallen_object(self.enemy_items[i])
                        #removing items is should be done only once so update removed value
                        self.enemy_items[i].removed = True
                        
                

            #now check where player is in the screen and adjust position based on that information
            self.adjust_moving_items_coordinates()
            
            #check if also static items have to be moved
            
            if self.screen != self.screen_prev:
                #static items have to be moved
                self.adjust_static_objects_positions()
                
                self.screen_prev = self.screen

            if not GameField.Game_running:
               
                #there is separate screens for winning and losing the game
                #choose the correct one
                if GameField.Fail:
                    
                    self.lose_screen_signal.emit()
                    
                else:
                    self.win_screen_signal.emit()
                
                
                
    def create_some_texts(self):
        #This method is a help method used to create texts used in the lose and win screens
        #called from init and reset_gui
        
        self.end_text = QGraphicsTextItem('GAME OVER,')
        self.continue_text = QGraphicsTextItem('Continue by pressing the button')
        self.win_text = QGraphicsTextItem('YOU WON!')
        self.lose_text = QGraphicsTextItem('YOU LOST')
        
    def reset_gui(self):

        #this method is called when game has ended and is
        #switched back to starting screen
        #this is test version of this method


        #Init win and lose screen values for a new game 
        self.first_win_screen = True
        self.first_lose_screen = True
        self.restart = True # This adjusts scene rect when user restarts the game
        
        #initialize gamefield's key press capturing class variables
        GameField.Right_arrow = 0
        GameField.Left_arrow = 0
        GameField.Space = 0
              

        #create same widget as in init, make scene and view not drawn
        self.scene.setSceneRect(0,0,0,0)
        self.scene_view.setFixedSize(0,0)
        
        #delete all the items in the scene
        self.scene.clear()
        self.layout.removeWidget(self.scene_view) #remove unnecessary scene view
        
        #Texts need to be redefined because the old items were destroyed above
        self.create_some_texts()

        #open the file and set level by calling set_level, it should always success because this file has been already opened and checked
        self.set_level(True)

        #initialize all lists of scene items
        self.enemy_items = []
        self.static_items = []
        
        
        GameField.Fail = False
        
        #set the correct screen style 
        widget = QLabel()
        widget.setPixmap(self.game_pixmap)
        widget.setScaledContents(True)
        self.setCentralWidget(widget)
        self.centralWidget().setLayout(self.layout)
        
        #enable start and cancel buttons and disable continue button
        self.start_button.setEnabled(True)
        self.start_button.setFixedSize(100,50)
        self.cancel_game_button.setEnabled(True)
        self.cancel_game_button.setFixedSize(70,50)
        
        self.continue_button.setFixedSize(0,0)
        self.continue_button.setEnabled(False)
        

    def lose_screen(self):
        #This method is called if a player has lost the game
        #It creates a screen that informs the player that the game has been lost
        #After the player continues from this screen reset_gui method will be called
        
        if self.first_lose_screen:
            #stop the game
            self.game = False
            GameField.Game_running = False
            
            #Enable continue button
            self.continue_button.setStyleSheet('QPushButton {color : red;}')
            self.continue_button.setFixedSize(100,100)
            self.continue_button.setEnabled(True)
           

            #Set correct texts in the scene
            self.end_text.setDefaultTextColor(QColor(250,0,0)) #these color have been choosen trough testing, could be changed
            self.lose_text.setDefaultTextColor(QColor(250,0,0))
            self.continue_text.setDefaultTextColor(QColor(90,20,20))
                                                            
            self.scene.addItem(self.end_text)
            self.scene.addItem(self.lose_text)
            self.scene.addItem(self.continue_text)

            self.first_win_screen = False
            
        self.end_text.setPos(self.win_width *0.5 -100 ,30) #set info texts to the scene, close to center (there is no check if these are placed on objects)
        self.lose_text.setPos(self.win_width * 0.5 -100, 50)
        self.continue_text.setPos(self.win_width * 0.5 -150, 100)
        

    def win_screen(self):
        #This method is called if a player has win the game
        #It creates a screen that informs the player that the game has been won
        #After the player continues from this screen reset_gui method will be called
        
        if self.first_win_screen:

            #stop the game
            self.game = False
            GameField.Game_running = False

            #Enable continue button
            self.continue_button.setStyleSheet('QPushButton {color : green;}')
            self.continue_button.setFixedSize(100,100)
            self.continue_button.setEnabled(True)
            

            #Set correct texts in the scene
            self.end_text.setDefaultTextColor(QColor(0,180,0)) #these color have been choosen trough testing, could be changed
            self.win_text.setDefaultTextColor(QColor(0,180,0))
            self.continue_text.setDefaultTextColor(QColor(20,90,20))
                                                            
            self.scene.addItem(self.end_text)
            self.scene.addItem(self.win_text)
            self.scene.addItem(self.continue_text)

            self.first_win_screen = False
            
        self.end_text.setPos(self.win_width *0.5 -100 ,30) #set info texts to the scene, close to center (there is no check if these are placed on objects)
        self.win_text.setPos(self.win_width * 0.5 -100, 50)
        self.continue_text.setPos(self.win_width * 0.5 -150, 100)

    def init_drawing_scene(self):
        #initializes the scene where objects are placed
        self.scene = QGraphicsScene()
        
        #view for scene
        self.scene_view = QGraphicsView(self.scene, self)
        
        self.scene_view.adjustSize()
        
        self.layout.addWidget(self.scene_view) #add to the layout and show the scene
        self.scene_view.show()


    def set_gamefield(self,gamefield):
        #helper method which sets handle to gamefield object (used also from the main)
        self.gamefield = gamefield
        

        
    def add_DrawGame_objects(self):
        #this method requires that a gamefield has been set
        #this method requires that a drawing scene has been set
        
        #it adds correct drawgame type objects for whole gamefield content
        #this method is called only once per started game, otherwise it creates duplicates

        #create drawitem for player and add it to scene
        #first create pixmap from player model picture and scale it
        
        pixmap = QPixmap('player_model_clear_3.png')
        pixmap = pixmap.scaled(Position.player_width,Position.player_heigth)
        
        player_item = DrawDynamic(self.gamefield.player,pixmap)
        self.scene.addItem(player_item)

        #add pointer to the item so that it's pos can be changed
        self.player_item = player_item
        self.player_item.move_item()
        
        #create drawitems for all enemies and add them to scene
        for i in range(len(self.gamefield.enemies)):
            
            #create pixmap and scale it correctly
            pixmap = QPixmap('enemy_model_clear1.png')
            pixmap = pixmap.scaled(Position.enemy_width,Position.enemy_heigth)
            
            enemy_item = DrawDynamic(self.gamefield.enemies[i],pixmap)
            self.scene.addItem(enemy_item)
            
            #move item to correct location
            enemy_item.move_item()
            
            #add enemy items to list so they can be easily moved
            self.enemy_items.append(enemy_item)

        #create drawitems for all ground objects
        for i in range(0,len(self.gamefield.ground_objects)):
            ground_item = DrawGround(self.gamefield.ground_objects[i])
            self.scene.addItem(ground_item)
            #add to the list of static objects
            self.static_items.append(ground_item)

        #create drawitems for all finish and visible objects

        for i in range(0,len(self.gamefield.static_objects)):
            if self.gamefield.static_objects[i].type == 'visible_object':
                visible_item = DrawVisible(self.gamefield.static_objects[i])
                self.scene.addItem(visible_item)
                self.static_items.append(visible_item)

            elif self.gamefield.static_objects[i].type == 'finish_object':
                finish_item = DrawFinish(self.gamefield.static_objects[i])
                self.scene.addItem(finish_item)
                self.static_items.append(finish_item)

    def remove_fallen_object(self, item):
        #This helper method is used to remove fallen enemy objects from drawing scene scene
        #called from update_game method
        
        self.scene.removeItem(item) #remove the enemy item from the scene
                

    def correct_scene_item_positions(self):
        #This method is called after user has changed window size
        #it sets new y_min coordinates for ground items in scene
        #so that window remains looking the same style as before adjusting the size (ground objects continue to the screen lower limit)

        
        #By changing implementation of this method could easily affected on how ground objects look (for example ground object could be set smaller)
        
        delta_y = self.win_height - GameField.MainWindow_Heigth
        
        if delta_y > 0:

            #correct ground objects y-coordinates:
            for i in range(0,len(self.static_items)):

                if self.static_items[i].type == 'ground_object':
                    x = self.static_items[i].x #left corner
                    y = self.static_items[i].y #upper corner
                    width = self.static_items[i].width
                    height = self.static_items[i].height + delta_y
                    self.static_items[i].new_height = height # used by adjust_static_objects_positions

                    #set new height
                    self.static_items[i].setRect(x,y,width,height)

    def adjust_moving_items_coordinates(self):
        #This method is called after player and enemy objects are moved
        #It adjust x_min coordinates to match player position

        

        if self.player_item.owner_object.position.x_max >= ((self.win_width -Gui.Distance_right_limit) + \
            self.screen * (self.win_width - Gui.Distance_right_limit - Position.Distance_x)):
            
            self.screen += 1 #player is on the right edge outside of the current screen 
            self.win_width_prev = self.win_width #this is done cause user can ajust screen anytime
            #and we don't want dynamic objects to move when the aren't near the edges
            
        elif (self.screen != 0) and self.player_item.owner_object.position.x_max < ((self.win_width -Gui.Distance_right_limit) + \
           (self.screen -1) * (self.win_width - Gui.Distance_right_limit - Position.Distance_x)):
            
            self.screen -= 1 #player is on the left edge of the current screen, screen has to be moved left so that player won't disappear
            self.win_width_prev = self.win_width
        
        

        if self.screen > 0:
        
            delta_x = self.screen *(self.win_width_prev - Position.Distance_x -Gui.Distance_right_limit)#Distance_x tells where the most left object should be located in the screen

            # adjust player item location
            y = self.player_item.owner_object.position.y_max #upper corner
            x = self.player_item.owner_object.position.x_min #left corner
            self.player_item.setPos(x - delta_x, y)

            # adjust enemy positions
            for i in range(len(self.enemy_items)):
                
                y = self.enemy_items[i].owner_object.position.y_max
                x = self.enemy_items[i].owner_object.position.x_min
                self.enemy_items[i].setPos(x - delta_x, y)
            
                

                
        
        #if delta_x = 0, player is still in the original screen and nothing has to be done
                   
        #notice that self.screen is also used to adjust  static object locations
                
        
    def adjust_static_objects_positions(self):
        #this method is called when self.screen != self.screen_prev
        # it adjusts static_object position to correctly fit object to the screen

        delta_x = self.screen *(self.win_width_prev - Position.Distance_x -Gui.Distance_right_limit)
        
        for i in range (len(self.static_items)):
            
            y = self.static_items[i].y #upper corner, it's not changed
            x = self.static_items[i].x - delta_x #left corner
            
            width = self.static_items[i].width
            height = self.static_items[i].height
            
            if self.static_items[i].type == 'ground_object':
                
                if self.static_items[i].new_height != 0:
                    #if correct_scene_item_positions method has been called ground's draw height doesn't match owner_object height
                    height = self.static_items[i].new_height
                    
            
            self.static_items[i].setRect(x,y,width,height)

        
    
            
    def get_scene_items_number(self):
        #this was for testing use only
        print('there is {} items in scene'.format(len(self.scene.items())))
            
        

        
