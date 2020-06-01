from init import *
# define the game function
def game(block_size=(10,10)):
     
    # initialize the pygame module and game class
    pygame.init()
    wuziqi = wuziqi_game()

    #set the block number
    wuziqi.set_block_number(block_size)

    #create the game board
    wuziqi.get_board()
    
    # load images
    logo = pygame.image.load("image/wuziqi.png")
    background = pygame.image.load('image/wooden_background.jpg')
    black_stone = pygame.image.load('image/black_stone.png')
    white_stone = pygame.image.load('image/white_stone.png')

    #set up logo
    pygame.display.set_icon(logo)
    pygame.display.set_caption("wuziqi")

    # create a surface on screen that has assigned size 
    screen = pygame.display.set_mode(wuziqi.app_size)

    #set up cursor appearence
    pygame.mouse.set_cursor(*pygame.cursors.arrow)
    
    # define a variable to control the main loop
    running = True
     
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT or type KEYDOWN and key is ESCAPE
            if (event.type == pygame.QUIT) or ((event.type == pygame.KEYDOWN) and (pygame.key.name(event.key) == 'escape')):
                #exit the main loop
                pygame.quit()
                return 'Normal Exit'
            #get mouse click events
            elif event.type == pygame.MOUSEBUTTONDOWN:
                #pass the mouse position to game class
                wuziqi.get_mouse_button(event.pos)
                #find match location for each mouse click and add to a list
                wuziqi.add_stone_location()
                #print out each move:location&color
                print(wuziqi.stone_locations[-1])


        #set up background
        screen.blit(background,(0,0))

        #set up stone color reminder for players
        #set font type&size
        font = pygame.font.Font(None, 48)
        #create text object for rendering
        reminder_text = font.render('Round', 1, wuziqi.color_black)
        #draw on the surface
        screen.blit(reminder_text,wuziqi.reminder_pos - np.array([150,-5]))
        #draw current round stone symbol on surface
        if wuziqi.stone_color == 'black':
            screen.blit(black_stone,wuziqi.reminder_pos)
        else:
            screen.blit(white_stone,wuziqi.reminder_pos)

        #set up timer
        font = pygame.font.Font(None, 36)
        tim = str(datetime.timedelta(milliseconds=pygame.time.get_ticks()))[:-7]
        timer = font.render(tim,1,wuziqi.color_black)
        screen.blit(timer,np.array(wuziqi.app_size)-np.array([100,800]))

        #set up stone number counter
        font = pygame.font.Font(None, 48)
        white_stone_number = font.render(f'{wuziqi.white_stone_number}', 1, wuziqi.color_black)
        black_stone_number = font.render(f'{wuziqi.black_stone_number}', 1, wuziqi.color_black)
        screen.blit(black_stone,np.array(wuziqi.black_stone_counter_pos)-np.array([75,5]))
        screen.blit(white_stone,np.array(wuziqi.white_stone_counter_pos)-np.array([75,5]))
        screen.blit(white_stone_number,wuziqi.white_stone_counter_pos)
        screen.blit(black_stone_number,wuziqi.black_stone_counter_pos)

        for y_pos,x_pos in enumerate(wuziqi.x_alphas[:wuziqi.line_number[0]]):

            #draw the wuziqi board
            pygame.draw.line(screen,wuziqi.color_black,wuziqi.board_pos[f"{x_pos}1"],wuziqi.board_pos[f"{x_pos}{wuziqi.line_number[0]}"],1)
            pygame.draw.line(screen,wuziqi.color_black,wuziqi.board_pos[f"A{y_pos+1}"],wuziqi.board_pos[f"{wuziqi.x_alphas[wuziqi.line_number[0]-1]}{y_pos+1}"],1)
            
            #draw axis text
            font = pygame.font.Font(None, 24)
            alphas = font.render(x_pos, 1, wuziqi.color_black)
            numerics = font.render(f"{y_pos+1}", 1, wuziqi.color_black)
            screen.blit(alphas,np.array(wuziqi.board_pos[f'{x_pos}1'])+np.array([-5,-30]))
            screen.blit(numerics,np.array(wuziqi.board_pos[f'A{y_pos+1}'])+np.array([-30,-6]))

        #display stones
        for stone in wuziqi.stone_locations:
            if stone[-1] == 'black':
                screen.blit(black_stone,np.array(wuziqi.board_pos[stone[0]])-wuziqi.stone_radius)
            else:
                screen.blit(white_stone,np.array(wuziqi.board_pos[stone[0]])-wuziqi.stone_radius)

        #check if one player won
        if wuziqi.isWin():
            pygame.quit()
            return f'{wuziqi.stone_locations[-1][-1]} Player'

        #check if the game if tied
        if wuziqi.isDraw():
            pygame.quit()
            return 'Game Tied'

        #display all draws
        pygame.display.flip()
