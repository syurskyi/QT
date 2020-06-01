import os


class Config():
    # class variables, these are read from config file
    # other classes use these (below are the standard values)
    # this means that in main Config object needs to be created first and read_config
    level_number = 0
    distance_x = 50
    distance_right_limit = 50
    empty_line_height = 10
    static_object_height = 20
    static_object_width = 20
    enemy_height = 10
    enemy_width = 10
    player_height = 20
    player_width = 15
    player_speed = 5
    player_jump_x = 2
    player_jump_y  = 5
    player_fall_y = 2
    player_fall_x = player_jump_x
    enemy_speed = 1
    enemy_fall_y = 10 
    
    
    
    
    
    
    
    
    
    def __init__(self):
        self.read_config() #when config object is created, it reads config file
    
    
    


    def read_config(self):
        #NOTICE: The dir containing the config file needs to be named as game_config
        # config file needs to be named as config.txt
        # config file must have a specific format, otherwise it content is ignored

        # Returns: 0,1 or 2
        # 0 means a fatal error in reading the config file
        # 1 config file ok
        # 2 smt incorrect in the config, partially using standard set values


    
        path = os.getcwd() #get the current working dir
        #print(path)

        os.chdir(path) #change dir to the current working dir

        try:
            file = open('game_config\config.txt', 'r') #This works for Windows
            #file = open('game_config/config.txt', 'r') #This should work for Linux ( MacOs)

            current_line = file.readline()#read first line
            static_object_height = 0
            static_object_width = 0
            level_number = False # bool for determining if the file contains level_number
            smt_wrong = False

            while current_line:
                print('hei')

                if current_line[0] != '%':
                    #a line starting not starting with comment symbol, so it is not skipped

                    line = current_line.split() #skip whitespace

                    if len(line) != 0:
                        #skip lines that contain only whitespace
                
                        actual_line = ''
                        for i in range (len(line)):
                            actual_line += line[i] #construct a whitespace free line

                        line_content = actual_line.split(':') # : is separator in the config

                        if len(line_content) == 2:
                            #line should now contain only one parameter and set value for it
                            # else we just read a new line

                            if line_content[0] == 'level_number':
                                if check_values(line_content[1],1000,0,'int'):
                                    Gui.Level_number = int(line_content[1]) #number was ok, but this can't check if it's correct
                                    print(Gui.Level_number)

                                    # it strongly advised not to change level_number from config file, wrong number will probably resort to non-working game
                                    level_number = True

                            elif line_content[0] == 'distance_x':
                                pass

                            elif line_content[0] == 'distance_right_limit':
                                pass

                            elif line_content[0] == 'empty_line_height':
                                 pass

                            elif line_content[0] == 'static_object_height':
                                 pass

                            elif line_content[0] == 'static_object_width':
                                 pass

                            elif line_content[0] == 'enemy_height':
                                 pass

                            elif line_content[0] == 'enemy_width':
                                 pass

                            elif line_content[0] == 'player_height':
                                 pass

                            elif line_content[0] == 'player_width':
                                 pass

                            elif line_content[0] == 'player_speed':
                                 pass

                            elif line_content[0] == 'player_jump_x':
                                 pass

                            elif line_content[0] == 'player_jump_y':
                                 pass

                            elif line_content[0] == 'player_fall_y':
                                 pass

                            elif line_content[0] == 'player_fall_x':
                                 pass
                            

                            elif line_content[0] == 'enemy_speed':
                                 pass

                            elif line_content[0] == 'enemy_fall_y':
                                 pass
                            

                        

                    

                current_line = file.readline()
                

            
                

            
        

        
            file.close() #reading the file has reached end, close the file
        
            return 1
    
        except FileNotFoundError:
            print("Config file not found, check that 'config.txt' exists in dir named 'game_config'")
            return 0
    
    
    def check_values (value,max_value, min_value, value_type):
        # Help function used by read_config
        # Checks if values are correct, return True or False
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


#read_config()
