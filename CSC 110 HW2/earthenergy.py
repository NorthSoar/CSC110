# Retracted name
# CSC 110 Programming Assignment#2
# Date: 5/02/2023

"""
print ritcher scale for 1 5 9.1 9.2 9.5
print calculations for joules and tnt equivilant
joules = 10**(1.5*ritcher)+4.8
1 tnt = 4.184*10**9 joules
ask for ritcher scale
calculate joules and print
calculate tnt equivilant and print
"""

# test code
# richter = [1, 5, 9.1, 9.2, 9.5]
# print('Richter')
# for i in richter:
#   print(f'Ritcher: {i} \nJoules: {10**((1.5*i)+4.8)}\n TNT {10**((1.5*i)+4.8)/(4.184*10**9)}')

import sys # error handling

print("{0:<7}  {1:<22}  {2}".format('Richter','Joules','TNT')) # format table and print
richter = [1, 5, 9.1, 9.2, 9.5] # create list of richter scales to convert 
for i in richter: # create loop to convert richter scale to joules and TNT
    joules = 10**((1.5*i)+4.8) # convert richter to joules ahead of time to save program from having to calculate this twice
    print('{0:<7}  {1:<22}  {2}'.format(i, joules, joules/(4.184*10**9))) # print table of richter scale, joules equivalent, and convert joules to TNT equivalent before printing

richtercalc = input('Please enter a Richter scale value: ').strip() # ask user for richter scale value and strip any whitespace
try: # check if the code can be ran
    joulescalc = 10**((1.5*float(richtercalc))+4.8) # check if can convert to richter scale to joules. if can, save joulescalc so the program doesn't have to calculate it twice
except: # if the code can not be ran
    sys.exit('Invalid input. Exited.') # error code and exit program
else: # if the code can run
    print(f'Richter scale value: {richtercalc}\nEquivalence in joules: {joulescalc}\nEquivalence in tons of TNT: {joulescalc/(4.184*10**9)}') # print out richter, joules, tnt values