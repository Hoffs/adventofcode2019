
rStart=168630
rEnd=718098


def isIncreasing(number):
    nStr = str(number)
    for i in range(1, len(nStr)):
        if (nStr[i] < nStr[i-1]):
            return False
    return True

def hasAdjacent(number):
    nStr = str(number)
    i = 1
    while i < len(nStr):
        if (nStr[i] == nStr[i-1]): 
            count = 2
            matchingC = nStr[i]
            i += 1
            while i < len(nStr) and nStr[i] == matchingC:
                count += 1
                i += 1
            if count % 2 == 0:
                return True
        else:
            i += 1
    return False

counter = 0
for number in range(rStart, rEnd+1):
    if (isIncreasing(number) and hasAdjacent(number)):
        counter += 1

print(counter)
