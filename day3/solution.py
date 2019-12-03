
isTest = False
inputFile = 'input.txt'
if (isTest):
    inputFile = 'test.txt'

dictList = []

def getPositionMap(inputLine):
    positions = {}
    split = inputLine.split(',')
    x = 0
    y = 0
    movCounter = 0
    for move in split:
        mDir = move[0]
        mAmount = int(move[1:])
        mult = 1
        xMov = 0
        yMov = 0
        if (mDir == 'U'):
            yMov = mAmount
        elif (mDir == 'D'):
            yMov = mAmount
            mult = -1
        elif (mDir == 'R'):
            xMov = mAmount
        elif (mDir == 'L'):
            xMov = mAmount
            mult = -1
        
        for i in range(0, xMov):
            x += 1 * mult
            movCounter += 1
            positions[(x, y)] = movCounter
        for i in range(0, yMov):
            y += 1 * mult
            movCounter += 1
            positions[(x, y)] = movCounter

    return positions

for line in open(inputFile, 'r'):
    dictList.append(getPositionMap(line))

maxX = -9999999999
maxY = -9999999999

#print(dictList)
#quit()

for dt in dictList:
    for k in dt.keys():
        if (abs(k[0]) > maxX):
            maxX = abs(k[0])
        if (abs(k[1]) > maxY):
            maxY = abs(k[1])

found = False
cRange = 1
reqDicts = len(dictList)

def allHavePosition(dicts, pos):
    count = 0
    for dt in dicts:
        if (dt.get(pos, 0) > 0):
            count += 1
    if len(dicts) == count:
        return True
    return False

matches = []

print(maxX, maxY)
print(len(dictList[0]))
print(len(dictList[1]))

def stepSum(dicts, pos):
    sum = 0
    for d in dicts:
        sum += d[pos]
    return sum

for ma in dictList[0].keys():
    if (allHavePosition(dictList, ma)):
        matches.append((ma, stepSum(dictList, ma)))

    continue

   #  for rX in range(cRange * -1, cRange + 1):
   #      if (allHavePosition(dictList, (rX, cRange))):
   #          matches.append((rX, cRange))
   #      elif (allHavePosition(dictList, (rX, cRange * -1))):
   #          matches.append((rX, cRange * -1))

   #  for rY in range (cRange * -1, cRange + 1):
   #      if (allHavePosition(dictList, (cRange, rY))):
   #          matches.append((cRange, rY))
   #      if (allHavePosition(dictList, (cRange * -1, rY))):
   #          matches.append((cRange * -1, rY))
   #  cRange += 1

print('matches')
print(matches)
minLen = matches[0][1]
minP = matches[0]

for match in matches:
    if match[1] < minLen:
        minP = match
        minLen = match[1]

print(minP, minLen)

