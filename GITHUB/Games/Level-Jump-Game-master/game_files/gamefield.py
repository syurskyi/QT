from gameobject import GameObject
from player import Player
from enemy import Enemy
from position import Position
from config import Config

class GameField:


    #NOTICE: In general this class is obtimized poorly and many method implementations are bad
    
    #define the class variables
    
    
    #UPDATE:this is just for parsing gamefield
    MainWindow_Heigth = 10000 #This is just for an old implementation: this determines so called ground objects y_min coordinates in pixels
    #it technically doesn't affect on the game at all (when it is big enough)
    #if this value is too small and user places object outside screen (lower than this value) -> objects will infinitely fall
    # it doesn't anymore affect how mainwindow looks (mainwindow scales dynamically), the implementation was created when mainwindow had a fixed size
    
    Space = 0
    Right_arrow = 0
    Left_arrow = 0
    Game_running = False
    Fail = False
    Max_empty_lines = 10 #can be changed, tries to prevent user from making insane gamefields. if levels are created with LevelEditor this won't affect anything
    

    def __init__(self):
        
        #init method, called from the main
        self.static_objects = []
        self.enemies = []
        self.player = None
        self.ground_objects = [] #used to draw ground
        self.Width = 0
        self.distance_y = 0 #used in drawgame to determine the 'highest' pixels to draw
        self.max_level = 0 #used in drawgame to determine the lowest pixels to draw
        
        self.space = 0
        self.right_arrow = 0
        self.left_arrow = 0

        self.first_turn = True #This is used in update_enemy_positions method

        self.__update_all_class_variables__()

    def __update_all_class_variables__(self):
        #This is called when new a new gamefield is created, it should no be called after that
        # It updates all class variables (in player, position and enemy) to match Config values read from the config.txt file
        
        Position.Distance_x = Config.distance_x
        Position.Empty_line_heigth = Config.empty_line_height

        Position.static_object_heigth = Config.static_object_height
        Position.static_object_width = Config.static_object_width

        Position.enemy_heigth = Config.enemy_height
        Position.enemy_width = Config.enemy_width

        Position.player_heigth = Config.player_height
        Position.player_width = Config.player_width

        Player.Speed = Config.player_speed
        Player.Jump_x = Config.player_jump_x
        Player.Jump_y = Config.player_jump_y
        Player.Jump_max_height = Config.player_jump_max_height
        Player.Fall_y = Config.player_fall_y
        Player.Fall_x = Config.player_fall_x

        Enemy.Enemy_speed = Config.enemy_speed
        Enemy.Fall_y = Config.enemy_fall_y

        
        
        
        


            
    def get_first_invisible_object(self):
        
        #This method return first invisible object (first invisible object is the highest and most left of those objects)
        #if there is no invisible objects, returns None
        
        for i in range(len(self.static_objects)):
             
            if self.static_objects[i].type == 'invisible_object':
                return self.static_objects[i]

        return None

    
        


    
    def parse_gamefield(self, file):
        # file is a handle to a file opened in the main
        
        # This method parses the gamefield to a GameField object if possible
        # implemented such a way that parsing can be done from gui or from the main
        # returns True if successfull, otherwise False

        #variables used to store information from the file
        current_line = ''
        empty_line_count = 0
        objects_level = 0
        object_number = 0 # tells object position at the file
        non_empty_lines = 0
        player_count = 0
        finish_count = 0
        prev_fall_object_x_max = Position.Distance_x  #used to construct ground objects
        
        field_width = object_number
           
           
        try:
            current_line = file.readline()
            
            while current_line:
                #loop until an EOF char is found
                
                object_number = 0 # initializing for a new line
                
                
                line = current_line.split() #whitespace skipped
                line_len = len(line)


                if current_line[0] == '%':
                    current_line = file.readline()
                    #comments starting with % are skipped

               
                elif line_len == 0:
                    #found an empty line
                    
                    if empty_line_count <  GameField.Max_empty_lines: 
                        empty_line_count += 1
                    current_line = file.readline()
                    
                else:
                    if non_empty_lines == 0:
                        #this is used to set distance_y only one time (all objects positions depend on it)
                        self.distance_y = empty_line_count #how much space before objects in y dimension
                        
                    non_empty_lines += 1
                   
                    i = 0
                    for i in range (line_len):
                        #creating object based on their location in the file
                        #the next implementation could be improved

                        
                        
                        if line[i].lower() == 'p':
                            
                            if player_count != 0:
                                print('Only one player location allowed')
                                return False
                            
                            player = Player() #create objects
                            location = Position()
                            location.set_position(object_number,objects_level,'player',empty_line_count) #see position.py
                            player.set_position_object(location)
                            self.player = player #set handle to the object
                            object_number += 1 #add counters
                            player_count += 1
                            

                        elif line[i].lower() == 'e': #enemy object
                            #create objects and add the enemy to correct list
                            enemy = Enemy()
                            position = Position()
                            position.set_position(object_number,objects_level,'enemy',empty_line_count)
                            enemy.set_position_object(position)
                            self.enemies.append(enemy)
                            object_number += 1

                        elif line[i].lower() == 'o': #obstacle
                            #create a visible object, doesn't have an own class, uses the upper class straighly
                            obstacle = GameObject('visible_object')
                            position = Position()
                            position.set_position(object_number,objects_level,'static',empty_line_count)
                            obstacle.set_position_object(position)
                            self.static_objects.append(obstacle)
                            object_number += 1

                        elif line[i].lower() == 'f': #fall object
                            #create an invisibleobject from the upper class
                            fall = GameObject('invisible_object') #see invisible.py
                            position = Position()
                            position.set_position(object_number,objects_level,'static',empty_line_count)
                            fall.set_position_object(position)
                            self.static_objects.append(fall)
                            object_number += 1

                            #ground objects are constructed based on fall object information, the last ground object is created outside this loop
                            x_min = prev_fall_object_x_max #initial value is draw area's left starting point
                            x_max = position.x_min 
                            y_max = position.y_min #this is fine because fall objects are on the bottom level of the screen
                            y_min = GameField.MainWindow_Heigth
                            
                            #create a position object for the ground object
                            prev_fall_object_x_max = position.x_max #this has to be just here, otherwise wrong value is assigned
                            
                            if x_min != x_max:
                                #This check is absolutely needed, otherwise extra ground objects are created if multiple fall objects are placed next to each other

                                #manually create an position object with correct coordinates
                                position = Position()
                                position.x_max = x_max
                                position.x_min = x_min
                                position.y_min = y_min
                                position.y_max = y_max
                                position.level = objects_level + 1
                            
                                #create a ground object, doesn't have an own class
                                ground = GameObject('ground_object')
                                ground.set_position_object(position)
                            
                                self.ground_objects.append(ground)
                            


                         

                        elif line[i].lower() == 'w': #finish object
                            #create a finish object, no own class
                            finish = GameObject('finish_object')
                            position = Position()
                            position.set_position(object_number,objects_level,'static',empty_line_count)
                            finish.set_position_object(position)
                            self.static_objects.append(finish)
                            object_number += 1
                            finish_count += 1
                            
                        elif line[i].lower() == '-': #empty object
                            object_number += 1
                        

                        else:
                            print("Incorrect object symbol, gamefield can't be created")
                            return False

                    #exit for-loop, increase level, check field_width and read newline
                    objects_level += 1 #could be done by using non_empty_lines
                    
                    
                    if field_width == 0:
                        field_width = object_number #the first object line defines how many 
                        #objects there should be in all the remaining lines

                    elif object_number != field_width:
                        print('Wrong amount of objects per line, check your input file')
                        return False
                    
                    current_line = file.readline() #read a new line and start the checking again
                        
            self.max_level = objects_level #this was for drawgame, probably not used anymore

            #check the level had a player and at least one finish
            if player_count != 1 or finish_count < 1:
                print('File is missing finish or player object')
                return False

            #now we have to append the last ground object which x-max is gamefield's right edge
            #if there is an invisible object just at the edge of a level this will make an extra ground object but the ground object (black line) informs
            #the user that there is still an invisible object which you can't hit (or you lose)
            
            x_max = self.find_biggest_x_value()
            #assign it also to width
            self.Width = x_max
            y_max = self.find_biggest_y_value() #upper corner coordinates
            position = Position()
            position.x_max = x_max
            position.x_min = prev_fall_object_x_max
            position.y_max = y_max
            position.y_min = GameField.MainWindow_Heigth
            position.level = self.max_level + 1
            
            ground = GameObject('ground_object')
            ground.set_position_object(position)
            self.ground_objects.append(ground)

            #check that invisible objects are not placed in incorrect locations (must be at the bottom level)
            invisible = self.get_first_invisible_object()
            if invisible:
                #if there was invisible objects
                #check that the invisible object is not higher than y_max (lowest point of the screen)
                if invisible.position.y_min < y_max:
                    print('Fall objects are incorrectly placed')
                    return False #gamefield is not appropriate
            
                            
            

            #now correct invisible objects height (y_max coordinates, changes size of hitboxes) 
            self.set_invisible_objects_height()
                    
            return True #if everything went fine, code reached this line
        
        except OSError:
            #if there is some severe error in the input file
            
            print('file containing gamefield is not readable format')
            return False
              

    def find_biggest_x_value(self):
        #this helper method is used in construction of the last ground object
        #it's called from parse_gamefield
        #this fuctionality seeking biggest value could be implementet straigth to the parser method
        
        x_max = Position.Distance_x
        for i in range(len(self.static_objects)):
            if self.static_objects[i].position.x_max > x_max:
                x_max = self.static_objects[i].position.x_max

        
        for i in range(0,len(self.enemies)):
            if self.enemies[i].position.x_max > x_max:
                x_max = self.enemies[i].position.x_max

        if self.player.position.x_max > x_max:
            x_max = self.player.position.x_max

        return x_max

    def set_invisible_objects_height(self):
        #this method is called from parse gamefield
        #it sets invisible_objects height to match Invisible_Object_Height from class invisible_object
        #Invisible_Object_Height tells how much object is above ground objects

        y_lowered = 200 #This value should work always (huge objects may still be an issue)
        
        for i in range(len(self.static_objects)):
            if self.static_objects[i].type == 'invisible_object':

                #notice: the y-coordinate system, y_min is lowest point of the object
                self.static_objects[i].position.y_max = self.static_objects[i].position.y_min - Config.invisible_object_height

                #now invisible objects lower coordinates can also be adjusted so that hit detection works
                #if invisible objects aren't lowered, with some fall_y and fall_x values dynamic objects can fall through invisible objects

                self.static_objects[i].position.y_min += y_lowered


    def find_biggest_y_value(self):
        #this helper method is used in construction of the last ground object
        #it's called from parse_gamefield
        #this fuctionality seeking biggest value could be implementet straigth to parser method
        
        y_max = 0
        #position.y_min is the lowest point of an object so position.y_min > position.y_max
        for i in range(len(self.static_objects)):
            if self.static_objects[i].position.y_min > y_max:
                y_max = self.static_objects[i].position.y_min

        
        for i in range(0,len(self.enemies)):
            if self.enemies[i].position.y_min > y_max:
                y_max = self.enemies[i].position.y_min

        if self.player.position.y_min > y_max:
            y_max = self.player.position.y_min

        return y_max





    def update_objects_positions(self):
        #This method is called from gui update_game to update gamefield
        
        self.update_player_pos()
        self.update_enemy_positions()

        self.first_turn = False #update the variable, the first turn is now completed
        #(only needs to be updated once but this sets it False every iteration but that doesn't take much time)
        
        
        

    def update_player_pos(self):

        #this method updates player position based on user key input
        #it's called from update_objects_positions

        if GameField.Space == 0 and GameField.Right_arrow == 0 and GameField.Left_arrow == 0:
            #this just falls player in the start of the game
            #cause level may have player floating in air
            
            self.player.fall_direction = 'down'
            self.fall(self.player)#fall dir down

        
        if self.player.jumping:
            #continue the jump
            self.space = GameField.Space
            self.right_arrow = GameField.Right_arrow
            self.left_arrow = GameField.Left_arrow
            self.jump()
       
        
            

        elif self.player.falling:
            #continue the fall
            
            self.fall(self.player)
            

        elif self.space < GameField.Space:

            
                
            if self.right_arrow < GameField.Right_arrow:
                #calls jump dir right
                
                self.space = GameField.Space
                self.right_arrow = GameField.Right_arrow
                
                self.player.set_jump_direction('right')
                self.player.jumping = True
                self.jump()

            elif self.left_arrow < GameField.Left_arrow:
                #calls jump dir left
                self.space = GameField.Space
                self.left_arrow = GameField.Left_arrow
                
                self.player.set_jump_direction('left')
                self.player.jumping = True
                self.jump()
               
               

            
            else:
                #calls jump dir straight
                self.space = GameField.Space
                self.player.set_jump_direction('up')
                self.player.jumping = True
                self.jump()
            

        elif self.right_arrow < GameField.Right_arrow:
                
                #calls move to right
                self.move(self.player,True)
                self.player.fall_direction = 'down'
                self.fall(self.player) 
                #call also fall to check player is not floating in air
                self.right_arrow = GameField.Right_arrow

        elif self.left_arrow < GameField.Left_arrow:
                
                #calls move to left
                self.move(self.player,False)
                self.player.fall_direction = 'down'
                self.fall(self.player) 
                #call also fall to check player is not floating in air
                self.left_arrow = GameField.Left_arrow


    def update_enemy_positions(self):
        #if enemy is destroyed it's position is no longer updated (fall method is still called so that destroyed enemies don't start to float)
        #fallen enemies should be removed from drawing scene but if enemies are just destroyed they aren't removed
        
        #it's now implemented such a way that enemy speed can't be high number
        #otherwise game is really difficult, almost impossible to win cause players move so fast

        #NOTICE: This implementation is really poorly optimized -> if level is big enough, framerate drops to couple fps
        # the methods this implementation calls are also poorly optimized

        for i in range(0,len(self.enemies)):
            if not self.enemies[i].destroyed:
                    
                if not self.enemies[i].falling:
                    if not self.first_turn:
                        #enemies can't be moved during first turn after game has been restarted
                        #because they may be floating on air
                        self.move(self.enemies[i],self.enemies[i].direction)

                    
                    #also call fall so that enemies dont' begin to float in air
                    self.fall(self.enemies[i])
                    

                else:
                    #an enemy object is floating in air and it must be fallen
                    self.fall(self.enemies[i])
                    
            elif not self.enemies[i].fallen:
                #fall destroyed enemies that are still visible in the game
                self.fall(self.enemies[i])
                


    def move(self,dynamic_object,direction):
        #moves dynamic object on the level
        #dynamic_object is the object to be moved
        #direction is Bool: False = left, True = Right


        position = dynamic_object.position
        y_min = position.y_min
        y_max = position.y_max

        if direction:
            new_x_min = position.x_min + dynamic_object.speed_x #these are the new coordinates where the object is trying to move
            new_x_max = position.x_max + dynamic_object.speed_x
        else:
            new_x_min = position.x_min - dynamic_object.speed_x
            new_x_max = position.x_max - dynamic_object.speed_x
            

        return_value = self.check_position(dynamic_object,new_x_min,new_x_max,y_min,y_max)

        #check the return value
        
        if return_value == 'empty':
            
            
            #position is ok
            #move object to the position
            dynamic_object.set_new_position(new_x_min,new_x_max,y_min,y_max)
            #see class dynamic_object
            
            

        elif return_value == 'finish_object':
            
            if dynamic_object.type == 'player':
                #player won the game
                dynamic_object.set_new_position(new_x_min,new_x_max,y_min,y_max)
                

                GameField.Game_running = False

            else:
                # an enemy hit a finish object, turns enemy's direction
                dynamic_object.turn_direction() #see class enemy
                

        elif return_value == 'enemy':
            if dynamic_object.type == 'player':
                #player lost the game
                GameField.Game_running = False
                GameField.Fail = True

            else:
                #an enemy just hit another enemy, if enemy hit a destroyed (or fallen) this line won't be executed
                #(check_position is not returning 'enemy' for destroyed enemies)
                
                enemy = self.get_enemy_object_at_position(new_x_min,new_x_max,y_min,y_max, dynamic_object) #see get_enemy_object_at_position
                
                dynamic_object.turn_direction()
                        
                #move the moving enemy to a new position
                dynamic_object.set_new_position(new_x_min,new_x_max,y_min,y_max)
        
        elif return_value == 'invisible_object':

            if dynamic_object.type == 'player':
                #player lost the game
                GameField.Game_running = False
                GameField.Fail = True

            else:
                #enemy is destroyed and removed from screen by setting it status fallen
                dynamic_object.set_destroyed()
                dynamic_object.set_fallen()
                

        elif return_value == 'visible_object' and dynamic_object.type == 'enemy':
            #hitting visible object doesn't do anything to the player object
            #reverses enemy direction
            dynamic_object.turn_direction()

        elif return_value == 'player':
            #enemy has collided with player and the game is lost
            #for more fair gameplay check the player isn't falling
            if not self.player.falling:
                GameField.Game_running = False
                GameField.Fail = True
            

                         

        elif return_value == 'ground_object' and dynamic_object.type == 'enemy':
            #hitting ground object (at the edge of a level)
            #turns an enemy direction, does nothing to a player object
            dynamic_object.turn_direction()
            




    def jump(self):
        #player jump method
        #called from update_player_pos
        #direction: 'up', 'left', 'right'
        

        direction = self.player.jump_direction
        
        
        if (direction == 'up') or (direction == 'right') or (direction == 'left'):

            

            if (self.player.jump_cycles * Player.Jump_y) >= Player.Jump_max_height:
                #player has reached the highest point of the jump and starts to fall
                
                self.player.jump_cycles = 0
                self.player.jumping = False
                self.player.falling = True
                
            else:
                #player hasn't yet reached highest point of a jump

                new_y_min = self.player.position.y_min - Player.Jump_y # notice how y-coordinate system works
                new_y_max = self.player.position.y_max - Player.Jump_y

                if direction == 'up':
                    new_x_min = self.player.position.x_min   # up (straight) jump doesn't change x-coordinates
                    new_x_max = self.player.position.x_max
                    self.player.fall_direction = 'down' #after jump the player falls straight down 
            
                elif direction == 'right':
                    new_x_min = self.player.position.x_min + Player.Jump_x
                    new_x_max = self.player.position.x_max + Player.Jump_x
                    self.player.fall_direction = 'right' #after jump player falls right

                else:
                
                    new_x_min = self.player.position.x_min - Player.Jump_x
                    new_x_max = self.player.position.x_max - Player.Jump_x
                    self.player.fall_direction = 'left' #after jump player falls left

                if direction == 'up':
                    return_value = self.check_position_jump(self.player,new_x_min,new_x_max,new_y_min,new_y_max, 0) #jump_x needs to be 0

                else:
                    return_value = self.check_position_jump(self.player,new_x_min,new_x_max,new_y_min,new_y_max, self.player.jump_x)
                    
                #check the return value and do actions based on that

                if return_value == 'empty':
                    self.player.set_new_position(new_x_min,new_x_max,new_y_min,new_y_max)
                    
                    self.player.jump_cycles += 1

                elif return_value == 'finish_object':
                    #player won the game
                    GameField.Game_running = False

                elif return_value == 'visible_object':
                    #player starts to fall
                    self.player.jumping = False
                    self.player.falling = True
                    
                        
                    self.player.jump_cycles = 0
                    
                elif return_value == 'invisible_object':
                    #player has lost the game
                        
                    self.player.falling = True
                    GameField.Fail = True
                    GameField.Game_running = False

                elif return_value == 'enemy':
                    
                    #player has destroyed an enemy
                    #this is not so good implementation
                    
                    enemy = self.get_enemy_object_at_position(new_x_min,new_x_max,new_y_min,new_y_max, None)
                   
                    

                    try:
                        enemy.set_destroyed()
                    except AttributeError:
                        #if enemy is None, but then smt unexpected has happened
                        #this error should not be ever possible under normal conditions
                        pass
                    
                    self.player.set_new_position(new_x_min,new_x_max,new_y_min,new_y_max)
                   
                    self.player.jump_cycles += 1

                else:
                    
                    #this is reached if return value is ground object (player trying jump outside playfield)
                    self.player.jumping = False
                    self.player.falling = True
                    self.player.jump_cycles = 0 #this has to be now initialized (same with visible objects)

                    self.player.fall_direction = 'down' 
                       
                    self.fall(self.player)
                    
                    
        
                        
                    
                    
    def fall(self, dynamic_object):
        #This is fall method for both player and enemy objects
        #Direction is a string 'down', 'right', 'left' and it's stored in dynamic_object.fall_direction
        
        #fall method is called after player has jumped
        #it also called after an enemy has moved to check that the enemy isn't floating in air
        #dynamic object is the object to fall if possible
        #only a player object can fall sideways
        

        if dynamic_object.type == 'player' and dynamic_object.fall_direction == 'right':
            x_min = dynamic_object.position.x_min + dynamic_object.fall_x
            x_max = dynamic_object.position.x_max + dynamic_object.fall_x

        elif dynamic_object.type == 'player' and dynamic_object.fall_direction == 'left':
            x_min = dynamic_object.position.x_min - dynamic_object.fall_x
            x_max = dynamic_object.position.x_max - dynamic_object.fall_x
        
        else:
            
            x_min = dynamic_object.position.x_min #fall doesn't change x-coordinates
            x_max = dynamic_object.position.x_max
            
        fall = dynamic_object.fall_y #This is same for all the fall directions

        y_min_new = dynamic_object.position.y_min + fall
        y_max_new = dynamic_object.position.y_max + fall

        return_value = self.check_position_fall(dynamic_object,x_min,x_max,y_min_new,y_max_new)
        
        #check the return_value and do actions based on that
      
        if return_value == 'empty':
            dynamic_object.falling = True
            dynamic_object.set_new_position(x_min, x_max, y_min_new, y_max_new)
            #see DynamicObject

            
        elif return_value == 'enemy':
            
            #enemy is destroyed
           
            enemy = self.get_enemy_object_at_position(x_min,x_max,y_min_new,y_max_new, dynamic_object)

            try:
                #this should always success
                
                enemy.set_destroyed()
                

            except AttributeError:
                #if enemy is None, but then smt unexpected has happened
                #this error should not be ever possible under normal conditions
                #print('virhe')
                pass
            
            dynamic_object.set_new_position(x_min,x_max,y_min_new,y_max_new)

        elif return_value == 'finish_object':
           

            if dynamic_object.type == 'player':
                
                
                #player has won the game
                GameField.Game_running = False
                GameField.Fail = False
                dynamic_object.falling = False

            else:
                #an enemy has just fallen on a finish
                dynamic_object.falling = False
                

        elif return_value == 'visible_object':
            #if the player is falling left or right, stop sideways falling
            #otherwise stop falling entirely
            
            if dynamic_object.type == 'player' and (self.player.fall_direction == 'left' or self.player.fall_direction == 'right'):
                self.player.fall_direction = 'down'
                
            else:
                #place object on a visible object so that it doesn't start floating in air
                self.set_object_to_ground_level(dynamic_object,'visible')
                dynamic_object.falling = False

        elif return_value ==  'ground_object':
            
            #place object on a ground object so that it doesn't start floating in air
            self.set_object_to_ground_level(dynamic_object,'ground')
            dynamic_object.falling = False

        elif return_value == 'invisible_object':

            if dynamic_object.type == 'player':
                #player lost the game
                GameField.Fail = True
                GameField.Game_running = False
                #dynamic_object.set_new_position(x_min,x_max,y_min_new,y_max_new) this may cause funny looking situations

            else:
                #an enemy has fallen and becomes destroyed
                # enemy's fall value needs to be changed
                dynamic_object.set_new_position(x_min,x_max,y_min_new,y_max_new)
                dynamic_object.set_destroyed()
                dynamic_object.set_fallen()

        elif return_value == 'player':
            #an enemy has destroyed player
            #player lost the game

            GameField.Fail = True
            GameField.Game_running = False
            dynamic_object_falling = False
        

            
            
        
                
            
                
                
            
            
    def check_position(self,dynamic_object,x_min,x_max,y_min,y_max):
        #check if a new position is ok to move into

        #returns 'visible_object' if there is visible object in that position
        #return 'finish_object' if there is a finish
        #returns 'invisible_object' if there is an invisible object
        #returns 'enemy' if there is an enemy
        #returns 'player' if there is a player (if input object is not a player)
        #returns 'ground_object' if there is a ground (for fall method)
        #returns 'empty' if position is empty


        #NOTICE: THIS IMPLEMENTATION IS REALLY BAD
        
        #IF PLAYER MOVES OUTSIDE LEVEL AREA, THIS METHOD RETURNS FIRST POSSIBLE OBJECT TYPE (IS CAUSED BY HOW check_pos is implemented)
        #SO IF GROUND OBJECTS AREN'T CHECKED FIRST GAME MAY ACCIDENTALLY END IF THERE IS A WIN
        #OBJECT IN FIRST INDEX OF STATIC OBJECT LIST. SAME STYLE CAN HAPPEN IF ENEMIES ARE CHECKED FIRST,
        #THEN PLAYER LOSES GAME ACCIDENTALLY
        
        #These methods check_position, check_position_jump and check_position_fall should be rewritten with better code (also those check_pos methods are horrible)
        #(after all the changes, all the moving methods should also updated)

        

        #check if there is a ground object

        for i in range(0,len(self.ground_objects)):
            
            pos = self.ground_objects[i].position

            if not self.check_pos(pos,x_min,x_max,y_min,y_max,dynamic_object.speed_x):
            
                return 'ground_object'
        
        #check if there is a static object

        
        
        
        for i in range(0,len(self.static_objects)):
            #eli se mika tassa ei ole hyvaa on se, etta jos on vain yksi objekti, win objekti, (tai win objekti indeksissa 1) ja pelaaja menee pelialueen ulkopuolelle,
            #niin palautetaan win objektin tyyppi ja peli paattyy. taman takia ground objektien testaamisen pitaa ehdottamisti olla ensimmaisena
            
            pos = self.static_objects[i].position

            if not self.check_pos(pos,x_min,x_max,y_min,y_max,dynamic_object.speed_x):
                    return self.static_objects[i].type

        

        #check if there is an enemy

        for i in range(0,len(self.enemies)):
            #first check that input object is not compared
            if dynamic_object != self.enemies[i]:
                pos = self.enemies[i].position
                
                #indentation here is extremely crusial otherwise old value may be compared
                if not self.check_pos(pos,x_min,x_max,y_min,y_max,dynamic_object.speed_x):
                    #check that enemy is not destroyed
                    if not self.enemies[i].destroyed:
                        return self.enemies[i].type
            
        #if dynamic_object is not destroyed enemy, also check if there is a player in that position
            
        if dynamic_object.type == 'enemy':
            if not dynamic_object.destroyed:
                
                if not self.check_pos(self.player.position,x_min,x_max,y_min,y_max,dynamic_object.speed_x):
                    return self.player.type
                    
            
        # if we haven't returned anything yet, position is free
        
        return 'empty'



    def check_position_jump(self,dynamic_object,x_min,x_max,y_min,y_max, jump_x):
        #check if a new position is ok to move into

        #returns 'visible_object' if there is visible object in that position
        #return 'finish_object' if there is a finish
        #returns 'invisible_object' if there is an invisible object
        #returns 'enemy' if there is an enemy
        #returns 'player' if there is a player (if input object is not a player)
        #returns 'ground_object' if there is a ground (for fall method)
        #returns 'empty' if position is empty

        #This method has the same flaws as check_position

        #jump_x is 0 if jump is 'up' jump and else player.jump_x

        #check if there is a ground object

        for i in range(0,len(self.ground_objects)):
            pos = self.ground_objects[i].position

            if not self.check_pos_jump(pos,x_min,x_max,y_min,y_max, jump_x, dynamic_object.jump_y):
    
                return 'ground_object'
        
        #check if there is a static object

        
        
        for i in range(0,len(self.static_objects)):
            pos = self.static_objects[i].position

            if not self.check_pos_jump(pos,x_min,x_max,y_min,y_max, jump_x, dynamic_object.jump_y):
                    return self.static_objects[i].type

        

        #check if there is an enemy

        for i in range(0,len(self.enemies)):
            #fist check that input object is not compared
            if dynamic_object != self.enemies[i]:
                pos = self.enemies[i].position

                if not self.check_pos_jump(pos,x_min,x_max,y_min,y_max, jump_x, dynamic_object.jump_y):
                    #check that enemy is not destroyed
                    if not self.enemies[i].destroyed:
                        return self.enemies[i].type
            
                            
            
        # if we haven't returned anything yet, position is free
        
        return 'empty'




    def check_position_fall(self,dynamic_object,x_min,x_max,y_min,y_max):
        #check if a new position is ok to move into

        #returns 'visible_object' if there is visible object in that position
        #return 'finish_object' if there is a finish
        #returns 'invisible_object' if there is an invisible object
        #returns 'enemy' if there is an enemy
        #returns 'player' if there is a player (if input object is not a player)
        #returns 'ground_object' if there is a ground (for fall method)
        #returns 'empty' if position is empty

        #This method has the same flaws as check_position


        #check if there is a ground object

        for i in range(0,len(self.ground_objects)):
            pos = self.ground_objects[i].position
            
            #This implementation is extremely heavy and it's one cause why game is unresponsive if currently played level has a lot of static objects and enemies
            if not self.check_pos_fall(pos,x_min,x_max,y_min,y_max,dynamic_object.fall_y,'ground'):
                
                for j in range(0,len(self.static_objects)):
                    pos = self.static_objects[j].position

                    if not self.check_pos_fall(pos,x_min,x_max,y_min,y_max,dynamic_object.fall_y,'static'):
                        return self.static_objects[j].type
                    
                return 'ground_object'
        
        #check if there is a static object
        
        for i in range(0,len(self.static_objects)):
            pos = self.static_objects[i].position
                            
            if not self.check_pos_fall(pos,x_min,x_max,y_min,y_max,dynamic_object.fall_y,'static'):
                    return self.static_objects[i].type

        

        #check if there is an enemy

        for i in range(0,len(self.enemies)):
            #fist check that input object is not compared
            if dynamic_object != self.enemies[i]:
                pos = self.enemies[i].position

                if not self.check_pos_fall(pos,x_min,x_max,y_min,y_max,dynamic_object.fall_y,'enemy'):
                    #check that enemy is not destroyed
                    if not self.enemies[i].destroyed:
                        return self.enemies[i].type
            
        #if dynamic_object is not a destroyed enemy, also check if there is a player in that position
            
        if dynamic_object.type == 'enemy':
            if not dynamic_object.destroyed:
                
                if not self.check_pos_fall(self.player.position,x_min,x_max,y_min,y_max,dynamic_object.fall_y,'player'):
                    return self.player.type
                    
            
        # if we haven't returned anything yet, position is free
    
        return 'empty'




    def check_pos(self,pos,x_min,x_max,y_min,y_max,speed):
        #This method looks horrible

        # helper method called by check_position
        # pos is Position object
        
        #This method works only for move method colloision detection
        #It does not work for fall method
        #it may not work if a bigger object is trying to get to a smaller object location, but this should now be fixed

        if (x_max > pos.x_min and x_max <= pos.x_max) or ( x_min > pos.x_min and x_min < pos.x_max) \
            or ( x_min > pos.x_max and (x_min - speed) < pos.x_min) or (x_min < pos.x_min and (x_min + speed) > pos.x_min):
                
            #complexity is caused by different object widths and move values
            # 1 (or sentence) object completely inside static object or right corner is inside
            # 2 left corner of the object is inside a static object
            # 3 object is trying to pass through a static object from left
            # 4 object is trying to pass through a static object from right
            
           
                
                
 
            if (y_min <= pos.y_min and y_max >= pos.y_max) or (y_min <= pos.y_min and y_min > pos.y_max) \
                or (y_max < pos.y_min and y_max > pos.y_max):
                # 1 object completely inside static object
                # 2 object's upper corner outside object but lower inside
                # 3 object's lower corner outside object but upper inside
                
                return False
            
        if (x_min < Position.Distance_x ) or (x_max > self.Width) :
            # 1 object outside playfield's left limit
            # 2 object outside playfiled's right limit
        
            
            return False
    
        return True


    def check_pos_jump(self, pos, x_min, x_max, y_min, y_max, jump_x, jump_y):
        #just as horrible as check_pos

        # helper method called by check_position
        # pos is Position object
        
        #This method works for jump method colloision detection
        #During 'up' jump jump_x = 0

        if (x_max > pos.x_min and x_max <= pos.x_max) or (pos.x_min >= x_min and pos.x_max <= x_max) or( x_min > pos.x_min and x_min < pos.x_max) \
            or ( x_min > pos.x_max and (x_min - jump_x) < pos.x_min) or (x_min < pos.x_min and (x_min + jump_x) > pos.x_min):
                
            #complexity is caused by different object widths and move values
            # 1 (or sentence) object completely inside static object or right corner is inside
            # 2 player is jumping through an enemy directly above and the enemy is smaller (or equal size)
            # 3 left corner of the object is inside a static object
            # 4 object is trying to pass through a static object from left
            # 5 object is trying to pass through a static object from right
            
            
                
                
 
            if (y_min <= pos.y_min and y_max >= pos.y_max) or (y_min <= pos.y_min and y_min > pos.y_max) \
                or (y_max < pos.y_min and y_max > pos.y_max) or (pos.y_min <= y_min and pos.y_max >= y_max) or (y_min < pos.y_max and y_max + jump_y >= pos.y_min):
                
                # 1 object completely inside static object
                # 2 object's upper corner outside object but lower inside
                # 3 object's lower corner outside object but upper inside
                # 4 an enemy object completely inside a player (static objects are bigger than a player so this never is true for them)
                # 5 object is trying to jump through an other object
                
              
                return False
            
        if (x_min < Position.Distance_x ) or (x_max > self.Width) :
            # 1 object outside playfield's left limit
            # 2 object outside playfiled's right limit
        
            
            return False
    
        return True

    def check_pos_fall(self,pos,x_min,x_max,y_min,y_max,fall_y,object_type):
        #this is also a horrible method
        
        # helper method called by check_position
        # pos is Position object
        # object_type tells which object type positions are compared
        
        #This method work only for fall method colloision detection
        #It does not work for move method
        #fal_y should be player or enemy fall_y
        #pos is the comparison object position

        if (x_max > pos.x_min and x_max <= pos.x_max) or ( x_min > pos.x_min and x_min < pos.x_max)\
           or (pos.x_max <= x_max and pos.x_min >= x_min):
        
            
                
            #complexity is caused by different object widths and move values
            # 1 (or sentence) object completely inside static object or right corner is inside
            # 2 left corner of the object is inside a static object
            # 3 dynamic object is completely outside of a static object (player falls on an enemy which is much smaller size)
           
            
           
                
                
 
            if (y_min <= pos.y_min and y_max >= pos.y_max) or (y_min <= pos.y_min and y_min > pos.y_max) \
                or (y_max < pos.y_min and y_max > pos.y_max) or (y_max >= pos.y_min and y_min - fall_y < pos.y_max):
                # 1 object completely inside static object
                # 2 object's upper corner outside object but lower inside
                # 3 object's lower corner outside object but upper inside
                # 4 object is trying to fall through some other object
                                                                 
                
                return False
            
        if object_type == 'ground' and ((x_min < Position.Distance_x ) or (x_max > self.Width)) :
            # 1 object outside playfield's left limit
            # 2 object outside playfiled's right limit
            
            return False
    
        return True

    


    


    def get_enemy_object_at_position(self,x_min,x_max,y_min,y_max, comparison):
        #if there is an enemy at the position, returns the enemy object
        #otherwise returns None

        #comparison is an enemy object which is trying to move if this method is called from update_enemies
        #if player is trying to move comparison is always not an enemy object
        
        

        for i in range(len(self.enemies)):

            if comparison != self.enemies[i]:
                #This needs to be checked so that this method doesn't return object itself
                
                pos = self.enemies[i].position
            
            
                if (x_max > pos.x_min and x_max <= pos.x_max) or ( x_min > pos.x_min and x_min < pos.x_max) \
                    or (pos.x_min >= x_min and pos.x_max <= x_max):
                

                    # 1. player completely inside an enemy object or right corner is inside
                    # 2. left corner of the player is inside an enemy object
                    # 3. an enemy object is completely inside player (or directly on the player)
                
                
                    if (y_min <= pos.y_min and y_max >= pos.y_max) or (y_min <= pos.y_min and y_min > pos.y_max) \
                        or (y_max < pos.y_min and y_max > pos.y_max):
                        # 1. player completely inside an enemy object
                        # 2. player's upper corner outside an enemy but lower inside
                        # 3. player's lower corner outside an enemy but upper inside

                        if not self.enemies[i].destroyed:
                            #check the enemy isn't destroyed already
                        
                            return self.enemies[i]  

        #if code reaches this line, there was is no enemy at that position
        return None


    def get_enemy_below (self,x_min,x_max,y_min,comparison, y_value):
        #This object is pretty much same as get_enemy_object_at_position but this only requires that an enemy is directly below
        #This is called from set_object_to_ground_level

        #enemy must be above y_value (or at y_value)


        for i in range(len(self.enemies)):

            if comparison != self.enemies[i]:
                #This needs to be checked so that this method doesn't return object itself
                
                pos = self.enemies[i].position
            
            
                if (x_max > pos.x_min and x_max <= pos.x_max) or ( x_min > pos.x_min and x_min < pos.x_max) \
                    or (pos.x_min >= x_min and pos.x_max <= x_max):
                

                    # 1. player completely inside an enemy object or right corner is inside
                    # 2. left corner of the player is inside an enemy object
                    # 3. an enemy object is completely inside player (or directly on the object)
                
                
                    if y_min <= pos.y_max and pos.y_min <= y_value:
                        # an enemy object is below the object which is dropping
                        
                        if not self.enemies[i].destroyed:
                            #check the enemy isn't destroyed already
                            return self.enemies[i]

        #if code reaches this line, there was is no enemy at that position
        return None

    def get_player (self,x_min,x_max,y_min, y_value):
        #This is a helper method used by set_objects_to_ground_level
        #it returns True if player is at the position
        #player must be found above y_value
        
        if (x_max > self.player.position.x_min and x_max <= self.player.position.x_max) or ( x_min > self.player.position.x_min and x_min < self.player.position.x_max) \
                    or (self.player.position.x_min >= x_min and self.player.position.x_max <= x_max):



            if y_min <= self.player.position.y_max and self.player.position.y_min <= y_value:
                        # an enemy object is above the player
                        

                        return True

        return False #player object wasn't at the position

            

    def get_static_object_at_position(self,x_min,x_max,y_min,y_max,object_type):
        #gets a dynamic object at the specified position
        #object_type tells the static object type, if object_type is '' all static objects are checked
        # this method is called by set_object_to_ground_level

        pos_changed = False 
        
        for i in range(len(self.static_objects)):
            if object_type == '':
                pos = self.static_objects[i].position
                pos_changed = True
                
            elif self.static_objects[i].type == object_type:
                pos = self.static_objects[i].position
                pos_changed = True

            if pos_changed:
                #This is just used to check that old position are not compared, it is not needed when object_type == ''
                #But wanted to keep this static object checking as one method

                pos_changed = False
                 
                if (x_max > pos.x_min and x_max <= pos.x_max) or ( x_min > pos.x_min and x_min < pos.x_max) \
                    or (pos.x_min > x_min and pos.x_max < x_max):
                

                    # 1. dynamic object is completely inside an object or right corner is inside
                    # 2. left corner of the dynamic object is inside an object
                    # 3. an object is completely inside dynamic object                
                
                    if y_min <= pos.y_max :
                        # 1. dynamic object is above the static object

                        
                        # NOTICE: THIS WORKS ONLY BECAUSE UPPER STATIC OBJECTS HAVE SMALLER INDEXES IN THE LIST THAN LOWER OBJECTS
                        # (parse_gamefield creates those smaller indexes for upper objects)
                        # IF HIGHER OBJECTS HAVEN'T SMALLER INDEXES, A DYNAMIC OBJECT WOULD NOW BE PLACED IN COMLETELY WRONG POSITION IN set_object_to_ground_level 
                        
                        
                    
                        return self.static_objects[i]

        #if code reaches this line, there was is no static object at that position
        return None

                
    def destroy_dynamic_object (self,x_min,x_max,y_min,dynamic_object, y_value):
        #This is just a helper method for set_object_to_ground_level
        #y_value is the y which above object must be found else it won't be destroyed
        
        #It needs to be checked that there is no enemy object at that position, (this is caused by the poor implementation of position check methods)
        enemy = self.get_enemy_below(x_min,x_max,y_min, dynamic_object, y_value)

        if enemy:
                #destroy the enemy
                enemy.set_destroyed()
                
        #and if dynamic object is an enemy also player must be checked
        if dynamic_object.type == 'enemy':
            player = self.get_player (x_min,x_max,y_min, y_value)

            if player:
                #an enemy has destroyed the player, game is over
                GameField.Fail = True
                GameField.Game_running = False
                

    def set_object_to_ground_level(self,dynamic_object,level):
        #this method is called when dynamic_object is in air above a ground object
        #the previous phenomenon is caused by non matching jump and fall
        #values
        #level tells if player should be set on a ground or on a visible object
        #level = 'ground' or 'visible'

        #This implementation is bad, using lots of repetation. it's caused partially by poorly implementing position check methods
        #This method is used to correct position etc. (it also is just used to patch poor implementations of other methods)

        x_min = dynamic_object.position.x_min
        x_max = dynamic_object.position.x_max
        y_min = dynamic_object.position.y_min
        y_max = dynamic_object.position.y_max

        #object height
        height = dynamic_object.position.y_min - dynamic_object.position.y_max

           
                
        if level == 'ground':
            
               

            #if player is on the edge of a level, player needs to be dropped and it this method and this if segment is activated

            #first check there is no static object (finish or visible) at that position
            static_object = self.get_static_object_at_position(x_min, x_max, y_min, y_max, '')

            
            
            if static_object:
                #if there was an object
                dynamic_object.position.y_min = static_object.position.y_max
                dynamic_object.position.y_max = static_object.position.y_max - height
                

                #if dynamic object is a player and static_object finish, game is over (won the game)
                if dynamic_object.type == 'player' and static_object.type == 'finish_object':
                    GameField.Fail = False
                    GameField.Game_running = False

                elif static_object.type == 'invisible_object':

                    if dynamic_object.type == 'player':
                        #if dynamic_object is a player, game is over
                        GameField.Fail = True
                        GameField.Game_running = False

                    else:
                        #dynamic_object was an enemy, set enemy destroyed
                        dynamic_object.set_destroyed()
                        
                #otherwise there was a visible object and dynamic object just needs to be dropped on that object (already done above)

                #check and destroy possible dynamic object at the position    
                self.destroy_dynamic_object (x_min,x_max,y_min,dynamic_object, static_object.position.y_max)

            else:

                #there was no object and dynamic object can be dropped to ground level
                #if static objects aren't checked player can get stuck inside a static object near the level's edge
                
    
                for i in range(len(self.ground_objects)):
                    #find the matching ground object

                    pos = self.ground_objects[i].position

                    if(x_max >= pos.x_min and x_max <= pos.x_max) or ( x_min > pos.x_min and x_min < pos.x_max):
                        # 1. dynamic object is completely inside a ground object or right corner is inside
                        # 2. left corner of the dynamic object is inside a ground object
                    
                    
                        #height of the ground object
                        #height = dynamic_object.position.y_min - dynamic_object.position.y_max

                        #set object on a ground object
                        dynamic_object.position.y_min = pos.y_max
                        dynamic_object.position.y_max = pos.y_max - height

                        #check and destroy possible dynamic object at the position    
                        self.destroy_dynamic_object (x_min,x_max,y_min,dynamic_object, dynamic_object.position.y_min)
            

        elif level == 'visible':

            
            visible = self.get_static_object_at_position(x_min,x_max,y_min,y_max,'visible_object')
            if visible != None:
                
                #height = dynamic_object.position.y_min - dynamic_object.position.y_max
                
                #set object on a visible object
                dynamic_object.position.y_min = visible.position.y_max
                dynamic_object.position.y_max = visible.position.y_max - height

                #check and destroy possible dynamic object at the position         
                self.destroy_dynamic_object (x_min,x_max,y_min,dynamic_object, dynamic_object.position.y_min)

