# Retracted name
# CSC 110 Programming Assignment#2
# Date: 6/08/2023

from fuelFunctions import * # import the functions into the main program

def main(): # main function
    cityData = readData('carModelData_city.txt') # open the city file and process the data
    hwyData = readData('carModelData_hwy.txt') # open the hwy file and process the data
    output(cityData, hwyData) # call the function to gather data and print out
    
main() # call the function

# Number of vehicles tested: 35463
# Average city MPG for all vehicles tested: 22.17491529481448
# Average highway MPG for all vehicles tested: 33.08256278092686
# Number of gas guzzlers for the city: 19967
# Number of gas guzzlers for the highway: 8709