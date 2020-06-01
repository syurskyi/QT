def initialize():
    global game_over
    game_over = False

    global game_pause
    game_pause = False

    global time
    time = '00:00:00'

    global no_bombs
    no_bombs = 0

    global bombs
    bombs = 0

    global flag_bombs
    flag_bombs = 0

    global first_click
    first_click = False

    global first_click_xy
    first_click_xy = [0, 0]

    global music
    music = True

    global no_bomb_in_first_click
    no_bomb_in_first_click = True

    global loose_animation
    loose_animation = True

    global question_marks
    question_marks = True

    def get_bool(string):
        if 'True' in string:
            return True
        else:
            return False

    with open('global_value', 'r') as file:
        music = get_bool(file.readline())
        question_marks = get_bool(file.readline())
        no_bomb_in_first_click = get_bool(file.readline())
        loose_animation = get_bool(file.readline())


def save_values():
    with open('global_value', 'w+') as file:
        file.write(str(music))
        file.write('\n')
        file.write(str(question_marks))
        file.write('\n')
        file.write(str(no_bomb_in_first_click))
        file.write('\n')
        file.write(str(loose_animation))
        file.write('\n')




