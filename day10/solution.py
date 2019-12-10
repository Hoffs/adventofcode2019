import sys
# Use patterns, calculate what kind of occurance pattern it follows +X+Y and then use that searching for blocking.

import math

isTest = False
inputFile = 'input.txt'
if (isTest):
    inputFile = 'test.txt'

grid = {}
asteroids = []
x = 0
y = 0
for line in open(inputFile, 'r'):
    x = 0
    for symbol in line.strip():
        grid[(x, y)] = symbol
        if symbol == "#":
            asteroids.append((x, y))
        x += 1
    y += 1

# pattern - x, y
def normalizePattern(pattern):
    x, y = pattern
    factor = math.gcd(abs(x), abs(y))
    return (x // factor, y // factor)


DEBUG=False
def dprint(*objects, sep=' ', end='\n', file=sys.stdout, flush=False):
    if DEBUG:
        print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

def getPatternRepeats(cX, cY, dX, dY, pattern):
    pX, pY = pattern
    c = 0
    while cX != dX or cY != dY:
        cX += pX
        cY += pY
        c += 1
    return c

def findDetectablePatternsNaiive(cPos, asteroids):
    patterns = {}
    cX, cY = cPos
    for (aX, aY) in asteroids:
        if aX == cX and aY == cY:
            continue
        pattern = (aX - cX, aY - cY)
        normPattern = normalizePattern(pattern)
        cVal = patterns.get(normPattern, [])
        cVal.append((aX, aY))
        # This could be done once in last/p2 part
        cVal.sort(key=lambda v: getPatternRepeats(cX, cY, v[0], v[1], normPattern))
        patterns[normPattern] = cVal

    # Returns detectable asteroid count
    return patterns

gPatterns = {}
maxAC = 0
maxAP = (0, 0)
for aster in asteroids:
    dt = findDetectablePatternsNaiive(aster, asteroids)
    gPatterns[aster] = dt
    if len(dt.keys()) > maxAC:
        maxAC = len(dt.keys())
        maxAP = aster

print(maxAC)

def getAngle(cX, cY, pX, pY):
    res = math.degrees(math.atan2(pX, pY * -1))
    if res < 0:
        res += 360
    return res

def findPosOfXDestructedAsteroid(center, patterns, desiredX):
    global DEBUG
    cX, cY = center

    sortedPatterns = sorted(patterns.keys(), key=lambda p: getAngle(cX, cY, p[0], p[1]))

    destr = 0
    idx = 0
    pCopy = patterns.copy()
    while True:
        key = sortedPatterns[idx]
        idxAsts = pCopy[key]
        if len(idxAsts) == 0:
            idx += 1
            continue

        destr += 1
        if destr == 200:
            print(idxAsts[0][0] * 100 + idxAsts[0][1])
            break
        pCopy[key] = idxAsts[1:]
        idx += 1
        if idx >= len(sortedPatterns):
            idx = 0

findPosOfXDestructedAsteroid(maxAP, gPatterns[maxAP], 200)
