
isTest = False
inputFile = 'input.txt'
if (isTest):
    inputFile = 'test.txt'

program = []

width = 25
height = 6

data = []
for line in open(inputFile, 'r'):
    data = [int(x.strip()) for x in line.strip()]

layers = []
idx = 0
while idx < len(data):
    layer = {}
    for y in range(0, height):
        for x in range(0, width):
            layer[(x, y)] = data[idx]
            idx += 1
    layers.append(layer)

# P1
## def countOccurances(data, searching):
##     count = 0
##     for d in data:
##         if d == searching:
##             count += 1
## 
##     return count
## 
## minL = 0
## minC = countOccurances(layers[0].values(), 0)
## for l in layers[1:]:
##     lMinC = countOccurances(l.values(), 0)
##     if lMinC < minC:
##         minL = layers.index(l)
##         minC = lMinC
## 
## print(minL, minC)
## ocOne = countOccurances(layers[minL].values(), 1)
## ocTwo = countOccurances(layers[minL].values(), 2)
## print(ocOne * ocTwo)

finalImage = {}

for y in range(0, height):
    for x in range(0, width):
        pos = (x, y)

        for layer in layers:
            if layer[pos] != 2:
                finalImage[pos] = layer[pos]
                break
        print(finalImage[pos], end="")
    print("")


