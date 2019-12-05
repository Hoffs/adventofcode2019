
def getOpInfo(op):
    pass

def runCalculations(tInput):
    currPos = 0

    while tInput[currPos] != '99':
        fromA = int(tInput[int(tInput[currPos+1])])
        fromB = int(tInput[int(tInput[currPos+2])])
        to = int(tInput[currPos+3])
        # print(fromA, fromB, to)
        
        if (tInput[currPos] == '1'):
            result = fromA + fromB
            tInput[to] = result
        elif (tInput[currPos] == '2'):
            result = fromA * fromB
            tInput[to] = result
        currPos += 4
        # print(tInput)
    return tInput[0]

isTest = False
inputFile = 'input.txt'
if (isTest):
    inputFile = 'test.txt'

inputLine = ''

for line in open(inputFile, 'r'):
    inputLine = line

originalInput = inputLine.split(',')

for noun in range(0, 100):
    for verb in range(0, 100):
        currentInput = originalInput.copy()
        currentInput[1] = noun
        currentInput[2] = verb
        print(currentInput, noun, verb)
        result = runCalculations(currentInput)
        print(result)
        if (result == 19690720):
            print(noun, verb)
            quit()          
