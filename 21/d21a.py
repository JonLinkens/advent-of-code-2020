# File Input -----------------
datafile = open("d21.txt")
data1 = datafile.read()
data = data1.splitlines()
datafile.close()
# ----------------------------

# Helper Functions -----------
def ingredSearch(algn):
    pot_ingreds = []
    for i, igr in enumerate(totalingreds):
        if algn in totalallergens[i]:
            pot_ingreds.append(igr) 
    return set.intersection(*pot_ingreds)
    
def ingredCount(igr):
    c = 0
    for i in totalingreds:
        c+= igr in i
    return c
# ----------------------------
# list of all ingredients, allergens
# set of possible ingredients for each allergens
# len(possible) == 1: add to final set
# igrs with no allergens = ingredients diff final

totalingreds, totalallergens = [], []

uniqueingreds = set(totalingreds)
uniqueallergens = set(totalallergens)

for line in data:
    ingred = set(line[:line.index("(")-1].split(" "))
    totalingreds.append(ingred)
    allergen = set(line[line.index("contains") + len("contains")+1:-1].split(", "))
    totalallergens.append(allergen)
    
    uniqueingreds.update(ingred)
    uniqueallergens.update(allergen)

ingreds = {}
validingreds = set()
while len(ingreds) != len(uniqueallergens):
    for a in uniqueallergens:
        pot = ingredSearch(a).difference(validingreds)
        if len(pot) == 1: # if only 1 valid ingredient (causes the allergy)
            ingred = pot.pop()
            ingreds[a] = ingred
            validingreds.add(ingred)

igrs = uniqueingreds.difference(validingreds)
c = 0
for igr in igrs:
    c += ingredCount(igr)

print(c)
