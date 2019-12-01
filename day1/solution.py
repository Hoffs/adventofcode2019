import math

isTest = False
inputFile = 'input.txt'
if (isTest):
    inputFile = 'test.txt'

# Solution

fuelRequired = 0

for line in open(inputFile, 'r'):
    unaccountedMass = math.floor(float(line) / 3) - 2 
    fuelRequired += unaccountedMass

    while unaccountedMass > 0:
        unaccountedMass = max(math.floor(float(unaccountedMass) / 3) - 2, 0)
        fuelRequired += unaccountedMass

print(fuelRequired)
