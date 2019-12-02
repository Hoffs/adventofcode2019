
isTest = True
inputFile = 'input.txt'
if (isTest):
    inputFile = 'test.txt'

inputLine = ''

for line in open(inputFile, 'r'):
    inputLine = line

inputSplit = inputLine.split(',')

currPos = 0

while inputSplit[currPos] != '99':
    fromA = int(inputSplit[currPos+1])
    fromB = int(inputSplit[currPos+2])
    to = int(inputSplit[currPos+3])
    if (inputSplit[currPos] == '1'):
        result = fromA + fromB
        inputSplit[to] = result
    elif (inputSplit[currPos] == '2'):
        result = fromA * fromB
        inputSplit[to] = result
    currPos += 4

print(inputSplit)
