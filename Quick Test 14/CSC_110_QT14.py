from math import sqrt # import square root from math library

def surfaceArea(base_length, base_width, height): # function that takes in param base_length, base_width, height
    try:
        base_length = float(base_length) # convert base_length to float number
        base_width = float(base_width) # convert base_width to float number
        height = float(height) # convert height to float number
    except:
        print('Invalid input')
    try: # try to calculate
        area = base_length*base_width+base_length*sqrt((base_width/2)**2+height**2)+base_width*sqrt((base_length/2)**2+height**2)
        return area
    except:
        print('Calculation error')