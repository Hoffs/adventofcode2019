
orbits = {}

isTest = False
inputFile = 'input.txt'
if (isTest):
    inputFile = 'test.txt'

def parseOrbit(line):
    oSplit = line.split(')')
    # Orbits Who, Key of itself
    return (oSplit[0].strip(), oSplit[1].strip())

def countOrbits(orbits, orbitStartKey):
    orbitCount = 1
    orbitsPlanet = orbits[orbitStartKey]
    while (orbits.get(orbitsPlanet, None) != None):
        orbitsPlanet = orbits[orbitsPlanet]
        orbitCount += 1
    print(orbitStartKey, orbitCount)
    return orbitCount

for line in open(inputFile, 'r'):
    (who, key) = parseOrbit(line)
    orbits[key] = who

print(orbits)

# # p1 
# totalOrbits = 0
# for key in orbits.keys():
#     totalOrbits += countOrbits(orbits, key)
# 
# print(totalOrbits)
# 

# p2

def fillDescendants(orbits, startKey, desc):
    orbitsplanet = orbits[startKey]
    print(orbitsplanet)
    desc.append(orbitsplanet)
    while (orbits.get(orbitsplanet, None) != None):
        orbitsplanet = orbits[orbitsplanet]
        print(orbitsplanet)
        desc.append(orbitsplanet)


YOUdesc = []
SANdesc = []

fillDescendants(orbits, "YOU", YOUdesc)
fillDescendants(orbits, "SAN", SANdesc)

print(YOUdesc)
print(SANdesc)

firstCommon = None

Yc = 0
Sc = 0

for Yd in YOUdesc:
    for Sd in SANdesc:
        if Yd == Sd:
            firstCommon = Yd
            break
        Sc += 1
    if firstCommon != None:
        break
    Sc = 0
    Yc += 1

print(firstCommon, Yc, Sc)


