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

(vm, add) = wrapperVM(program, [1])

grid = {}

x = 0
y = 0
direction = 0 # 0 - 360, 0 UP, 90 RIGHT, 180 DOWN, 270 LEFT

vmIter = iter(vm)
for color in vmIter:
    turn = next(vmIter)
    grid[(x, y)] = color
    if turn == 0:
        direction -= 90
    elif turn == 1:
        direction += 90

    if direction < 0:
        direction += 360
    if direction >= 360:
        direction -= 360

    if direction == 0:
        y += 1
    elif direction == 90:
        x += 1
    elif direction == 180:
        y -= 1
    elif direction == 270:
        x -= 1

    add(grid.get((x, y), 0))

print(len(grid))

minY = 10000000
minX = 10000000
maxY = -1000000
maxX = -1000000

for (gX, gY) in grid:
    if gX < minX:
        minX = gX
    if gY < minY:
        minY = gY
    if gX > maxX:
        maxX = gX
    if gY > maxY:
        maxY = gY

for y in range(minY, maxY + 1):
    for x in range(minX, maxX + 1):
        letter = grid.get((x, y), ' ')
        if letter == 0:
            letter = ' ';
        print(letter, end="")
    print()
