import os


class Config():
    # class variables, these are read from config file
    # other classes use these (below are the standard values)
    # this means that in the main Config object needs to be created first and read_config method called
    # when Config object is created
    
    level_number = 0   # this is used to name new levels (see leveleditor)
    
    distance_x = 50
    distance_right_limit = 50
    empty_line_height = 10
    
    static_object_height = 20
    static_object_width = 20
    enemy_height = 10
    enemy_width = 10
    player_height = 19
    player_width = 15
    
    player_speed = 5
    player_jump_x = 2
    player_jump_y  = 5
    player_jump_max_height = 60
    player_fall_y = 2
    player_fall_x = player_jump_x
    
    enemy_speed = 1
    enemy_fall_y = 10

    invisible_object_height = 5
    
    
    
    
    
    
    
    
    
    def __init__(self):
        self.config_return_value = self.read_config() #when config object is created, it reads config file
    
    
    


    def read_config(self):
        #NOTICE: The dir containing the config file needs to be named as game_config
        # config file needs to be named as config.txt
        # config file must have a specific format, otherwise it content is ignored

        # Returns: 0,1 or 2,  this return value affects how the main continues, it's stored in self.config_return_value
        # 0 means a fatal error in reading the config file
        # 1 config file ok
        # 2 smt incorrect in the config, partially using standard set values

        #However notice that this method does not check are values really functioning (ie. if speed values are too big objects can't move)
    
        path = os.getcwd() #get the current working dir
        

        try:
            os.chdir('game_config') #change to the folder where config.txt should be located
            file = open('config.txt', 'r') #This should work with every os
            

            current_line = file.readline()#read the first line
            static_object_height = 0
            static_object_width = 0
            width_counter = 0 #these are used to detect duplicates in static_object width and height
            height_counter = 0
            
            level_number = False # bool for determining if the file contains level_number
            smt_wrong = False

            while current_line:
                #loop until an EOF char is found

                if current_line[0] != '%':
                    #a line is not starting with comment symbol, so it is not skipped

                    line = current_line.split() #skip whitespace

                    if len(line) != 0:
                        #skip lines that contain only whitespace
                
                        actual_line = ''
                        for i in range (len(line)):
                            actual_line += line[i] #construct a whitespace free line

                        line_content = actual_line.split(':') # : is the content separator in the config

                        if len(line_content) == 2:
                            #the line should now contain only one parameter and a set value for it
                            # else we just read a new line
                            #now line_content[0] should contain a parameter

                            if line_content[0] == 'level_number':
                                if self.check_values(line_content[1],1000,0,'int'):
                                    Config.level_number = int(line_content[1]) #number was ok, but this can't check if it's correct
                                    

                                    # it is strongly advised not to change level_number from config file, wrong number will probably resort to a non-working game
                                    level_number = True

                            elif line_content[0] == 'distance_x':
                                if self.check_values(line_content[1],500,0,'int'):
                                    Config.distance_x = int(line_content[1])

                            elif line_content[0] == 'distance_right_limit':
                                if self.check_values(line_content[1],200,0,'int'):
                                    Config.distance_right_limit = int(line_content[1])

                            elif line_content[0] == 'empty_line_height':
                                if self.check_values(line_content[1],70,0,'int'):
                                    Config.empty_line_height = int(line_content[1])

                            elif line_content[0] == 'static_object_height':
                                height_counter += 1 #update counter
                                
                                if self.check_values(line_content[1],500,1,'int'):
                                    
                                    Config.static_object_height = int(line_content[1])
                                    static_object_height = Config.static_object_height #this is just for detecting that player and enemy's heights are correct

                            elif line_content[0] == 'static_object_width':
                                width_counter += 1 #update counter
                                
                                if self.check_values(line_content[1],500,1,'int'):
                                    Config.static_object_width = int(line_content[1])
                                    static_object_width = Config.static_object_width # same use purpose as static_object_height

                            elif line_content[0] == 'enemy_height':
                                if self.check_values(line_content[1],static_object_height -1,0,'int'):
                                    Config.enemy_height = int(line_content[1])
                                else:
                                    #enemy height is not correct in relation to static_object
                                    smt_wrong = True
                                    
                                

                            elif line_content[0] == 'enemy_width':
                                if self.check_values(line_content[1],static_object_width,0,'int'):
                                    Config.enemy_width = int(line_content[1])
                                else:
                                    #enemy width is not correct in relation to static_object
                                    smt_wrong = True

                            elif line_content[0] == 'player_height':
                                if self.check_values(line_content[1],static_object_height -1 ,0,'int'):
                                    Config.player_height = int(line_content[1])
                                else:
                                    #player height is not correct in relation to static_object
                                    smt_wrong = True
                                
                                
                                

                            elif line_content[0] == 'player_width':
                                if self.check_values(line_content[1],static_object_width,0,'int'):
                                    Config.player_width = int(line_content[1])
                                else:
                                    #player width is not correct in relation to static_object
                                    smt_wrong = True

                            elif line_content[0] == 'player_speed':
                                if self.check_values(line_content[1],100,0,'float'):
                                    Config.player_speed = float(line_content[1])
                                    

                            elif line_content[0] == 'player_jump_x':
                                if self.check_values(line_content[1],50,0,'float'):
                                    Config.player_jump_x = float(line_content[1])

                            elif line_content[0] == 'player_jump_y':
                                if self.check_values(line_content[1],static_object_height,1,'int'):
                                    Config.player_jump_y = int(line_content[1])
                                else:
                                    #the jump value is incorrect
                                    smt_wrong = True
                                
                            elif line_content[0] == 'player_jump_max_height':
                                if self.check_values(line_content[1],1000,0,'int'):
                                    Config.player_jump_max_height = int(line_content[1])

                            elif line_content[0] == 'player_fall_y':
                                if self.check_values(line_content[1],static_object_height,1,'int'):
                                    Config.player_fall_y = int(line_content[1])
                                else:
                                    #the fall value is incorrect
                                    smt_wrong = True

                            elif line_content[0] == 'player_fall_x':
                                if self.check_values(line_content[1],50,0,'float'):
                                    Config.player_fall_x = float(line_content[1])
                            

                            elif line_content[0] == 'enemy_speed':
                                if self.check_values(line_content[1],100,0,'float'):
                                    Config.enemy_speed = float(line_content[1])

                            elif line_content[0] == 'enemy_fall_y':
                                if self.check_values(line_content[1],static_object_height,1,'int'):
                                    Config.enemy_fall_y = int(line_content[1])
                                else:
                                    #the fall value is incorrect
                                    smt_wrong = True

                            elif line_content[0] == 'invisible_object_height':
                                if self.check_values(line_content[1],static_object_height,0,'int'):
                                    Config.invisible_object_height = int(line_content[1])

                                else:
                                    #the invisible_object_height is incorrect'
                                    smt_wrong = True
                            

                        

                    

                current_line = file.readline() #this is inside the loop, when the line content is checked, read a new line

            os.chdir(path) #after the loop, change dir to the current working dir
        
            file.close() #reading the file has reached end, close the file

            if Config.static_object_height <= Config.player_height or Config.static_object_height <= Config.enemy_height \
                or Config.static_object_width < Config.player_width or Config.static_object_height < Config.enemy_width:
                    #user has set only static object width or height value and those values are incorrect
                    #this is added later (after minor errors emerged in the final test of this game) and this makes those earlier smt_wrong check partially unnecessary
                    smt_wrong = True

            
            if not level_number:
                return 0 #the file is fatally malformed


            
            
            elif smt_wrong or width_counter > 1 or height_counter > 1:
                #if static_object width or height is > 1, there is duplicates (which are not allowed)
                # Object height and width values or jump/fall values may be incorrect, use standard values
                
                Config.static_object_height = 20
                Config.static_object_width = 20
                Config.enemy_height = 10
                Config.enemy_width = 10
                Config.player_height = 19
                Config.player_width = 15


                
                Config.player_jump_x = 2
                Config.player_jump_y  = 5
                Config.player_jump_max_height = 60
                Config.player_fall_y = 2
                Config.player_fall_x = Config.player_jump_x
                Config.enemy_fall_y = 10
                
                Config.invisible_object_height = 5

                return 2 
                
            
            return 1 #everything went fine
    
        except FileNotFoundError:
            #a major error occurred
            os.chdir(path) #change dir to the current working dir
            return 0
    
    
    def check_values (self,value,max_value, min_value, value_type):
        # A help method used by read_config
        # Checks if values are correct, returns True or False
        # value is the value to be checked in a string format
        # max value is the biggest value for the parameter
        # min value is the smallest value for the parameter
        # value_type is int or float

        if value_type == 'int':
            try:
                value_int = int(value)
            
                if value_int <= max_value and value_int >= min_value:
                    #the value is ok
                    return True

            except ValueError:
                # ValueError is raised if user has set value that is not a number
                return False

        elif value_type == 'float':
            try:
                value_float = float(value)
                if value_float <= max_value and value_float >= min_value:
                    #the value is ok
                    return True

            except ValueError:
                # ValueError is raised if user has set value that is not a number
                return False
        
        return False  #if function reaches this line value hasn't been ok



   

