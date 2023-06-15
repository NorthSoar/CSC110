# # Retracted name
# CSC 110 Programming Assignment #13
# Date: 5/23/2023

"""
Write a python function pyramidVolume that computes and prints the volume of a pyramid given it's height (h), base length (l) and base width (w) as parameters.

Here is the formula for calculating volume:

Volume = lwh/3

Submit your code and answer the following:

What is the approximate volume of great pyramid of Giza: https://en.wikipedia.org/wiki/Great_Pyramid_of_Giza to an external site.

Here are it's approximate dimensions: height is 455.4 feet, base length and widths are 755.9 feet each. (86736214.15799998)
"""

import sys #error handling

def pyramidVolume(length, width, height): # function for the calculations
    Volume = (length * width * height)/3 # calculate pyramid volume
    return Volume # return the volume

def userinput(): # function for grabbing user input
    height = input('Enter the height of the pyramid: ') # ask for height
    length = input('Enter the length of the pyramid: ') # ask for length
    width = input('Enter the width of the pyramid: ') # ask for width
    if height == 'exit' or width == 'exit' or length == 'exit': # check if user requested to exit program
        sys.exit() # exit program
    try: # error handling
        answer = pyramidVolume(float(length), float(width), float(height)) # call function to calculate volume
    except: # if error
        print('Invalid response. Please try again. To exit program, type exit') # error code
        userinput() # ask for the user input again
    return answer # return the answer

def main(): # main function
    answer = userinput() # call the user input
    print(f'The volume of the pyramid is: {answer} cu ft') # print the answer
    main() # loop the function

print('The volume of the Great Pyramid of Giza is:', pyramidVolume(455.4,755.9,755.9), ('cu ft')) # outside main function because only need to calculate once
# the calculations are based off of the approximation given by the question, wikipedia page gives height as 481ft and width and length as 454ft 
main() # call main program
sys.exit() # exit program

