import sys # used to terminate program

def Calc(Expression): # define expression
    if Expression == "": # checking to see if argument is empty
        sys.exit("Exited") # terminate program, "To quit early, the user can make the program crash by typing a bad expression"
    Answer = eval(Expression) # evaluate the answer
    print(str(Expression) + " = " + str(Answer))  # print out problem and answer

while True: # while loop for user input, "loop so that the user can perform many calculations"
    Calculator = Calc((input("Enter a math expression: "))) # calling function and asking for math expression, "you have learned how to obtain user input, store this in a variable, and evaluate it"