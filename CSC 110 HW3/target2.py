# Retracted name
# CSC 110 Programming Assignment#2
# Date: 5/09/2023

"""
Modify your program from part (a) above to make it interactive.
Allow the user to specify the diameter of the outermost circle of the target.
You may get this value from the user in a similar manner as the principal and apr were obtained in the futval_graph2.py program on page 105 of the textbook (2nd edition page 101).
You will need to have the graphics window adjust its size to accommodate the archery target that will be created within it. Save your new program as target2.py. 
"""

from graphics import * # import graphics to create GUI


def main():  # defining the GUI
    try: # run next code and check for invalid input
        outerDiameter = input('This program creates a target with a given diameter.\nEnter the diameter of the outermost circle: ') # ask for diameter
        outerDiameter= float(outerDiameter)/2 # convert to radius
    except: # error handling
        if outerDiameter == 'exit': # if input was to exit
            sys.exit() # close the program
        print('Invalid input. Try again. To exit, type exit') # print error code
        main() # rerun the program
    else: # run after try passes
        win = GraphWin('Target', outerDiameter*2,outerDiameter*2) # create a window the size of the diameter
        fifthCircle = Circle(Point(outerDiameter,outerDiameter),outerDiameter) # create the 5th ring with the given diameter 
        fourthCircle = Circle(Point(outerDiameter,outerDiameter),outerDiameter*0.8) # create the 4th ring 20% smaller than the 5th ring
        thirdCircle = Circle(Point(outerDiameter,outerDiameter),outerDiameter*0.6) # create the 3th ring 20% smaller than the 4th ring
        secondCircle = Circle(Point(outerDiameter,outerDiameter),outerDiameter*0.4) # create the 2th ring 20% smaller than the 3th ring
        innerCircle = Circle(Point(outerDiameter,outerDiameter),outerDiameter*0.2) # create the inner ring 20% smaller than the 2nd ring

        fifthCircle.draw(win).setFill('white') # draw the 5th ring first in white
        fourthCircle.draw(win).setFill('black') # draw the 4th ring first in black
        thirdCircle.draw(win).setFill('blue') # draw the 3rd ring first in blue
        secondCircle.draw(win).setFill('red') # draw the 2nd ring first in red
        innerCircle.draw(win).setFill('yellow') # draw the 1st ring first in yello
    input('Press <Enter> to quit.') # used to keep the program up
    win.close() # close the program when user input enter

main() # call the program