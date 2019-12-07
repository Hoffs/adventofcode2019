
def getOpInfo(op):
    op = str(op).rjust(5, '0')
    opCode = int(op[-2:])
    modThird = int(op[0])
    modSecond = int(op[1])
    modFirst = int(op[2])
    return (opCode, modFirst, modSecond, modThird) 

def getValue(inArr, pos, mod):
    if (mod == 0):
        return int(inArr[int(inArr[pos])])
    elif (mod == 1):
        return int(inArr[pos])
    else:
        raise Exception('Bad modifier ' + mod)

def runCalculations(tInput):
    currPos = 0
    while True:
        (opCode, modFirst, modSecond, modThird) = getOpInfo(tInput[currPos])

        if opCode == 1:
            a = getValue(tInput, currPos + 1, modFirst)
            b = getValue(tInput, currPos + 2, modSecond)
            c = getValue(tInput, currPos + 3, 1)
            tInput[c] = a + b
            currPos += 4
        elif opCode == 2:
            a = getValue(tInput, currPos + 1, modFirst)
            b = getValue(tInput, currPos + 2, modSecond)
            c = getValue(tInput, currPos + 3, 1)
            currPos += 4
            tInput[c] = a * b
        elif opCode == 3:
            inpt = int(input("OPCODE3: "))
            c = getValue(tInput, currPos + 1, 1)
            tInput[c] = inpt
            currPos += 2
        elif opCode == 4:
            a = getValue(tInput, currPos + 1, modFirst)
            print(a)
            currPos += 2
        elif opCode == 5:
            a = getValue(tInput, currPos + 1, modFirst)
            b = getValue(tInput, currPos + 2, modSecond)
            if a != 0:
                currPos = b
            else:
                currPos += 3
        elif opCode == 6:
            a = getValue(tInput, currPos + 1, modFirst)
            b = getValue(tInput, currPos + 2, modSecond)
            if a == 0:
                currPos = b
            else:
                currPos += 3
        elif opCode == 7:
            a = getValue(tInput, currPos + 1, modFirst)
            b = getValue(tInput, currPos + 2, modSecond)
            c = getValue(tInput, currPos + 3, 1)
            if a < b:
                tInput[c] = 1
            else:
                tInput[c] = 0
            currPos += 4
        elif opCode == 8:
            a = getValue(tInput, currPos + 1, modFirst)
            b = getValue(tInput, currPos + 2, modSecond)
            c = getValue(tInput, currPos + 3, 1)
            if a == b:
                tInput[c] = 1
            else:
                tInput[c] = 0
            currPos += 4
        elif opCode == 99:
            quit()
        else:
            raise Exception('Unknown opcode ' + opCode)

isTest = False
inputFile = 'input.txt'
if (isTest):
    inputFile = 'test.txt'

for line in open(inputFile, 'r'):
    result = runCalculations(line.split(','))
    print(result)
