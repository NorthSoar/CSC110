# Retracted name
# CSC 110 Programming Assignment#2
# Date: 6/08/2023

"""
a. Write a function readData(filename) that will read in all the data from a text file that
consists of float data formatted such that each value is on a new line.
b. Write a function averageMPG(dataList) that calculates the average mpg for all vehicles
tested given a list of the mpg values.
c. Write a function countGasGuzzlers(list1, list2) that calculates the number of gas
guzzlers among the vehicle models tested for this program, define a “gas guzzler” as a
car that gets EITHER less than 22 mpg city OR less than 27 mpg highway.
d. Write a function output(<parameters>) to print the following output (you will
determine what parameters this function needs to have passed in to it):
i. The total number of vehicles tested
ii. The average for the city mpg for all the vehicles tested
iii. The average for the highway mpg for all the vehicles tested
iv. The number of gas guzzlers among the vehicle models tested
e. Write a program fuelEconomy.py that contains a main() function that calls all the
functions you made in parts a-d.
"""
def readData(filename): # function to read data
    list = [] # create a list
    f = open(filename, 'r') # open the file
    for i in f.readlines(): # add data from file into the list
        list.append(float(i[0:-1])) # remove the /n from the list and convert the number to float
    return list # return the list

def averageMPG(dataList): # function to create average
    average = 0.0 # create a variable called average
    for mpg in dataList: # create a loop to add all items from the list
        average += mpg # total the numbers to average variable
    return average/len(dataList) # divide the total by how many items in list and return the average

def countGasGuzzlers(list1,list2): # function to check gas guzzlers for city and hwy
    city = 0 # create variable for city gas guzzler counter
    hwy = 0 # create variable for hwy gas guzzler counter
    for gas_guzzler in list1: # for loop to iterate city
        if gas_guzzler < 22: # check if car mpg is bellow 22
            city += 1 # add 1 to the counter
    for gas_guzzler in list2: # for loop to iterate hwy
        if gas_guzzler < 27: # check if car mpg is bellow 27
            hwy += 1 # add 1 to the counter
    return city, hwy # return both counters
            
def output(city, hwy): # function "to print the following output"
    total = len(city) # variable for "The total number of vehicles tested"
    cityMPG = averageMPG(city) # varible for "average for the city mpg for all the vehicles tested"
    hwyMPG = averageMPG(hwy) # varibale for "average for the highway mpg for all the vehicles tested"
    guzzlers = countGasGuzzlers(city, hwy) # variable for "number of gas guzzlers among the vehicle models tested"
    # next 5 lines are to "print the following output"
    print(f'Number of vehicles tested: {total}')
    print(f'Average city MPG for all vehicles tested: {cityMPG}')
    print(f'Average highway MPG for all vehicles tested: {hwyMPG}')
    print(f'Number of gas guzzlers for the city: {guzzlers[0]}')
    print(f'Number of gas guzzlers for the highway: {guzzlers[1]}')
    return total, cityMPG, hwyMPG, guzzlers # returns the data as well for future usage