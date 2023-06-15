# Retracted name
# CSC 110 Programming Assignment#2
# Date: 5/09/2023

""""
Input: Two mouse clicks for the end points of the line segment.
Output:
Draw the midpoint of the segment in cyan.
Draw the line.
Print the length and the slope of the line.
Formulas:
dx = x2 - x1
dy = y2 - y1
slope = dy/dx
length = sqrt(dx2 + dy2)
"""

from graphics import * # import graphics to create GUI
from math import sqrt # import math for sqrt operator

def main(): # defining the GUI
    win = GraphWin('Line',700,700) # create a window
    linePoints = [] # create a list to store coordinate points
    for i in range(2): # create a for loop to ask for 2 mouse click
        mouse = win.getMouse() # create 2 mouse click
        linePoints.append(mouse.getX()) # add x coord of mouse click into list
        linePoints.append(mouse.getY()) # add y coord of mouse click into list
    line = Line(Point(linePoints[0],linePoints[1]),Point(linePoints[2],linePoints[3])) # create a line between the 2 points mouse clicked
    lineMidpoint = Circle(line.getCenter(),5) # create a circle at the midpoint on the line
    dx = linePoints[2] - linePoints[0] # calculate dx
    dy = linePoints[3] - linePoints[1] # calculate dy
    line.draw(win) # draw the line
    lineMidpoint.draw(win).setOutline('Cyan') # draw the midpoint with a cyan border
    try: # run next code if no errors occur during calculations
        print(f'Length = {sqrt(dx**2+dy**2)}\nSlope = {(dy/dx)-1}') # calculate and print length and slope of line. since the GUI is in the 4th quadrant multiply by -1 to flip back to first quadrant for slope
    except: # if error occur during calculations
        print('Error calculating length or slope of line. Please try again') # print error code
        win.close() # close the window
        main() # rerun the program

main() # call the program
input() # used to keep the program up