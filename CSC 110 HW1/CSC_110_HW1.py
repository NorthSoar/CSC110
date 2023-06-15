# Retracted name
# CSC 110 Programming Assignment#1
# Date: 4/12/2023


# Solution for part 2A
print("***********\n***********\n***********\n***********\n***********\n***********\n***********\n")
#print 11 stars on a new line 7 times


# Solution for part 2B
def spam(): #define function
    print("***********\n***********\n***********\n***********\n***********\n***********\n***********\n")
    #print 11 stars on a new line 7 times
    return(0) #return the function

spam() #call the function


# Solution for part 2C
def cleanerspam(): #define function
    for i in range(7): #loop the next line 7 times
        print("***********") #print out 11 stars
    return(0) #return the function

cleanerspam() #call the function


# Your answer for: List one advantage of each of the above three different ways
# #1 is simple to do
# #2 is modular so you don't have to type it out again if you need the to do the same operation again and can just call it instead
# #3 is scalable and modular because you can change how many times it prints out

# Solution for part3
import sys # used to terminate program

def Calc(Expression): # define expression
    if Expression == "": # checking to see if argument is empty
        sys.exit("Exited") # terminate program, "To quit early, the user can make the program crash by typing a bad expression"
    try: # runs the next line if there are no errors
        print(Expression + " = " + str(eval(Expression)))  # evaluate the expression, convert answer to string, and print question and answer
    except: # runs the next line if there are errors
        sys.exit("Exited") # terminate program, "To quit early, the user can make the program crash by typing a bad expression"

while True: # while loop for user input, "loop so that the user can perform many calculations"
    Calculator = Calc((input("Enter a math expression: "))) # calling function and asking for math expression, "you have learned how to obtain user input, store this in a variable, and evaluate it"
sys.exit() # terminate program in case any other exceptions not caught by the function, "To quit early, the user can make the program crash by typing a bad expression"