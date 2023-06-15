import sys # for error handling
       
def Calculations(Conversion): # putting the program in a module
    try: # checking for a valid input
        Converted = float(Conversion) * 128 # if the input is valid, calculate and store in Converted
    except: # if input is invalid and the math can't be done
        sys.exit('Invalid input. Expected number as input. Exited') # give an error and close the program
    else: # if try statement successfully ran
        print(f'There are {Converted} fluid ounces in {Conversion} gallons') # print out result using the template given
       
while True: # have the program continuously to allow multiple conversions
    Calculations((input('Please enter number of gallons to convert it into fluid ounces: '))) # ask for an input and runs the function/module