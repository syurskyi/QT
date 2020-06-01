# ShutTheBox
Game of Shut the Box, using PyQt5  

I'm a GCSE student, so feel free to ignore this as it is not likely to be particularly worthwhile: just a small project.  
That being said, feel free to comment, though this probably won't be updated much.  

That and the dice in this game look pretty bad, so if you have your own jpgs or pngs just change the ones in the DiceFaces folder.

# History
This game was invented most likely in the Middle Ages, with a variety of origins. One of the earliest of these origins was 12th century Normandy (Northern France).  
In the modern age, some people play the game with several boxes, all with 7-9 such switches, and several pairs of dice, making the game more difficult.

# For use
You will need:  
* Python 3 installed, preferably 3.7. If it is not installed, follow these steps for Linux
> sudo apt-get install python3.7

* PyQt5 installed. if it is not installed, follow these steps for Linux
> sudo apt-get install python3-pip  
> pip3 install PyQt5

To run, go to directory and run:  
> python GameMain.py

# Rules
* First you roll the dice
* Then you flip at least one switch to be down
  * The switch/es has/ve to correspond to one of the dice, or both added together
* If all the switches are down, you win
  * This is made quite obvious
* If there are no moves that can be made in the turn, you lose
* If you can no longer play, either due to win or loss, or just don't like the way your switches have panned out, you can restart the game

***Feel free to edit the code in any clones that you download if you so wish***
