# File Input -----------------
datafile = open("d16.txt")
data1 = datafile.read()
data = data1.splitlines()
datafile.close()
# ----------------------------

flds,tkts = [],[]
for line in data:
    if 'or' in line:
        flds.append(line)
    elif ',' in line:
        tkts.append(line)

def findRanges():
    ranges = {} 

    for line in flds:
        line = line.split(': ')
        field = line[0]
        line = line[1].split(' or ')
        low,high = line[0].split('-'), line[1].split('-')
        lo = (int(low[0]), int(low[1])) 
        hi = (int(high[0]), int(high[1]))
        ranges[field] = (lo, hi)
    return ranges

def validateTkts():
    ranges = findRanges()
    badnums,goodtkts = [],[]

    for line in tkts:
        line = line.split(',')
        tkt = [int(n) for n in line]

        isvalid = True
        for n in tkt: #check tkt against each field in ranges dict
            validn = False
            for i,j in ranges.items():
                a,b,aa,bb = j[0][0], j[0][1], j[1][0], j[1][1] # range values: lo1,lo2, hi1,hi2
                if n in range(a,b+1) or n in range(aa,bb+1): #if it fits into ranges
                    validn = True
                    break
            if not validn:
                badnums.append(n)
                isvalid = False

        if isvalid:
            goodtkts.append(tkt)
            
    return sum(badnums), goodtkts

def findFields():
    ranges = findRanges()
    validfields = {}

    for i,j in ranges.items():
        validfields[i] = []
        a,b,aa,bb = j[0][0], j[0][1], j[1][0], j[1][1]

        for y in range(len(validtkts[0])):
            valid = True
            for tkt in validtkts:
                n = tkt[y]
                if not (n in range(a,b+1) or n in range(aa,bb+1)):
                    valid = False
                    break
            if valid:
                validfields[i].append(y)

    correctIndexes, correctFields = [], {}

    for i in range(len(flds)):
        for fld, potField in validfields.items():
            if len(potField) == i+1:
                for j in potField:
                    if j not in correctIndexes:
                        correctIndexes.append(j)
                        correctFields[fld] = j
                        break

    prod = 1
    for fld, val in correctFields.items():
        if 'departure' in fld:
            prod *= validtkts[0][val]
    
    return prod

num, validtkts = validateTkts()
print(num) # A
print(findFields()) # B