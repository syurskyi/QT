from gui import *

#This starts the game (this is the main for the game)

if __name__=="__main__":

    #create a main qt5 object to run the whole program (event loop)
    app = QApplication(sys.argv)
    app.setApplicationName('Gui')


    config = Config()
    #create config object, this must be done before creating gui or gamefield objects
    #config object is used to set constant values for jumping, moving, object size and so on

    if config.config_return_value:
        #If is true when return value is 1 or 2

        if config.config_return_value == 2:
            print('NOTICE: There is something wrong in the config file')
            print('The game is partially using standard set values')


        path = os.getcwd() #get the current working dir
        
        os.chdir('game_levels')   
        
        file = open('game_testi.txt','r')
        

        os.chdir(path) #change dir to the current working dir

        #create a GameField object which handles main game logic
        gamefield = GameField()

        #parse a starting level for the main game
        gamefield.parse_gamefield(file)
        file.close()
    
    
        #create gui object that handles the user interface
        main = Gui()
    
    
   
        #set the starting level  
        main.set_gamefield(gamefield)
        main.gamefield_level = 'game_testi.txt'
    
   
        #start to show the user interface
        main.show()

        #stop the main when app object is killed
        sys.exit(app.exec_())


    else:
        #when config is 0

        print('A fatal error happened during reading the config file')
        print("Check that 'config.txt' file exists in a folder named 'game_config', one level below the current working directory")
        print("Check also that 'config.txt' contains 'level_number' ") 
