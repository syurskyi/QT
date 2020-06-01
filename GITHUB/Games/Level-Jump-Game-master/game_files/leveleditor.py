from levelobject import LevelObject
from drawlevelobject import DrawLevelObject
from config import Config
import os

class LevelEditor:

    #class variables

    Left_arrow = 0 #these are used to detect movement in the editor
    Right_arrow = 0
    Up_arrow = 0
    Down_arrow = 0

    Key_P = 0 #tells if player wants add a player location
    Key_F = 0 #-||- a finish location
    Key_O = 0 # -||- a visible object
    Key_E = 0 # -||- an enemy
    Key_I = 0 # -||- a fall (invisible) object
    Delete = 0
    Name = 'my_level' #This is standard name for a file (number is added to the end and txt ending)

    def __init__(self):

        self.x = 0 #current x coordinate in the editor scene
        self.y = 0 #current y coordinate in the editor scene
        self.right = 0 #these are used to detect movement in the editor
        self.left = 0
        self.up = 0
        self.down = 0
        #self.delete_object = False

        self.p = 0 #these are compared to the class variables
        self.f = 0 
        self.o = 0 
        self.e = 0 
        self.i = 0
        self.delete = 0
        self.max_y = 0 #This is the lowest point in the screen (used with fall(invisible) objects)
        self.active_objects = 0 #This is used to reset max_y
        self.active_invisible = 0 #This is also used to reset max_y
        self.inactivated_object = False #This is also used to reset max_y, see reset_y_max

        #handles to objects in the scene
        self.player = None
        self.enemies = []
        self.visible = []
        self.invisible = []
        self.finish = []
        self.current = LevelObject('current')
        self.current.set_pos(self.x,self.y)

    def update_position(self):
        #updates the current object position to match user input

        if LevelEditor.Right_arrow > self.right:
            self.x +=1
            self.right = LevelEditor.Right_arrow

        if LevelEditor.Left_arrow > self.left:
            if self.x >0:
                #check that new pos is ok
                self.x -=1
            self.left = LevelEditor.Left_arrow

        if LevelEditor.Up_arrow > self.up:
            if self.y > 0:
                #check that new pos is ok
                self.y -= 1
            self.up = LevelEditor.Up_arrow

        if LevelEditor.Down_arrow > self.down:
            self.y += 1
            self.down = LevelEditor.Down_arrow

        #update the position
        self.current.set_pos(self.x,self.y)


    def update_all_positions(self):
        #This method is called from gui to add new objects and update existing objects
        self.update_position()
        self.add_new_objects()
        self.correct_fall_objects()
        
        if LevelEditor.Delete > self.delete:
            #user wants to remove a object at current pos
            self.inactivate_object()
            self.delete = LevelEditor.Delete

        self.reset_y_max()
        self.inactivated_object = True #init this value
        

    

    def add_new_objects(self):
        #This method add objects based on user input
        #update_position -method need to be called prior this method

        if LevelEditor.Key_P > self.p:
            #user wants add a player object

            #Only 1 player pos is allowed so set current player object inactive
            #if there already is a player added
            if self.player:
                if self.player.is_active:
                    self.player.inactivate() #see LevelObject
                    self.active_objects -= 1
            
                
            self.inactivate_object()

            #create the new object
            self.player = LevelObject('player')
            self.player.set_pos(self.x,self.y)
            
            self.set_max_y(self.y) #see set_max_y
            self.active_objects += 1
            
            self.p = LevelEditor.Key_P

        elif LevelEditor.Key_E > self.e:
            #user wants to add an enemy object
            
            self.inactivate_object()
            
            #create a new enemy object
            enemy = LevelObject('enemy')
            
            
            enemy.set_pos(self.x,self.y)

            #add the object to the correct list
            self.enemies.append(enemy)

            self.set_max_y(self.y)
            self.active_objects += 1

            self.e = LevelEditor.Key_E

        elif LevelEditor.Key_O > self.o:
            #user wants to add a visible object

            self.inactivate_object()

            #create a visible object
            visible = LevelObject('visible')
            visible.set_pos(self.x,self.y)
            self.visible.append(visible)

            self.set_max_y(self.y)
            self.active_objects += 1

            self.o = LevelEditor.Key_O

        elif LevelEditor.Key_F > self.f:
            #user wants add a finish object
            self.inactivate_object()

            #create a finish object
            finish = LevelObject('finish')
            finish.set_pos(self.x,self.y)
            self.finish.append(finish)

            self.set_max_y(self.y)
            self.active_objects += 1

            self.f = LevelEditor.Key_F

        elif LevelEditor.Key_I > self.i:
            #user wants add an invisible (fall) object
            self.i = LevelEditor.Key_I #this line is crusial and ensures smooth operation
            
            if self.y >= self.max_y:
                #invisible object can never be added above other objects
                self.inactivate_object()

                #create a new invisible object
                invis = LevelObject('invisible')
                invis.set_pos(self.x,self.y)
                self.invisible.append(invis)

                self.set_max_y(self.y)
                self.active_objects += 1
                self.active_invisible += 1

                
            
            
        


    def correct_fall_objects(self):
        #Fall (invisible) object can be added only on the lowest point of a level
        #This method removes those incorrectly added fall objects (gui removes them from the scene)

        for i in range(len(self.invisible)):
            if self.invisible[i].y != self.max_y: #comparing absolute coordinates (pixels)
                if self.invisible[i].is_active:
                    self.invisible[i].inactivate()
                    self.active_objects -= 1
                    self.active_invisible -= 1
                

        
    def set_max_y(self,y):
        #This is a helper method used to update max_y
        #called from add_new_objects

        if y > self.max_y:
            self.max_y = y
        
    def inactivate_object(self):
        #This is a helper method called from add_new_objects
        #It inactivates object at self.x, self.y if possible

        obj = self.get_object_at_pos(self.x,self.y)
        if obj:
            #check obj is not None
            obj.inactivate()
            self.active_objects -= 1
            self.inactivated_object = True

            if obj.object_type == 'invisible':
                
                self.active_invisible -= 1 #also this counter needs to be changed
                

    def get_object_at_pos(self,x,y):
        #This method is called to check a pos
        #If there is an object at the pos, returns the object
        #Otherwise returns None
        #Notice this is an iteration method so it's somewhat heavy

        #Iterate over all the object (not current because it doesn't behave same style)
        for i in range(0,len(self.enemies)):
            if self.enemies[i].x == x and self.enemies[i].y == y and self.enemies[i].is_active:
                #there may already be non active object in the pos (and they are have lower list indexes)
                #is active ensures that correct object is found
                return self.enemies[i]

        for i in range(0,len(self.visible)):
            if self.visible[i].x == x and self.visible[i].y == y and self.visible[i].is_active:
                return self.visible[i]

        for i in range(0,len(self.invisible)):
            if self.invisible[i].x == x and self.invisible[i].y == y and self.invisible[i].is_active:
                return self.invisible[i]

        for i in range(0,len(self.finish)):
            if self.finish[i].x == x and self.finish[i].y == y and self.finish[i].is_active:
                return self.finish[i]

        if self.player:
            #check the player is not None
            if self.player.x == x and self.player.y == y and self.player.is_active:
                return self.player

        #If code reaches this line the pos is empty
        return None


    def reset_y_max (self):
        #If scene is empty this resets max_y value so that fall object can again placed anywhere
        
        if self.active_objects == 0:
            self.max_y = 0
       

        if self.active_invisible == 0 and self.inactivated_object:
            #This is implemented this way because this requires checking max_y fewer times, only when it's needed
            #if invisible object aren't added we won't iterate unnecessarily
            #Otherwise using multiple variables to reset one variable is a bit confusing
            #This is used when user removes last invisible object to set correct max_y value
            max_values = self.get_max_y_and_max_x () # see get_max_y_and_max_x
            
            if self.max_y != max_values[0]:
                self.max_y = max_values[0] 

                
            
            
            


    def create_file(self,file_name):
        #This method is called from gui to create a file from a level which user has designed
        
        #file_name tells the level name
        #if the file name is empty or non-unique, this method uses standard naming system
        #for this reason this method needs access to Config.level_number and this method also updates
        #that number

        #the file is created if level is ok (has a player location, a finish etc)
        #the file is created under game_levels folder

        #returns created file name if file was successfully created,
        #returns 'error' if the file wasn't created successfully -> these are used in gui to inform user

        #only active object's positions are written to the file (obviously)

        #first check a player and a at least one finish pos exists
        if self.player:

            if self.player.is_active and self.check_finish_objects():
                #player and finish pos is ok

                #level seems to be ok so it can be created
                objects_list = self.sort_objects() #see sort_objects, this is a 2D list
                

                #try to save level with file_name
                standard_name = ''
                
                try:
                    path = os.getcwd() #get the current working dir
                    os.chdir('game_levels')
                    file = open(file_name + '.txt','r') #if user has given unique name this causes FileNotFoundError
                    file.close() #if file is opened, user has given non correct name and file needs to be closed

                    #create a file that has the standard name (Config.Level_number is used to make file names unique)
                    number = str(Config.level_number) #this is an int so it needs to be converted to a string
                    standard_name = LevelEditor.Name + number

                    #create a new file
                    file = open(standard_name + '.txt', 'w')

                    
                except FileNotFoundError:
                    #This is reached if user gave a valid name
                    #In worst case scenerio this is reached because user has deleted game_levels folder but there is no fix to that

                    #create a file that has the name user has given
                    file = open(file_name + '.txt', 'w')

                finally:
                    #this is executed in all cases
                    
                    self.write_file(file,objects_list)
                   
                    #file has been written and can be closed
                    file.close()
                    os.chdir(path) #change back to working dir

                    if standard_name == '':
                        #user defined name was ok
                        return file_name

                    else:
                        #Config.level_number needs to be updated
                        self.write_new_level_number()

                        return standard_name #level was saved with standard name
   


    
        #there is some error in the level if this line is reached
        return 'error'
    

    def write_file(self,file, objects):
        #This is a helper method called by create_file to write to a file
        #file is a handle to the file, file needs to be opened in write mode
        #objects is a 2d list which content needs to be written to the file

        for j in range(len(objects)):
            #the first dimension

            for i in range(0,len(objects[j])):
                #the 2nd dimension

                file.write(objects[j][i]) #objects list is containing the correct symbols (see sort_objects) which can be directly written to the file
                file.write(' ') #this is purely for aesthetic reasons (makes the file more human readable)
                
            file.write('\n') #add a line feed
            
         #the file is now written and  can be closed but it's closed in  create_file                 

        
        
    
    def check_finish_objects(self):
        #This is a helper method which just checks that there is at least one active finish object
        #Returns True if a finish object was found
        #Else returns False

        for i in range(0,len(self.finish)):
            if self.finish[i].is_active:
                return True

        return False #if this line is reached no active finish objects were found

    def get_max_y_and_max_x (self):
        #This method returns max_y and max_x
        #as list[max_y,max_x]
        #it used both by sort_objects (requires both return values) and reset_y_max (requires only y_max)

        #max values are found when all the active objects are iterated and checked

        max_y = 0
        max_x = 0

        if self.player:
            #check player is not None
        
            if self.player.is_active:
                #check the object is active
                if self.player.y > max_y:
                    max_y = self.player.y

                if self.player.x > max_x:
                    max_x = self.player.x

        for i in range(0, len(self.enemies)):
            if self.enemies[i].is_active:
                if self.enemies[i].y > max_y:
                    max_y = self.enemies[i].y
                
                if self.enemies[i].x > max_x:
                    max_x = self.enemies[i].x
                
        for i in range(0,len(self.visible)):
            if self.visible[i].is_active:
                if self.visible[i].y > max_y:
                    max_y = self.visible[i].y

                if self.visible[i].x > max_x:
                    max_x = self.visible[i].x

        for i in range(0,len(self.invisible)):
            if self.invisible[i].is_active:
                if self.invisible[i].y > max_y:
                    max_y = self.invisible[i].y

                if self.invisible[i].x > max_x:
                    max_x = self.invisible[i].x

                
       
        for i in range(0, len(self.finish)):
            if self.finish[i].is_active:
                if self.finish[i].y > max_y:
                    max_y = self.finish[i].y

                if self.finish[i].x > max_x:
                    max_x = self.finish[i].x

        #values are now updated
        return [max_y, max_x]
                    
            
    def sort_objects(self):
        #This is a helper method used by create_file, a heavy and slow method
        #This method gets the max x and y size and then sorts objects
        

        #returns 2d list of objects which has correct symbols in object's places
        #max x and y are used to create list whit correct dimensions

        #object symbols used in the files (and in the list)
        # player = 'P'
        # enemy = 'E'
        # visible_object = 'O'
        # invisible_object = 'F'
        # finish = 'F'
        # empty = '-'
        

        

        #iterate over all the object and find the correct values
        max_values = self.get_max_y_and_max_x()
        max_y = max_values[0] #this is unnecessary, could be done straighly
        max_x = max_values[1]
       
        
        # now the 2d list can be creted,
        # a bit heavy data type but it can be easily modified and somewhat easily written to a file

     
        list_2d = []
        for i in range(0,max_y+1):
            #use this to make list inmutable, max_y is the max index
            list_2d.append(['-']*(max_x +1) ) #init list whit empty symbols (note that there is x_max +1 positions because indexing starts from 0)


        #now add object to the list

        #add the player object
        list_2d[self.player.y][self.player.x] = 'P'

        #add the enemies
        for i in range(0,len(self.enemies)):
            if self.enemies[i].is_active:
                list_2d[self.enemies[i].y][self.enemies[i].x] = 'E'
        

        #add the visible objects
        for i in range(0, len(self.visible)):
            if self.visible[i].is_active:
                list_2d[self.visible[i].y][self.visible[i].x] = 'O'

        #add the invisible objects
        for i in range(0, len(self.invisible)):
            if self.invisible[i].is_active:
                list_2d[self.invisible[i].y][self.invisible[i].x] = 'F'

        #add the finish objects
        for i in range(0, len(self.finish)):
            if self.finish[i].is_active:
                list_2d[self.finish[i].y][self.finish[i].x] = 'W'


        #the list is now ready and can be returned

        return list_2d






    def write_new_level_number(self):
        #This method is called from create_file
        #It is used to append a new level number to the end of the config.txt
        #It also changes Config.level_number to the correct value

        try:
            Config.level_number += 1 #update level_number
            
            path = os.getcwd() #get the current dir
                        
            os.chdir('game_config')#this dir should contain config.txt
            
            file = open('config.txt', 'a') #we don't want to remove config.txt but append content to it

            
            file.write('\n') #add a line feed
            file.write('level_number:' + str(Config.level_number)) #append the correct level number to the file

            file.close()

        except FileNotFoundError:
            #This should never happen
            #Happens only if user has runtime deleted (or renamed but same thing) game_config folder and there is nothing that can be done to that
            print("'game_config' folder is missing")
            print("the file can't be updated")

        finally:
            os.chdir(path) #change back to the working dir
                
                
    def init_class_variables(self):
        #This method is called from gui to init all LevelEditor class variables

        LevelEditor.Left_arrow = 0 
        LevelEditor.Right_arrow = 0
        LevelEditor.Up_arrow = 0
        LevelEditor.Down_arrow = 0

        LevelEditor.Key_P = 0 
        LevelEditor.Key_F = 0 
        LevelEditor.Key_O = 0 
        LevelEditor.Key_E = 0 
        LevelEditor.Key_I = 0 
        LevelEditor.Delete = 0
                
                

        

        
                    
        
            
        
        
    
