import itertools

def parseOp(op):
    op = str(op).rjust(5, '0')
    opCode = int(op[-2:])
    modThird = int(op[0])
    modSecond = int(op[1])
    modFirst = int(op[2])
    return (opCode, modFirst, modSecond, modThird) 

def getValue(inArr, pos, mod, relBase):
    if mod == 0:
        return int(inArr[int(inArr[pos])])
    elif mod == 1:
        return int(inArr[pos])
    elif mod == 2:
        return int(inArr[int(inArr[relBase + pos])])
    else:
        raise Exception('Bad modifier ' + mod)

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

        if opCode == 1:
            a = getValue(memory, currPos + 1, modFirst, relBase)
            b = getValue(memory, currPos + 2, modSecond, relBase)
            c = getValue(memory, currPos + 3, 1)
            memory[c] = a + b
            currPos += 4
        elif opCode == 2:
            a = getValue(memory, currPos + 1, modFirst, relBase)
            b = getValue(memory, currPos + 2, modSecond, relBase)
            c = getValue(memory, currPos + 3, 1)
            currPos += 4
            memory[c] = a * b
        elif opCode == 3:
            inpt = fetchInput()
            c = getValue(memory, currPos + 1, 1)
            memory[c] = inpt
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
            c = getValue(memory, currPos + 3, 1)
            if a < b:
                memory[c] = 1
            else:
                memory[c] = 0
            currPos += 4
        elif opCode == 8:
            a = getValue(memory, currPos + 1, modFirst, relBase)
            b = getValue(memory, currPos + 2, modSecond, relBase)
            c = getValue(memory, currPos + 3, 1)
            if a == b:
                memory[c] = 1
            else:
                memory[c] = 0
            currPos += 4
        elif opCode == 9:
            a = getValue(memory, currPos + 1, modFirst, relBase)
            relBase = a
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


isTest = True
inputFile = 'input.txt'
if (isTest):
    inputFile = 'test.txt'

program = []

for line in open(inputFile, 'r'):
    program = [int(x.strip()) for x in line.split(',')]

(vm, add) = wrapperVM(program, [1])

for r in vm:
    print(r)
