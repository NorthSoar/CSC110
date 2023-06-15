# Retracted name
# CSC 110 Programming Assignment#2
# Date: 5/09/2023
"""
An archery target consists of a central circle of yellow surrounded by concentric
rings of red, blue, black and white. Each ring has the same width, which is the same as the radius of the yellow circle. Write a program that draws such a target.
Hint : Objects drawn later will appear on top of objects drawn earlier.
"""
from graphics import * # import graphics to create GUI

def main():  # defining the GUI
    win = GraphWin('Target', 800,800) # create the window
    innerCircle = Circle(Point(400,400),50) # create the inner circle
    secondCircle = Circle(Point(400,400),100) # create the 2nd ring
    thirdCircle = Circle(Point(400,400),150) # create the 3rd ring
    fourthCircle = Circle(Point(400,400),200) # create the 4th ring
    fifthCircle = Circle(Point(400,400),250) # create the 5th ring
    
    fifthCircle.draw(win).setFill('white') # draw the 5th ring first in white
    fourthCircle.draw(win).setFill('black') # draw the 4th ring first in black
    thirdCircle.draw(win).setFill('blue') # draw the 3rd ring first in blue
    secondCircle.draw(win).setFill('red') # draw the 2nd ring first in red
    innerCircle.draw(win).setFill('yellow') # draw the 1st ring first in yello
    
main() # call the program
input() # used to keep the program up