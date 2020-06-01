from gamefield import GameField

def main():

    file1 = open('game_testi.txt','r')
    gamefield1 = GameField()
    print(gamefield1.player)
    print(GameField.Space)
    
    

    gamefield1.parse_gamefield(file1)
    print('leveli on :{}'.format(gamefield1.max_level))
    print(gamefield1.player)

    print(gamefield1.player.position.x_min) #this should be 100
    print(gamefield1.player.position.x_max) #this should be 130
    print(gamefield1.player.position.y_max) #this should be 250+3*50=400
    print(gamefield1.player.position.y_min) # 460

    #those coordinates (in comments) were wrong and the should be ignored

    for i in range(0,len(gamefield1.ground_objects)):
        ob = gamefield1.ground_objects[i].position
        print('ground objekti y_min: {} y_max: {} x_min: {} x_max: {}'.format(ob.y_min,ob.y_max, ob.x_min, ob.x_max))

    print()
    for i in range (len(gamefield1.static_objects)):
        #print all positions (compare to game_testi.txt)
        ob = gamefield1.static_objects[i].position
        if gamefield1.static_objects[i].type == 'finish_object':
            print('maali loytyy')
        print('y_min: {} y_max: {} x_min: {} x_max: {}'.format(ob.y_min,ob.y_max, ob.x_min, ob.x_max))

    for i in range (len(gamefield1.enemies)):
        enemy = gamefield1.enemies[i].position 
        print('enemies in file: y_min {}, y_max {}, x_min {}, x_max {}'.format(enemy.y_min, enemy.y_max, enemy.x_min, enemy.x_max))

    enemy = gamefield1.enemies[1].position #2 enemy which is read so it's enemy at the bottom left corner
    print('enemy 2 in file: y_min {}, y_max {}, x_min {}, x_max {}'.format(enemy.y_min, enemy.y_max, enemy.x_min, enemy.x_max))

    print(gamefield1.static_objects[27].type) #shoud be invisible

    file1.close()
    print()

    file2 = open('game_testi2.txt','r')
    gamefield2 = GameField()
    gamefield2.parse_gamefield(file2) #should be same as test 1 but 1 more line so y location should be shiftet 50 down
    for i in range (len(gamefield2.static_objects)):
        #print all positions (compare to game_testi.txt)
        ob = gamefield2.static_objects[i].position
        print('y_min: {} y_max: {} x_min: {} x_max: {}'.format(ob.y_min,ob.y_max, ob.x_min, ob.x_max))

    file2.close()
    print()

    #let's test malformed files

    file3 = open ('game_testi_broken1.txt')
    #this file is missing one - so it's not well-formed

    gamefield3 = GameField()
    ret = gamefield3.parse_gamefield(file3) #should return false and print error message
    print(ret)
    file3.close()

    gamefield4 = GameField()
    file4 = open('game_testi_broken2.txt')
    #file is missing finish

    print()
    gamefield4.parse_gamefield(file4)
    file4.close()

    gamefield5 = GameField()
    file5 = open('game_testi_broken3.txt')
    #file contains too many player locations

    print()
    gamefield5.parse_gamefield(file5)
    file5.close()


    gamefield6 = GameField()
    file6 = open('game_testi_broken4.txt')
    #file contains incorrect object symbol

    print()
    gamefield6.parse_gamefield(file6)
    file5.close()

    

  

    

main()
