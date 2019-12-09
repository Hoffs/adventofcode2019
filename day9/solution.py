import itertools
import sys

IS_DEBUG = False

def parseOp(op):
    op = str(op).rjust(5, '0')
    opCode = int(op[-2:])
    modThird = int(op[0])
    modSecond = int(op[1])
    modFirst = int(op[2])
    return (opCode, modFirst, modSecond, modThird) 

def dprint(*objects, sep=' ', end='\n', file=sys.stdout, flush=False):
    if IS_DEBUG:
        print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

def getAddress(inArr, pos, mod, relBase):
    try:
        if mod == 0:
            return inArr[pos]
        elif mod == 1:
            return pos
        elif mod == 2:
            return inArr[pos] + relBase
    except IndexError:
        return 0

def getValue(inArr, pos, mod, relBase):
    dprint('DEBUG GET', 'pos', pos, 'mod', mod, 'rel', relBase)
    try:
        return int(inArr[getAddress(inArr, pos, mod, relBase)])
    except IndexError:
        return 0

def assignValue(inArr, pos, value):
    if (pos >= len(inArr)):
        inArr += (list([0 for x in range(0, pos - len(inArr) + 1)]))
    inArr[pos] = value

def inputFetcher(inputs):
    idx = 0
    locInputs = inputs
    def fetch():
        nonlocal idx
        if idx < len(locInputs):
            val = inputs[idx]
            idx += 1
            return val
        else:
            return int(input('INPUT: '))
    
    def add(val):
        locInputs.append(val)

    return (fetch, add)

def runnerVM(memory, fetchInput):
    currPos = 0
    relBase = 0

    while True:
        (opCode, modFirst, modSecond, modThird) = parseOp(memory[currPos])
        dprint('DEBUG', 'relative base', relBase, 'pos', currPos, 'op', opCode, 'memory', memory)

        if opCode == 1:
            a = getValue(memory, currPos + 1, modFirst, relBase)
            b = getValue(memory, currPos + 2, modSecond, relBase)
            c = getAddress(memory, currPos + 3, modThird, relBase)
            assignValue(memory, c, a + b)
            currPos += 4
        elif opCode == 2:
            a = getValue(memory, currPos + 1, modFirst, relBase)
            b = getValue(memory, currPos + 2, modSecond, relBase)
            c = getAddress(memory, currPos + 3, modThird, relBase)
            currPos += 4
            assignValue(memory, c, a * b)
        elif opCode == 3:
            inpt = fetchInput()
            c = getAddress(memory, currPos + 1, modFirst, relBase)
            assignValue(memory, c, inpt)
            currPos += 2
        elif opCode == 4:
            a = getValue(memory, currPos + 1, modFirst, relBase)
            yield a
            currPos += 2
        elif opCode == 5:
            a = getValue(memory, currPos + 1, modFirst, relBase)
            b = getValue(memory, currPos + 2, modSecond, relBase)
            if a != 0:
                currPos = b
            else:
                currPos += 3
        elif opCode == 6:
            a = getValue(memory, currPos + 1, modFirst, relBase)
            b = getValue(memory, currPos + 2, modSecond, relBase)
            if a == 0:
                currPos = b
            else:
                currPos += 3
        elif opCode == 7:
            a = getValue(memory, currPos + 1, modFirst, relBase)
            b = getValue(memory, currPos + 2, modSecond, relBase)
            c = getAddress(memory, currPos + 3, modThird, relBase)
            if a < b:
                assignValue(memory, c, 1)
            else:
                assignValue(memory, c, 0)
            currPos += 4
        elif opCode == 8:
            a = getValue(memory, currPos + 1, modFirst, relBase)
            b = getValue(memory, currPos + 2, modSecond, relBase)
            c = getAddress(memory, currPos + 3, modThird, relBase)
            if a == b:
                assignValue(memory, c, 1)
            else:
                assignValue(memory, c, 0)
            currPos += 4
        elif opCode == 9:
            a = getValue(memory, currPos + 1, modFirst, relBase)
            relBase += a
            currPos += 2
        elif opCode == 99:
            return
        else:
            raise Exception('Unknown opcode ' + opCode)

def wrapperVM(memory, inputs):
    locMemory = memory.copy()
    (fetch, add) = inputFetcher(inputs)
    
    # Runner generator + Memory addition
    return (runnerVM(memory, fetch), add)


isTest = False
inputFile = 'input.txt'
if (isTest):
    inputFile = 'test.txt'

program = []

for line in open(inputFile, 'r'):
    program = [int(x.strip()) for x in line.split(',')]

(vm, add) = wrapperVM(program, [2])

for r in vm:
    print(r)
