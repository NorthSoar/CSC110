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